This program records audio using a microphone, translates it into English using the Google Translate API, and displays the translated text as subtitles in a GUI using the Tkinter framework. The program also uses the pycaption library to create subtitles in SRT format.

The program consists of several classes and functions. The first class, DisplaySubtitle, is used to display subtitles in the GUI. This class has several functions such as init() to initialize variables and create GUI elements, process_queue() to process the data queue and display subtitles on the label, as well as several other functions to adjust the label's appearance.

The record_and_translate() function is used to handle the recording and translation of audio using the SpeechRecognition library and the Google Translate API. The translated text is then passed to the DisplaySubtitle class to display as subtitles. The program runs continuously until it is manually stopped.
How to use it = Just run the file Delaveen.exe
