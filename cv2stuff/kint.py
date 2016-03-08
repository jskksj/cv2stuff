import tkinter as tk
import tkinter.ttk as ttk


def buttonPressed():
    print("You will win")
    tk.root.destroy()


def button(root):
    myImage = PhotoImage(file='./tests/images/earth.gif')

    BT = Style()
    BT.theme_use('clam')
    BT.configure('exit.TButton',
                 foreground='#ffffff',
                 background='#%02d%02d%02d' %(128, 192, 200),
                 relief='raised')
    Button1 = Button(root,
                     text='use exit.TButton style',
                     command=buttonPressed,
                     image=myImage,
                     Style='exit.TButton')
    Button1.grid(column=0, row=0)

def openWindow():
    root = tk.Tk()
    root.title('Open a Window')
    root.geometry("500x300+200+10")
    button(root)
    root.mainloop()
