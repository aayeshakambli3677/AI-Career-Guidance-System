from app.services.resume_analyzer import analyze_resume


def extract_text_from_file(file):
    """
    Temporary implementation.
    Reads uploaded file content as text.
    """

    content = file.file.read()

    try:
        return content.decode("utf-8")
    except:
        return str(content)


def analyze_resume_text(resume_text: str):
    """
    Analyze resume and return response
    in format expected by resume_routes.py
    """

    ai_response = analyze_resume(resume_text)

    return {
        "ats_score": 80,
        "feedback": ai_response,
        "strengths": [
            "Good technical skills"
        ],
        "improvements": [
            "Add more measurable achievements"
        ]
    }