from logging import root
from tkinter import *
from trace import Trace
import tkinter.messagebox
from turtle import bgcolor
from playsound import playsound
import speech_recognition as sr

root = Tk()

root.title("Language Translator")
root.geometry("600x400+10+20")
root.config(bg = '#485063')

global TextBoxText 
TextBoxText = "Waiting for audio..."

def buttonClick():
    r = sr.Recognizer()
    global TextBoxText
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        TextBoxText = "Listening to audio..."
        # TranslatedText.insert('end', "Listening to audio...")

    try:
        # print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n") 
        TextBoxText = query
        TranslatedText.delete("1.0","end")
        TranslatedText.insert('end', TextBoxText)

    except Exception as e:
        print("say that again please.....")
        TranslatedText.delete("1.0","end")
        TextBoxText = "Could not catch that :(" + '\n' + "Press the button to speak again"
        TranslatedText.insert('end', TextBoxText)

ListenButton = Button(root, text="Start listening?", fg='white', bg = '#56717d', font= ('Helvetica', 11), command= buttonClick)
ListenButton.pack(pady = 30)

Label(root, text="Translated Text:", bg= '#5d6475', fg = 'white', font = ('Times', 13)).pack(pady = 30)

TranslatedText = Text(root, height= 10, width= 40, font=('Arial', 10))
TranslatedText.insert('end', TextBoxText)
TranslatedText.pack()
# TranslatedText.config(state= 'disabled')

root.mainloop()