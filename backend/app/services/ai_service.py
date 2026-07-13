def generate_response(prompt):
    prompt = prompt.lower()

    if "internship" in prompt:
        return """Recommended Internships:

1. Java Developer Intern
2. Python Developer Intern
3. Web Development Intern
4. Data Analyst Intern

Platforms:
- Internshala
- LinkedIn
- Indeed
"""

    elif "evaluate" in prompt:
        if len(prompt.strip()) < 20:
            return "Score: 1/10\nAnswer is too short."

        elif len(prompt.strip()) < 50:
            return "Score: 4/10\nGood attempt but needs more details."

        elif len(prompt.strip()) < 150:
            return "Score: 7/10\nGood answer."

        else:
            return "Score: 9/10\nExcellent answer."

    elif "interview" in prompt:
        return """1. Tell me about yourself.
2. Why should we hire you?
3. What are your strengths?
4. What are your weaknesses?
5. Explain OOP.
"""

    elif "roadmap" in prompt:
        return """Month 1 - Learn Programming
Month 2 - Learn SQL
Month 3 - Learn Backend
Month 4 - Build Projects
Month 5 - Learn React
Month 6 - Interview Preparation
"""

    elif "resume" in prompt:
        return """ATS Score: 82/100

Suggestions:
- Add GitHub
- Add Projects
- Add Skills
"""

    elif (
        "career" in prompt
        or "developer" in prompt
        or "software" in prompt
        or "java" in prompt
        or "python" in prompt
    ):
        return """Recommended Careers:

1. Software Engineer
2. Java Developer
3. Python Developer
4. Full Stack Developer
"""

    return "AI Service Running Successfully"