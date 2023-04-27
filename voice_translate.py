import speech_recognition as sr
from googletrans import Translator
import tkinter as tk
import threading
from queue import Queue

class DisplaySubtitle:
    def __init__(self, root, q):
        self.root = root
        self.q = q
        self.root.geometry("600x400+{}+{}".format(int(root.winfo_screenwidth()/2 - 300), int(root.winfo_screenheight()/2 - 30)))
        self.root.configure(bg='black')
        self.root.overrideredirect(True)
        self.root.attributes('-alpha', 0.8)
        self.root.attributes('-topmost', True) 
        self.root.lift()
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "black")
        self.label = tk.Label(root, text="", font=("Lucida Grande", 20), fg="white", bg="black", wraplength=550, highlightthickness=2, highlightbackground="black")
        self.label.pack(side="top", fill="both", expand=True) 
        self.thread = threading.Thread(target=self.process_queue, daemon=True)
        self.thread.start()

    def process_queue(self):
        while True:
            try:
                original_text, translated_text = self.q.get(timeout=0.1)
                self.label.configure(text=translated_text)
                self.q.task_done()
            except:
                pass

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
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    q = Queue()
    root = tk.Tk()
    sub = DisplaySubtitle(root, q)
    threading.Thread(target=record_and_translate, args=(q,), daemon=True).start()
    root.mainloop()
