import speech_recognition as sr
import random
import string
import logging

print("Modules are installed successfully!")

# Configure logging
logging.basicConfig(filename='speech_recognition.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Generate a random password
def generate_password():
    s = string.ascii_letters + string.digits + string.punctuation
    print(s)
    n = int(input("Enter the length of the password: "))
    password = "".join(random.choice(s) for i in range(n))
    print("Your password is: ", password)

generate_password()

# Speech recognition
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=10)
        print("Listening... Please speak now.")
        audio = recognizer.listen(source)
        try:
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            with open("transcriptions.txt", "a") as f:
                f.write("You said: {}\n".format(text))
            logging.info("Recognition success.")
        except sr.UnknownValueError:
            print("Google Web Speech could not understand the audio.")
            logging.warning("Unable to recognize speech.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech service; {e}")
            logging.error(f"API request error: {e}")

if __name__ == "__main__":
    while True:
        recognize_speech_from_mic()
        user_input = input("\nPress Enter to continue or type 'quit' to exit: ").strip()
        if user_input.lower() == 'quit':
            break

    print("Exiting the program. Goodbye!")
