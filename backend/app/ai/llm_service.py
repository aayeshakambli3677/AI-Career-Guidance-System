def generate_response(prompt: str) -> str:
    prompt = prompt.lower()

    # Career Recommendation
    if "career" in prompt:
        return """
Top Careers:
1. Python Developer
2. Java Developer
3. Data Analyst
4. Full Stack Developer
5. Cloud Engineer
6. DevOps Engineer
7.backend devloper

"""

    # Interview Questions
    if "interview" in prompt or "questions" in prompt:
        return """
1. What is OOP?
2. What is difference between list and tuple?
3. Explain SQL joins
4. What is API?
5. What is exception handling?
"""

    # Roadmap
    if "roadmap" in prompt:
        return """
Step 1: HTML, CSS
Step 2: JavaScript
Step 3: React
Step 4: Backend (Python/Java)
Step 5: Database (SQL)
"""

    # Resume analysis
    if "resume" in prompt:
        return """
Strengths: Basic programming knowledge
Weakness: Missing Git, DSA, Projects
ATS Score: 72/100
"""

    return "AI service running in mock mode"