import tkinter as tk
from queue import Queue
import threading
import time
import voice_translate


class DisplaySubtitle:
    def __init__(self, root, q):
        self.root = root
        self.q = q
        self.root.geometry(
            "600x400+{}+{}".format(
                int(root.winfo_screenwidth() / 2 - 300),
                int(root.winfo_screenheight() / 2 - 30),
            )
        )
        self.root.configure(bg="red")
        self.root.overrideredirect(True)
        self.root.attributes("-alpha", 0.8)
        self.root.attributes("-topmost", True)  # Menambahkan parameter
        self.root.lift()
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "black")
        self.label = tk.Label(
            root,
            text="",
            font=("Comic Sans MS", 20, "bold italic"),
            fg="white",
            bg="black",
            wraplength=550,
            highlightthickness=0,
        )
        self.label.place(relx=0.5, rely=1.0, anchor="s")
        self.label.pack(
            side="top", fill="both", expand=True
        )  # untuk meletakkan label di tengah
        self.label.bind(
            "<Button-1>", self.on_label_click
        )  # Menambahkan fungsi on_label_click saat label diklik
        self.label.bind(
            "<ButtonRelease-1>", self.on_label_release
        )  # Menambahkan fungsi on_label_release saat label dilepas
        self.label.bind(
            "<B1-Motion>", self.on_label_motion
        )  # Menambahkan fungsi on_label_motion saat label digerakkan
        self.label.bind(
            "<Enter>", self.on_label_enter
        )  # Menambahkan fungsi on_label_enter saat kursor masuk ke dalam label
        self.label.bind(
            "<Leave>", self.on_label_leave
        )  # Menambahkan fungsi on_label_leave saat kursor keluar dari label
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
        self.label.configure(
            text=translated_text, fg="white"
        )  # Mengubah warna teks menjadi putih smoke

    def on_label_click(self, event):
        print("Label clicked at", event.x, event.y)

    def on_label_release(self, event):
        print("Label released at", event.x, event.y)

    def on_label_motion(self, event):
        print("Label moved to", event.x, event.y)

    def on_label_enter(self, event):
        print("Mouse entered the label")

    def on_label_leave(self, event):
        print("Mouse left the label")


if __name__ == "__main__":
    q = Queue()
    root = tk.Tk()
    sub = DisplaySubtitle(root, q)
    threading.Thread(target=voice_translate.record_and_translate, args=(q,)).start()
    root.mainloop()
