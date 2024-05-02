#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Importing all the necessary modules------
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer        
import os

# Initializing the mixer
mixer.init()

# Play, Stop, Load and Pause & Resume functions-------

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
  # Displaying Selected Song title
    song_name.set(songs_list.get(ACTIVE))
  # Loading Selected Song
    mixer.music.load(songs_list.get(ACTIVE))
  # Playing Selected Song
    mixer.music.play()
  # Displaying Status
    status.set("Song PLAYING")


def stop_song(status: StringVar):
  # Displaying Status
    mixer.music.stop()
  # Stopped Song
    status.set("Song STOPPED")


def pause_song(status: StringVar):
  # Displaying Status
    mixer.music.pause()
  # Paused Song
    status.set("Song PAUSED")


def resume_song(status: StringVar):
  # Displaying Status
    mixer.music.unpause()
  # Playing back Song
    status.set("Song RESUMED")
    
# Specifying Directory for fetching Songs------
def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
  # Fetching Songs
    tracks = os.listdir()
  # Inserting Songs into Playlist
    for track in tracks:
        listbox.insert(END, track)

# Creating the master GUI
 # to create an empty window
root = Tk()
root.geometry('800x280')
 # Title of the window
root.title('Pratap Music Player')
root.resizable(0, 0)

# Creating All the frames -------
 # Creating Song Frame
song_frame = LabelFrame(root, text='Current Song', bg='dodgerblue', width=500, height=110)
song_frame.place(x=0, y=0)
 # Creating Button Frame
button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=800, height=150)
button_frame.place(y=110)
 # Creating Playlist Frame
listbox_frame = LabelFrame(root, text='Playlist', bg='DodgerBlue')
listbox_frame.place(x=400, y=0, height=220, width=400)

# All StringVar variables
current_song = StringVar(root, value='<Not selected>')

song_status = StringVar(root, value='<Not Available>')

# Creating Playlist ListBox ----
playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=2)

# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', bg='aliceblue', font=('Times', 10, 'bold')).place(x=5, y=28)

song_lbl = Label(song_frame, textvariable=current_song, bg='aliceblue', font=("Times", 12), width=25)
song_lbl.place(x=160, y=26)

# Inserting Buttons in the main Frame --------
play_btn = Button(button_frame, text='      Play▶️', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=15, y=15)

pause_btn = Button(button_frame, text='Pause⏸️', bg='Aqua', font=("Georgia", 13), width=7,
                    command=lambda: pause_song(song_status))
pause_btn.place(x=105, y=15)

stop_btn = Button(button_frame, text='Stop⏹️', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=195, y=15)

resume_btn = Button(button_frame, text='Resume⏯️', bg='Aqua', font=("Georgia", 13), width=8,
                    command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=15)

load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35,
                  command=lambda: load(playlist))
load_btn.place(x=10, y=78)

# Label at the bottom that displays the state of the music
Label(root, textvariable=song_status, bg='lightblue', font=('Times', 10), justify=LEFT).pack(side=BOTTOM, fill=X)

# Finalizing the GUI
root.update()
root.mainloop()


# In[ ]:





# In[ ]:




