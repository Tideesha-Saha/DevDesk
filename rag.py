import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Optional: Uncomment if you're using OpenAI for LLM calls
# import openai
# openai.api_key = "YOUR_API_KEY"

# === CONFIG ===
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
COLLECTION_NAME = "project_docs"
TOP_K = 5

# === INITIALIZE ===
embedder = SentenceTransformer(EMBEDDING_MODEL)
client = chromadb.Client(Settings())
collection = client.get_or_create_collection("project_docs")

# === RAG Function ===
def retrieve_and_generate(input_text: str):
    # 1. Embed the input text
    input_embedding = embedder.encode(input_text).tolist()

    # 2. Query ChromaDB for similar chunks
    results = collection.query(
        query_embeddings=[input_embedding],
        n_results=TOP_K
    )

    # 3. Extract relevant chunks and metadata
    retrieved_chunks = results['documents'][0]
    metadatas = results['metadatas'][0]

    # 4. Build final prompt for LLM
    context = ""
    for idx, chunk in enumerate(retrieved_chunks):
        meta = metadatas[idx]
        context += f"[{meta['project']} - {meta['type']}] → {chunk}\n\n"

    final_prompt = f"""
You are an expert in your field.

Given the following input:

\"\"\"{input_text}\"\"\"

Here are some relevant information from past projects:

{context}

Use the above as reference and provide refined output accordingly.
"""

    # Optional: Call the LLM (OpenAI/Claude/etc.)
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful software consultant."},
    #         {"role": "user", "content": final_prompt}
    #     ]
    # )
    # return response["choices"][0]["message"]["content"]

    return final_prompt  # return prompt or pass it to next agent