#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 07, 2019 10:20:29 PM IST  platform: Windows NT

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

import your_songs_support

def return_back():
    import front_page as fp
    root.destroy()
    fp.vp_start_gui()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global w, root
    root = tk.Tk()
    root.state('zoomed')
    top = Toplevel1 (root)
    your_songs_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    your_songs_support.init(w, top, *args, **kwargs)
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

        top.geometry("1250x650")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Your Songs")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.song_list = tk.Message(top)
        self.song_list.place(relx=0.052, rely=0.02, relheight=0.09
                , relwidth=0.336)
        self.song_list.configure(background="#ffffff")
        self.song_list.configure(font="-family {Yu Gothic Light} -size 48")
        self.song_list.configure(foreground="#d1074f")
        self.song_list.configure(highlightbackground="#d9d9d9")
        self.song_list.configure(highlightcolor="black")
        self.song_list.configure(text='''Your Songs''')
        self.song_list.configure(width=646)

        self.search_song = tk.Entry(top)
        self.search_song.place(relx=0.818, rely=0.05,height=34, relwidth=0.138)
        self.search_song.configure(background="white")
        self.search_song.configure(disabledforeground="#a3a3a3")
        self.search_song.configure(font="-family {Courier New} -size 10")
        self.search_song.configure(foreground="#000000")
        self.search_song.configure(highlightbackground="#d9d9d9")
        self.search_song.configure(highlightcolor="black")
        self.search_song.configure(insertbackground="black")
        self.search_song.configure(selectbackground="#c4c4c4")
        self.search_song.configure(selectforeground="black")

        self.search_msg = tk.Message(top)
        self.search_msg.place(relx=0.547, rely=0.04, relheight=0.05
                , relwidth=0.264)
        self.search_msg.configure(background="#ffffff")
        self.search_msg.configure(font="-family {Yu Gothic Light} -size 22")
        self.search_msg.configure(foreground="#d1074f")
        self.search_msg.configure(highlightbackground="#d9d9d9")
        self.search_msg.configure(highlightcolor="black")
        self.search_msg.configure(text='''Search for something new''')
        self.search_msg.configure(width=506)

        self.search_btn = tk.Button(top)
        self.search_btn.place(relx=0.854, rely=0.11, height=33, width=126)
        self.search_btn.configure(activebackground="#ececec")
        self.search_btn.configure(activeforeground="#000000")
        self.search_btn.configure(background="#7b003e")
        self.search_btn.configure(disabledforeground="#a3a3a3")
        self.search_btn.configure(font="-family {Yu Gothic Light} -size 12")
        self.search_btn.configure(foreground="#fc94b8")
        self.search_btn.configure(highlightbackground="#d9d9d9")
        self.search_btn.configure(highlightcolor="black")
        self.search_btn.configure(pady="0")
        self.search_btn.configure(text='''Search''')

        self.recommended = tk.Message(top)
        self.recommended.place(relx=0.547, rely=0.18, relheight=0.05
                , relwidth=0.227)
        self.recommended.configure(background="#ffffff")
        self.recommended.configure(font="-family {Yu Gothic Light} -size 22")
        self.recommended.configure(foreground="#d1074f")
        self.recommended.configure(highlightbackground="#d9d9d9")
        self.recommended.configure(highlightcolor="black")
        self.recommended.configure(text='''Recommended Songs''')
        self.recommended.configure(width=436)

        self.songs = tk.Message(top)
        self.songs.place(relx=0.083, rely=0.15, relheight=0.819, relwidth=0.264)
        self.songs.configure(background="#ffffff")
        self.songs.configure(font="-family {Yu Gothic Light} -size 18")
        self.songs.configure(foreground="#000000")
        self.songs.configure(highlightbackground="#d9d9d9")
        self.songs.configure(highlightcolor="black")
        self.songs.configure(text='''{}''')
        self.songs.configure(width=506)

        self.recmmended_song = tk.Message(top)
        self.recmmended_song.place(relx=0.578, rely=0.25, relheight=0.719
                , relwidth=0.222)
        self.recmmended_song.configure(background="#ffffff")
        self.recmmended_song.configure(font="-family {Yu Gothic Light} -size 18")
        self.recmmended_song.configure(foreground="#000000")
        self.recmmended_song.configure(highlightbackground="#d9d9d9")
        self.recmmended_song.configure(highlightcolor="black")
        self.recmmended_song.configure(text='''{}''')
        self.recmmended_song.configure(width=426)

        self.Return = tk.Button(top)
        self.Return.place(relx=0.016, rely=0.02, height=33, width=96)
        self.Return.configure(activebackground="#ececec")
        self.Return.configure(activeforeground="#000000")
        self.Return.configure(background="#7b003e")
        self.Return.configure(disabledforeground="#a3a3a3")
        self.Return.configure(foreground="#fc94b8")
        self.Return.configure(highlightbackground="#d9d9d9")
        self.Return.configure(highlightcolor="black")
        self.Return.configure(pady="0")
        self.Return.configure(text='''Return''')
        self.Return.configure(command=return_back)

if __name__ == '__main__':
    vp_start_gui()