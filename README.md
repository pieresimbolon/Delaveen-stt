# Delaveen

Delaveen is a simple Python program that can translate speech in Indonesian language to English language in real-time. This program uses the speech_recognition module from the SpeechRecognition library to record speech from the microphone and the googletrans module from the googletrans library to translate the text into English. The program also uses the tkinter module from the Tkinter library to create a graphical user interface (GUI) that displays the translated text as subtitles.

## How it works

 **Delaveen** is made up of 2 main python programs.
 
"Its a simple program that utilizes the SpeechRecognition and Googletrans libraries to record the user's voice through the microphone and translate the conversation from Indonesian to English in real-time.

The voice_translate.py file contains the record_and_translate function that uses the Recognizer object from SpeechRecognition to record the user's voice through the microphone. Then, the function uses Googletrans to translate the recorded text from Indonesian to English. Finally, the function adds the original text and its translation to a queue, which will be used by the subtitle.py file to display the translated text on the screen.

The subtitle.py file contains the DisplaySubtitle class that creates a tkinter window with a label that will display the translated text. This class also has a process_queue method that will continuously check the queue and display any new translated text found on the label. The class also uses a thread that runs in the background to continuously process the queue. Finally, the main program calls the mainloop function from tkinter to run the GUI.

This program can be used to help users communicate with people who speak a foreign language. However, it is important to note that automatic translations are not always accurate and can lead to misunderstandings that can affect communication."

## How to run it

Install library

**Speech Recognition**

```pip install SpeechRecognition```

**Google translate**

```pip install googletrans```

**Pyaudio**

```pip install pipwin``` then```pipwin install pyaudio```

Download the code then run **subtitle.py**




Btw, the more standardized the language used, the better the translation will be.

## Disclaimer 
This is an ameteur project, use at your own risk.

## License
