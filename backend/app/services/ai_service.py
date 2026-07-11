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

        score = 0

        answer_length = len(prompt.strip())

        # Very Short Answer
        if answer_length < 20:

            return """
Score: 1/10

Strengths:
✔ Attempted the answer.

Weaknesses:
✘ Answer is too short.
✘ Important concepts are missing.

Improvement Suggestions:
- Write at least 2-3 meaningful sentences.
- Explain the concept clearly.
"""

        # Short Answer
        elif answer_length < 50:

            return """
Score: 4/10

Strengths:
✔ Basic attempt made.

Weaknesses:
✘ Missing important details.
✘ Explanation is incomplete.

Improvement Suggestions:
- Add technical concepts.
- Include examples.
"""

        # Medium Answer
        elif answer_length < 150:

            return """
Score: 7/10

Strengths:
✔ Good understanding shown.
✔ Relevant explanation.

Weaknesses:
✘ Could include more details.

Improvement Suggestions:
- Add examples.
- Explain concepts more clearly.
"""

        # Detailed Answer
        else:

            return """
Score: 9/10

Strengths:
✔ Detailed explanation.
✔ Good technical understanding.
✔ Well structured answer.

Weaknesses:
✘ Minor improvements possible.

Improvement Suggestions:
- Add real-world examples.
- Improve answer presentation.
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