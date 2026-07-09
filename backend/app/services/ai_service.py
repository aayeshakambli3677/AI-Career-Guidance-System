def generate_response(prompt):

    prompt = prompt.lower()

    # Career Advice
    if "career" in prompt:
        return """
Recommended Careers:

1. Java Developer
2. Python Developer
3. Full Stack Developer
4. Software Engineer

Required Skills:
- Java
- SQL
- Spring Boot
- React
- Git

Projects:
- Student Management System
- CareerGPT
- E-Commerce Website

Final Advice:
Focus on Java Full Stack Development and build strong projects.
"""

    # Interview Questions
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

    # Roadmap
    elif "roadmap" in prompt:
        return """
Month 1:
Learn Java Fundamentals

Month 2:
Learn SQL & Database

Month 3:
Learn Spring Boot

Month 4:
Build Backend Projects

Month 5:
Learn React

Month 6:
Interview Preparation & Resume Building
"""

    # Resume Analysis
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
- Improve Resume Formatting
"""

    return "AI Service Running Successfully"