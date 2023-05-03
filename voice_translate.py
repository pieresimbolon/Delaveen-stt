import speech_recognition as sr
from googletrans import Translator
import threading
from queue import Queue

def record_and_translate(q):
    r = sr.Recognizer()
    translator = Translator()
    with sr.Microphone() as source:
        while True:
            print("Speak now...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='id-ID')
                print(f"You said: {text}")
                translated_text = translator.translate(text, dest='en').text
                print(f"Translated: {translated_text}")
                q.put((text, translated_text), timeout=0.1)
            except sr.UnknownValueError:
                print("Google Speech Recognition tidak bisa mengerti audio")
            except sr.RequestError as e:
                print(f"tidak bisa menemuka hasil dari Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    q = Queue()
    threading.Thread(target=record_and_translate, args=(q,), daemon=True).start()
    while True:
        try:
            original_text, translated_text = q.get(timeout=0.1)
            print(translated_text)
            q.task_done()
        except:
            pass
