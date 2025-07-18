import speech_recognition as sr

def transcribe_from_file(file_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            print("Reading audio file...")
            audio = recognizer.record(source)

        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        print("\nTranscribed Text:")
        print(text)
        return text

    except FileNotFoundError:
        print("File not found. Please check the path.")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print("Could not connect to Google API:", str(e))

# Example usage
file_path = "example.wav"  # <-- Replace with your WAV file path
transcribe_from_file(file_path)

