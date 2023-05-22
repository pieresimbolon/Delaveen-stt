# Delaveen

ini adalah program iseng-iseng menggunakan Python yang sangat sederhana yang dapat menerjemahkan ucapan dari bahasa Indonesia ke bahasa Inggris secara real-time. dengan menggunakan modul speech_recognition dari library SpeechRecognition untuk menangkap ucapan dari mikrofon (awalanya ingin menggunakan (Whisper AI), dan modul googletrans dari perpustakaan googletrans untuk menerjemahkan teks ke dalam bahasa Inggris (awalnya saya ingin menggunakan deepl). Selain itu, program ini menggunakan modul tkinter dari perpustakaan tkinter untuk membuat antarmuka pengguna grafis (GUI) yang menampilkan teks terjemahan sebagai subtitle.

## How it works
 
File voice_translate.py berisi fungsi yang disebut record_and_translate yang menggunakan objek Recognizer dari SpeechRecognition untuk merekam suara pengguna melalui mikrofon. Selanjutnya, fungsi tersebut menggunakan Googletrans untuk menerjemahkan teks rekaman dari bahasa Indonesia ke bahasa Inggris. Terakhir, fungsi menambahkan teks asli dan terjemahannya ke antrian, yang akan digunakan oleh file subtitle.py untuk menampilkan teks terjemahan di layar.

File subtitle.py berisi kelas DisplaySubtitle, yang membuat jendela tkinter dengan label yang menampilkan teks terjemahan. Kelas ini juga memiliki metode process_queue yang terus menerus memeriksa antrian dan menampilkan teks terjemahan baru yang ditemukan pada label. Selain itu, kelas menggunakan utas latar belakang untuk terus memproses antrean. Terakhir, program utama memanggil fungsi mainloop dari tkinter untuk menjalankan GUI dengan lancar.

Program ini dapat membantu pengguna dalam berkomunikasi dengan individu yang berbicara bahasa asing. Namun, penting untuk diperhatikan bahwa terjemahan otomatis tidak selalu akurat dan dapat menyebabkan kesalahpahaman yang dapat memengaruhi komunikasi.

## How to run 
**Speech Recognition**

```pip install SpeechRecognition```

**Google translate**

```pip install googletrans```

**Pyaudio**

```pip install pipwin``` then```pipwin install pyaudio```

Download dan jalankan **subtitle.py**

semakin baku bahasa yang digunakan, semakin baik hasil terjemahannya.

