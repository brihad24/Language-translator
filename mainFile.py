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

TextBoxText = StringVar()

def buttonClick():
    r = sr.Recognizer()
    global TextBoxText
    # TranslatedText.config(state= 'normal')
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        TextBoxText.set("Listening to audio...")

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")
        TextBoxText.set(query)

    except Exception as e:
        print("say that again please.....")
        TextBoxText.set("Could not catch that :(" + '\n' + "Press the button to speak again")
    # tkinter.messagebox.showinfo('Translator', 'Listening to audio...           ')

ListenButton = Button(root, text="Start listening?", fg='white', bg = '#56717d', font= ('Helvetica', 11), command= buttonClick)
ListenButton.pack(pady = 30)

Label(root, text="Translated Text:", bg= '#5d6475', fg = 'white', font = ('Times', 13)).pack(pady = 30)

DisplayText = Label(root, text=TextBoxText, bg= 'white', fg = 'black', font = ('Times', 13), width= 40, height= 10).pack(pady = 30)

TextBoxText.set("Waiting for audio...")
# TranslatedText = Text(root, height= 10, width= 40)
# TranslatedText.insert('end', TextBoxText)
# TranslatedText.pack()
# TranslatedText.config(state= 'disabled')

root.mainloop()