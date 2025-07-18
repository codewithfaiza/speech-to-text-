
import speech_recognition as sr

def transcribe_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            print("Adjusting for background noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening... Speak clearly into the microphone.")
            
            audio_data = recognizer.listen(source, timeout=15)
            print("Processing...")

            # Transcribe speech using Google's API
            text = recognizer.recognize_google(audio_data)
            print("\nTranscribed Text:")
            print(text)
            return text

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start.")
    except sr.UnknownValueError:
        print("Sorry, couldn't understand the audio.")
    except sr.RequestError as e:
        print("API request error:", str(e))

# Run the function
transcribe_from_mic()
