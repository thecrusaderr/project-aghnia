#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 05, 2019 08:20:56 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import front_page_support
import os.path

def sign_in():
    import sign_in as si
    root.destroy()
    si.vp_start_gui()

def sign_up():
    import sign_up as su
    root.destroy()
    su.vp_start_gui()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global  w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    root.state('zoomed')
    top = Toplevel1 (root)
    front_page_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    front_page_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font21 = "-family {Yu Gothic Light} -size 28 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font22 = "-family {Yu Gothic Light} -size 22 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font24 = "-family {Yu Gothic Light} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("1250x650")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Aghnia")
        top.configure(background="#ffffff")

        self.Sign_In = tk.Button(top)
        self.Sign_In.place(relx=0.6, rely=0.840, height=53, width=246)
        self.Sign_In.configure(activebackground="#ececec")
        self.Sign_In.configure(activeforeground="#000000")
        self.Sign_In.configure(background="#7b003e")
        self.Sign_In.configure(disabledforeground="#a3a3a3")
        self.Sign_In.configure(font=font24)
        self.Sign_In.configure(foreground="#fc94b8")
        self.Sign_In.configure(highlightbackground="#d9d9d9")
        self.Sign_In.configure(highlightcolor="black")
        self.Sign_In.configure(pady="0")
        self.Sign_In.configure(text='''Sign In''')
        self.Sign_In.configure(command=sign_in)

        self.Welcome = tk.Message(top)
        self.Welcome.place(relx=0.3, rely=0.03, relheight=0.1, relwidth=0.435)
        self.Welcome.configure(background="#ffffff")
        self.Welcome.configure(font=font21)
        self.Welcome.configure(foreground="#d1074f")
        self.Welcome.configure(highlightbackground="#d9d9d9")
        self.Welcome.configure(highlightcolor="#000000")
        self.Welcome.configure(text='''Welcome to Aghnia Music Hub''')
        self.Welcome.configure(width=836)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Sign_Up = tk.Button(top)
        self.Sign_Up.place(relx=0.318, rely=0.840, height=53, width=246)
        self.Sign_Up.configure(activebackground="#ececec")
        self.Sign_Up.configure(activeforeground="#000000")
        self.Sign_Up.configure(background="#7b003e")
        self.Sign_Up.configure(disabledforeground="#a3a3a3")
        self.Sign_Up.configure(font=font24)
        self.Sign_Up.configure(foreground="#fc94b8")
        self.Sign_Up.configure(highlightbackground="#d9d9d9")
        self.Sign_Up.configure(highlightcolor="black")
        self.Sign_Up.configure(pady="0")
        self.Sign_Up.configure(takefocus="0")
        self.Sign_Up.configure(text='''Sign Up''')
        self.Sign_Up.configure(command=sign_up)

        self.Need_account = tk.Message(top)
        self.Need_account.place(relx=0.318, rely=0.700, relheight=0.1
                , relwidth=0.170)
        self.Need_account.configure(background="#ffffff")
        self.Need_account.configure(font=font22)
        self.Need_account.configure(foreground="#d1074f")
        self.Need_account.configure(highlightbackground="#d9d9d9")
        self.Need_account.configure(highlightcolor="black")
        self.Need_account.configure(text='''Need an account?''')
        self.Need_account.configure(width=276)

        self.Already_have_account = tk.Message(top)
        self.Already_have_account.place(relx=0.6, rely=0.700, relheight=0.1
                , relwidth=0.139)
        self.Already_have_account.configure(background="#ffffff")
        self.Already_have_account.configure(font=font22)
        self.Already_have_account.configure(foreground="#d1074f")
        self.Already_have_account.configure(highlightbackground="#d9d9d9")
        self.Already_have_account.configure(highlightcolor="black")
        self.Already_have_account.configure(text='''Already have an account?''')
        self.Already_have_account.configure(width=266)

        self.Aghina_Logo = tk.Label(top)
        self.Aghina_Logo.place(relx=0.307, rely=0.16, height=400, width=700)
        self.Aghina_Logo.configure(background="#d9d9d9")
        self.Aghina_Logo.configure(disabledforeground="#a3a3a3")
        self.Aghina_Logo.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"Aghnia Music Logo Temporary.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Aghina_Logo.configure(image=_img0)

if __name__ == '__main__':
    vp_start_gui()