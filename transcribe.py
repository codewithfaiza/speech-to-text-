
import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            print("Listening to audio...")
            audio = recognizer.record(source)
            print("Transcribing...")
            text = recognizer.recognize_google(audio)
            print("Transcription:")
            print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    file_path = input("Enter path to your WAV audio file: ")
    transcribe_audio(file_path)
