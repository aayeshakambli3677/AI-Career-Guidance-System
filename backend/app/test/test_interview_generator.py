from app.services.interview_generator import generate_questions

result = generate_questions("Java Developer")

print("\n===== INTERVIEW QUESTIONS =====\n")
print(result)