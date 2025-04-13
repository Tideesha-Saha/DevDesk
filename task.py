# from crewai import Task
# from agents import business_analyst,design_agent

# # Business analyst task
# business_analyst_task = Task(
#     # description=("Given a high-level business requirement, create detailed user stories following the standard format: "
#                 # "'As a [role], I want to [action], so that [benefit]'. Ensure clarity, completeness, and relevance to stakeholders."),

#     description=(
#         "Given a high-level business requirement, create a detailed list of user stories in the format: "
#         "'As a [role], I want to [action], so that [benefit]'. "
#         "Ensure completeness, clarity, and relevance, and include well-defined acceptance criteria. "
#         "**Do NOT include system design details or technical aspects.**"
#     ),

#     agent=business_analyst,
#     expected_output="A structured list of user stories with clear acceptance criteria.",

# )

# # Design agent task
# design_task = Task(
   
#     description=(
#         "Create a detailed software architecture and system design **based strictly on the user stories** from the Business Analyst for {topic}. "
#         "Ensure the design includes system components, database choices, data flow, and UI wireframes. "
#         "**Avoid repeating business requirements, user stories, security considerations, or future enhancements.**"
#     ),
#      inputs=["topic"],
#     agent=design_agent, 
#     expected_output="A structured design document including system architecture, tech stack, and UI wireframes, avoiding duplicates",


# )



# #task.py
# from crewai import Task
# from agents import business_analyst, design_agent,developer_agent,tester_agent

# # Business analyst task
# business_analyst_task = Task(
#     description=(
#         "Given a high-level business requirement, create a detailed list of user stories in the format: "
#         "'As a [role], I want to [action], so that [benefit]'. "
#         "Ensure completeness, clarity, and relevance, and include well-defined acceptance criteria. "
#         "**Do NOT include system design details or technical aspects.**"
#     ),
#     agent=business_analyst,
#     expected_output="A structured list of user stories with clear acceptance criteria.",
# )

# # Design agent task
# design_task = Task(
#     description=(
#         "Create a detailed software architecture and system design **based strictly on the user stories** from the Business Analyst for {topic}. "
#         "Ensure the design includes system components, database choices, diagrams, data flow, and UI wireframes. "
#         "Ensure that the design is well formatted with structured headings. Avoid excessive large headings"
#         "**Avoid repeating business requirements, user stories, security considerations, or future enhancements.**"
#     ),
#     inputs=["topic"],  # Explicit input for topic
#     agent=design_agent, 
#     expected_output="A structured design document including system architecture, tech stack, and UI wireframes, avoiding duplicates",
# )


# developer_task = Task(
#      description=(
#         "Develop a fully functional, scalable, and well-structured codebase for {topic} based on the system design document. "
#         "Ensure best practices in software development, modularity, and efficiency. "
#         "Write production-ready code that adheres to industry standards, including security, performance, and maintainability. "
#         "Use appropriate design patterns and follow the specified tech stack. "
#         "Document the code with meaningful comments explaining key implementation decisions, logic flow, and API endpoints (if applicable). "
#         "Ensure the implementation is testable, extendable, and ready for deployment."
#     ),
#     inputs=["topic"],  # Explicit input for topic
#     agent=developer_agent,
#         expected_output=(
#         "A fully implemented, structured, and well-commented codebase for the specified project, "
#         "ready for testing, deployment, and future enhancements."
#     ),
# )

# tester_task = Task(
#     description=(
#         "Based on the implementation code and original requirements, create a comprehensive test suite for {topic}. "
#         "Generate test cases that cover unit testing, integration testing, and system testing. "
#         "Include test cases for validating both functional and non-functional requirements. "
#         "For each test case, specify: test ID, test description, preconditions, test steps, expected results, and status. "
#         "Prioritize tests based on critical functionality and potential risk areas. "
#         "Focus on ensuring all user stories have appropriate test coverage."
#     ),
#     inputs=["topic"],
#     agent=tester_agent,
#     expected_output=(
#         "A detailed test report outlining passed and failed test cases, identified bugs with reproducible steps, "
#         "and confirmation that the software is functioning correctly and ready for production deployment."
#         "A complete test plan with detailed test cases organized by test level (unit, integration, system) and priority."
#     ),
# )


from crewai import Task
from agents import business_analyst, design_agent,developer_agent,tester_agent

# Business analyst task
business_analyst_task = Task(
    description=(
        "Given a high-level business requirement, create a detailed list of user stories in the format: "
        "'As a [role], I want to [action], so that [benefit]'. "
        "Ensure completeness, clarity, and relevance, and include well-defined acceptance criteria. "
        "*Do NOT include system design details or technical aspects.*"
    ),
    agent=business_analyst,
    expected_output="A structured list of user stories with clear acceptance criteria.",
)

# Design agent task
design_task = Task(
    description=(
        # "Create a detailed software architecture and system design *based strictly on the user stories* from the Business Analyst for {topic}. "
        # "Ensure the design includes system components, database choices, diagrams, data flow, and UI wireframes. "
        # "Ensure that the design is well formatted with structured headings. Avoid excessive large headings"
        #  "*Avoid repeating business requirements, user stories, security considerations, or future enhancements.*"
        #  "Create a detailed software architecture and system design **based strictly on the user stories** from the Business Analyst for {topic}. "
        # "Ensure the design includes system components, database choices, diagrams, data flow, and UI wireframes. "
        # "Ensure that the design is well formatted with structured headings. Avoid excessive large headings"
        # "**Avoid repeating business requirements, user stories, security considerations, or future enhancements.**"
        "Create a detailed software architecture and system design **based strictly on the user stories** from the Business Analyst for {topic}. "
        "Ensure the design includes system components, database choices, data flow, and UI wireframes. "
        "**Avoid repeating business requirements, user stories, security considerations, or future enhancements.**"
         
    ),
    inputs=["topic"],  # Explicit input for topic
    agent=design_agent, 
    expected_output="A structured design document including system architecture, tech stack, and UI wireframes, avoiding duplicates",
)


developer_task = Task(
     description=(
        # "You are a senior software engineer at a leading tech company. Based on the provided system design, generate clean, modular, and production-grade development code."
        # "The code should align with the software development lifecycle (SDLC) documentation standards used in large-scale tech environments."
        # "Your code must reflect real-world implementation practices, follow SOLID principles, and avoid unnecessary scaffolding or placeholder comments."
        # "Develop a fully functional, scalable, and well-structured codebase for {topic} based on the system design document. "
        # "Ensure best practices in software development, modularity, and efficiency. "
        # "Write production-ready code that adheres to industry standards, including security, performance, and maintainability. "
        # "Use appropriate design patterns and follow the specified tech stack. "
        # "Document the code with meaningful comments explaining key implementation decisions, logic flow, and API endpoints (if applicable). "
        # "Ensure the implementation is testable, extendable, and ready for deployment."
        # "You are a senior software engineer at a leading tech company. Based on the provided system design document (including database schema, partial backend code, and frontend components), "
        # "develop a clean, modular, and production-grade codebase. "
        # "Ensure the implementation aligns with SDLC best practices. "
        # "The code must reflect real-world implementation practices, follow SOLID principles, and be secure, efficient, and maintainable. "
        # "Use appropriate design patterns. Structure the backend with controllers, routes, services, and models. "
        # "Create a reusable component-based frontend. Include database schema enhancements if necessary. "
        # "Document the code with meaningful comments explaining key implementation decisions and logic."
        
        # "You are a senior software engineer at a top tech company. Based on the provided design document, "
        # "develop a complete, modular, and production-grade code for {topic}. "
        # "This system could be a web app, mobile app, desktop application, game, AI system, or backend API — adapt accordingly. "
        # "Follow real-world software engineering practices including SOLID principles, modular design, and maintainability. "
        # "Use appropriate design patterns, apply clean architecture principles, and optimize for performance, scalability, and security. "
        # "Document your code meaningfully, explaining major decisions, core logic, and key modules. "
        # "The system must be testable, extendable, and deployment-ready across modern environments."
        
        "Develop a fully functional, scalable, and well-structured codebase for {topic} based on the business requirement design document. "
        "Ensure best practices in software development, modularity, and efficiency. "
        "Write production-ready code that adheres to industry standards, including security, performance, and maintainability. "
        "Use appropriate design patterns and follow the specified tech stack. "
        "Document the code with meaningful comments explaining key implementation decisions, logic flow, and API endpoints (if applicable). "
        "Ensure the implementation is testable, extendable, and ready for deployment."


    ),
    inputs=["topic"],  # Explicit input for topic
    agent=developer_agent,
        expected_output=(
        # "Return only the development code in a clean, professional format, as it would appear in a codebase during the development phase."
        # "Do not include explanations, disclaimers, placeholders like 'implement later', or comments suggesting that the code is incomplete."
        # "Output should consist solely of complete, ready-to-integrate code — clean, idiomatic, and suitable for inclusion in SDLC documentation or enterprise repositories."
        # "Ready for testing, deployment, and future enhancements."
        # "A fully implemented, structured, and well-commented codebase for the specified project, "
        # "ready for testing, deployment, and future enhancements."
        # "A complete, modular, and production-ready codebase including backend (Node.js + Express), frontend (React.js), and database (PostgreSQL). "
        # "Output should be structured into folders/files and ready for deployment. No placeholders or incomplete logic."
    
        # "A fully implemented, modular, and production-grade codebase for the requested software system. "
        # "The implementation must include appropriate folder structure, clean code, reusable components, and relevant setup/config files. "
        # "Use best practices suited to the system type — e.g., React/Vue for frontend, Node/Django/Spring Boot for backend, Unity for games, Flutter/Kotlin/Swift for mobile apps, etc. "
        # "Do not include placeholders or partial code. Output must be complete, idiomatic, and suitable for testing, deployment, and scaling in real-world scenarios. "
        # "Include inline comments and documentation where necessary for clarity and onboarding new developers."

        "A fully implemented, structured, and well-commented codebase for the specified project, "
        "ready for testing, deployment, and future enhancements."
    ),
)

tester_task = Task(
    description=(
        # "Given a piece of development code, generate the complete testing code required to validate its functionality for {topic}."
        # "The tests should follow the structure and conventions used in enterprise-scale test suites. Include unit tests, edge case handling, and integration tests (where relevant)."
        # "Use the appropriate testing framework based on the language of the development code."
        # "Include test cases for validating both functional and non-functional requirements. "
        # "Prioritize tests based on critical functionality and potential risk areas. "
        # "Based on the implementation code and original requirements, create a comprehensive test suite for {topic}. "
        # "Generate test cases that cover unit testing, integration testing, and system testing. "
        # "Include test cases for validating both functional and non-functional requirements. "
        # "For each test case, specify: test ID, test description, preconditions, test steps, expected results, and status. "
        # "Prioritize tests based on critical functionality and potential risk areas. "
        # "Focus on ensuring all user stories have appropriate test coverage."
        "You are a senior QA engineer at a leading software company. Based on the provided production-grade codebase, "
        "develop a complete suite of automated tests to validate the system’s functionality, performance, and reliability for {topic}. "
        "Follow best practices in software testing, such as test-driven development (TDD), black-box and white-box testing, and boundary value analysis. "
        "Create tests that cover API endpoints, database operations, business logic, and user interactions. "
        "Include both positive and negative test cases, edge cases, and integration tests. "
        "Ensure the test suite is easy to maintain, modular, and runnable via test runners such as Jest, Mocha (for Node.js), and React Testing Library. "
        "Mock dependencies and isolate units of code as appropriate. "
        "Clearly document the purpose of each test case and its expected behavior."
    ),
    inputs=["topic"],
    agent=tester_agent,
    expected_output=(
        # "Return only the testing code."
        # "No test plan, explanation, disclaimers, or comments stating the code is incomplete."
        # "The output should be fully structured as executable test code, suitable for inclusion in a production codebase during the testing phase of the SDLC."
        # "The test code must:Use proper test naming conventions, Be grouped in test classes or suites (if supported by the framework), Cover positive, negative, and edge cases, Mock dependencies if necessary, Be clean and idiomatic for the language and framework used"
        # "A detailed test report outlining passed and failed test cases, identified bugs with reproducible steps, "
        # "and confirmation that the software is functioning correctly and ready for production deployment."
        #  "A detailed test report outlining passed and failed test cases, identified bugs with reproducible steps, "
        # "and confirmation that the software is functioning correctly and ready for production deployment."
        # "A complete test plan with detailed test cases organized by test level (unit, integration, system) and priority."
        "A complete, structured, and production-grade test suite for the provided codebase. "
        "Include backend API tests (e.g., using Jest or Mocha with Supertest), frontend component tests (e.g., React Testing Library or Jest), and database validation logic. "
        "Ensure high test coverage, clear assertions, proper mocking, and independence between tests. "
        "Each test should be self-explanatory and follow best practices for unit, integration, and end-to-end testing. "
        "Output should be ready for CI/CD pipelines and future maintainability."
    ),
)