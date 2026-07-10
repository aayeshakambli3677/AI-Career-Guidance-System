def generate_response(prompt: str) -> str:

    prompt = prompt.lower()

    # Career Advice
    if "career counselor" in prompt or "best career options" in prompt:
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
- E-commerce Website

Final Advice:
Focus on Java Full Stack Development and build projects.
"""

    # Internship Recommendation
    elif "internship" in prompt:
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

    # Interview
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