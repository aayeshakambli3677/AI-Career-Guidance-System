import speech_recognition as sr


def speech_to_text(audio_file_path: str) -> str:
    """
    Convert speech audio to text.
    """

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        return text

    except FileNotFoundError:
        return "Audio file not found."

    except sr.UnknownValueError:
        return "Speech could not be understood."

    except sr.RequestError:
        return "Speech recognition service unavailable."

    except Exception as e:
        return f"Error: {str(e)}"