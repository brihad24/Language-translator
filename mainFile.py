from logging import root
from tkinter import *
from trace import Trace
import tkinter.messagebox
from turtle import bgcolor
from SpeechToText import *

root = Tk()

root.title("Language Translator")
root.geometry("600x400+10+20")
root.config(bg = '#485063')

def buttonClick():
    tkinter.messagebox.showinfo('Translator', 'Listening to audio...           ')
    print(speechConversion())

ListenButton = Button(root, text="Start listening?", fg='white', bg = '#56717d', font= ('Helvetica', 11), command= buttonClick)
ListenButton.pack(pady = 30)

Label(root, text="Translated Text:", bg= '#5d6475', fg = 'white', font = ('Times', 13)).pack(pady = 30)

TranslatedText = Text(root, height= 10, width= 40)
TranslatedText.insert('end', "Waiting for audio...")
TranslatedText.pack()
TranslatedText.config(state= 'disabled')

root.mainloop()