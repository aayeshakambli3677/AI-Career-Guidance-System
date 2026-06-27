from app.services.speech_to_text import speech_to_text

result = speech_to_text("sample_audio.wav")

print("\n===== SPEECH TO TEXT =====\n")
print(result)