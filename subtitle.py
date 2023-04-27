import tkinter as tk
from queue import Queue
import threading
import time
import voice_translate

class DisplaySubtitle:
    def __init__(self, root, q):
        self.root = root
        self.q = q
        self.root.geometry("600x400+{}+{}".format(int(root.winfo_screenwidth()/2 - 300), int(root.winfo_screenheight()/2 - 30)))
        self.root.configure(bg='red')
        self.root.overrideredirect(True)
        self.root.attributes('-alpha', 0.8)
        self.root.attributes('-topmost', True) # Menambahkan parameter topmost
        self.root.lift()
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "black")
        self.label = tk.Label(root, text="", font=("Lucida Grande", 20), fg="red", bg="black", wraplength=550, highlightthickness=2, highlightbackground="black")
        self.label.place(relx=0.5, rely=1.0, anchor='s')
        self.label.pack(side="top", fill="both", expand=True) # Letakkan label di tengah
        self.thread = threading.Thread(target=self.process_queue)
        self.thread.daemon = True
        self.thread.start()

    def process_queue(self):
        while True:
            try:
                item = self.q.get(block=False)
            except:
                time.sleep(0.1)
            else:
                self.update_label(item)
                self.q.task_done()

    def update_label(self, item):
        original_text, translated_text = item
        self.label.configure(text=translated_text, fg="white") # Mengubah warna teks menjadi putih smoke


if __name__ == '__main__':
    q = Queue()
    root = tk.Tk()
    sub = DisplaySubtitle(root, q)
    threading.Thread(target=voice_translate.record_and_translate, args=(q,)).start()
    root.mainloop()
