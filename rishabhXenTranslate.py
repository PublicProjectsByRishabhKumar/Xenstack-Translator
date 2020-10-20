from googletrans import Translator  #sudo pip3 install googletrans
from tkinter import * # sudo apt-get install python3-tk
import tkinter.font as font
tk = Tk()
canvas = Canvas(tk,width = 420,height = 320)
tk.title("Translator English to Hindi")
canvas.pack()

cusfont = font.Font(size = 15)
sub = Label(tk, text= "powered by Google Translate")
canvas.create_window(200, 20, window=sub)

sub01 = Label(tk, text= "Type something in English")
canvas.create_window(120, 70, window=sub01)

e1 = Entry(tk,font = cusfont)
canvas.create_window(200, 100, window=e1,height = 32,width = 350)

def Translate2Hindi():  
    try:
        canvas.delete("label1")
    except:
        pass
    txt = e1.get()
    translator = Translator()
    result = translator.translate(txt,src = "en",dest = "hi")
    label1 = Label(tk, text= result.text,bg = "white",font = cusfont)
    wid = len(result.text)*8+20
    canvas.create_window(wid/2, 230, window=label1)
    label1.pack()

bt1 = Button(text='Translate', command=Translate2Hindi)
canvas.create_window(200, 180, window=bt1)
tk.mainloop()