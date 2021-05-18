import tkinter
from tkinter import filedialog, messagebox
import pywhatkit

def HANDWRITE(TEXT,DIRECTORY):
    print('[HANDWRITE] gettng image...')
    pywhatkit.text_to_handwriting(TEXT,save_to=DIRECTORY)
    print("[HANDWRITE] Done!")
    messagebox.showinfo('Satus','Done!')


def CLICK():
    DIRECTORYFINDER = filedialog.asksaveasfilename(title='Save as file',
                                                   filetypes=(('png file', '*.png'), ('all files', '*.*')))
    TEXT = INPUT.get("1.0",'end')
    HANDWRITE(TEXT,DIRECTORYFINDER+'.png')

WINDOW = tkinter.Tk()
WINDOW.configure()
WINDOW.geometry('800x500')
WINDOW.title('Text To Handwriting')
WINDOW.resizable(False,False)
BUTTON = tkinter.Button(WINDOW,text='CONVERT IT!',height='5',width='30',command=CLICK)
INPUT = tkinter.Text(WINDOW,height='20',width="96")

BUTTON.place(x=285, y=370)
INPUT.place(x=15,y=9)

WINDOW.mainloop()

