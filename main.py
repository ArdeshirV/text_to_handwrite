import tkinter
import pywhatkit

def HANDWRITE(TEXT,DIRECTORY):
    print('[HANDWRITE] gettng image...')
    pywhatkit.text_to_handwriting(TEXT,save_to=DIRECTORY)
    print("[HANDWRITE] Done1")



WINDOW = tkinter.Tk()
WINDOW.configure(bg='light blue')
WINDOW.geometry('800x500')
WINDOW.title('Text To Handwriting')
WINDOW.resizable(False,False)
LABEL = tkinter.Label(WINDOW,text='STATUS : ',bg='light blue',fg='black')
BUTTON = tkinter.Button(WINDOW,text='CONVERT IT!',height='5',width='30',bg='gray')
INPUT = tkinter.Text(WINDOW,height='30',width="50",bg='gray',fg='black')

LABEL.place(x=580,y=20)
BUTTON.place(x=500, y=350)
INPUT.place(x=15,y=7)

WINDOW.mainloop()

