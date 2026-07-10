def generate_response(prompt):

    prompt = prompt.lower()

    # =========================
    # INTERNSHIP
    # =========================

    if "internship" in prompt:

        return """
Recommended Internships:

1. Java Developer Intern
2. Python Developer Intern
3. Web Development Intern
4. Data Analyst Intern

Platforms:
- Internshala
- LinkedIn
- Indeed

Preparation:
- Build Projects
- Improve Resume
- Practice Interviews
"""

    # =========================
    # ANSWER EVALUATION
    # =========================

    elif "evaluate" in prompt:

        if "what is oop" in prompt:

            return """
Score: 8/10

Strengths:
✔ Correct understanding of OOP.
✔ Answer is relevant.

Weaknesses:
✘ Too short.
✘ Did not mention pillars of OOP.

Improvement Suggestions:
- Mention Encapsulation, Inheritance, Polymorphism and Abstraction.

Better Sample Answer:

OOP (Object-Oriented Programming) is a programming paradigm that organizes software using objects and classes. The four pillars are Encapsulation, Inheritance, Polymorphism and Abstraction.
"""

        elif "arraylist" in prompt and "linkedlist" in prompt:

            return """
Score: 8/10

Strengths:
✔ Relevant answer.
✔ Correct concept.

Weaknesses:
✘ Missing performance comparison.

Improvement Suggestions:
- Explain indexing speed.
- Explain insertion and deletion performance.

Better Sample Answer:

ArrayList uses a dynamic array internally and provides fast random access using indexes. LinkedList uses a doubly linked list internally and is better for frequent insertions and deletions.
"""

        elif "jdbc" in prompt:

            return """
Score: 8/10

Strengths:
✔ Correct topic identified.

Weaknesses:
✘ Missing full form.

Improvement Suggestions:
- Explain database connectivity.

Better Sample Answer:

JDBC (Java Database Connectivity) is an API that allows Java applications to connect and interact with databases.
"""

        elif "exception" in prompt:

            return """
Score: 8/10

Strengths:
✔ Understands exceptions.

Weaknesses:
✘ Missing keywords.

Improvement Suggestions:
- Mention try, catch and finally.

Better Sample Answer:

Exception Handling is a mechanism used to handle runtime errors and maintain normal program flow using try, catch and finally blocks.
"""

        elif "spring boot" in prompt:

            return """
Score: 8/10

Strengths:
✔ Relevant answer.

Weaknesses:
✘ Missing features.

Improvement Suggestions:
- Mention auto configuration and embedded server.

Better Sample Answer:

Spring Boot simplifies Java application development by providing auto configuration, starter dependencies and embedded servers.
"""

        elif "rest api" in prompt:

            return """
Score: 8/10

Strengths:
✔ Correct concept.

Weaknesses:
✘ Missing HTTP methods.

Improvement Suggestions:
- Mention GET, POST, PUT and DELETE.

Better Sample Answer:

REST API is an architectural style used for communication between client and server applications using HTTP methods.
"""

        elif "get" in prompt and "post" in prompt:

            return """
Score: 8/10

Strengths:
✔ Relevant answer.

Weaknesses:
✘ Missing comparison points.

Improvement Suggestions:
- Explain usage and security differences.

Better Sample Answer:

GET retrieves data from the server while POST sends data to the server. POST is generally more secure because data is sent in the request body.
"""

        elif "sql join" in prompt:

            return """
Score: 8/10

Strengths:
✔ Correct topic.

Weaknesses:
✘ Missing join types.

Improvement Suggestions:
- Mention INNER JOIN, LEFT JOIN, RIGHT JOIN and FULL JOIN.

Better Sample Answer:

SQL JOIN combines rows from multiple tables based on a related column.
"""

        elif "polymorphism" in prompt:

            return """
Score: 8/10

Strengths:
✔ Correct concept.

Weaknesses:
✘ Missing types.

Improvement Suggestions:
- Mention method overloading and overriding.

Better Sample Answer:

Polymorphism allows one interface to represent multiple forms. It is achieved through method overloading and method overriding.
"""

        elif "tell me about yourself" in prompt:

            return """
Score: 8/10

Strengths:
✔ Good introduction.

Weaknesses:
✘ Missing achievements.

Improvement Suggestions:
- Mention education, skills and projects.

Better Sample Answer:

My name is Aayesha Kambli. I am pursuing a Diploma in Computer Engineering. I have knowledge of Java, SQL, HTML, CSS and JavaScript. I am currently learning Java Full Stack Development and have worked on projects like CareerGPT.
"""

        else:

            return """
Score: 7/10

Strengths:
✔ Relevant answer.

Weaknesses:
✘ Needs more detail.

Improvement Suggestions:
- Add examples.
- Explain concepts clearly.
"""

    # =========================
    # HR QUESTIONS
    # =========================

    elif "hr interview questions" in prompt:

        return """
1. Tell me about yourself.
2. Why should we hire you?
3. What are your strengths?
4. What are your weaknesses?
5. Where do you see yourself in 5 years?
6. Why do you want to work with us?
7. Tell me about a challenge you faced?
8. How do you handle pressure?
9. Describe a teamwork experience.
10. What motivates you?
"""

    # =========================
    # INTERVIEW QUESTIONS
    # =========================

    elif "interview" in prompt or "questions" in prompt:

        return """
1. What is OOP?
2. Difference between ArrayList and LinkedList?
3. What is JDBC?
4. Explain Exception Handling.
5. What is Spring Boot?
6. What is REST API?
7. Difference between GET and POST?
8. What is SQL Join?
9. What is Polymorphism?
10. Tell me about yourself.
"""

    # =========================
    # ROADMAP
    # =========================

    elif "roadmap" in prompt:

        return """
Month 1: Learn Java Fundamentals

Month 2: Learn SQL & Database

Month 3: Learn Spring Boot

Month 4: Build Backend Projects

Month 5: Learn React

Month 6: Interview Preparation & Resume Building
"""

    # =========================
    # RESUME
    # =========================

    elif "resume" in prompt:

        return """
ATS Score: 82/100

Strengths:
- Java
- SQL
- Projects

Improvements:
- Add GitHub Link
- Add Internship Details
"""

    # =========================
    # CAREER
    # =========================

    elif (
        "career" in prompt
        or "developer" in prompt
        or "java" in prompt
        or "python" in prompt
        or "skills" in prompt
    ):

        return """
Recommended Careers:

1. Java Developer
2. Python Developer
3. Full Stack Developer
4. Software Engineer
"""

    return "AI Service Running Successfully"