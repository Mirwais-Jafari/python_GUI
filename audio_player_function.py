from tkinter import *
import tkinter as tk
import pygame
import os
def musicplayer():
	root=Tk()
	root.title('Music Player')
	root.geometry("1000x200+200+200")
	pygame.init()
	pygame.mixer.init()
	track=StringVar()
	status=StringVar()
	trackframe=LabelFrame(root,text='song track',bg='gray',fg='white',relief=GROOVE)
	trackframe.place(x=0,y=0,width=600,height=100)
	songtrack=Label(trackframe,textvariable=status,bg='white',fg='white').grid(row=0,column=0,padx=10,pady=5)
	trackstatus=Label(trackframe,textvariable=status,bg='grey',fg='gold').grid(row=0,column=1,padx=10,pady=5)
	buttonframe=LabelFrame(root,text='Control panel',bg='grey',fg='white',bd=5,relief=GROOVE)
	playbtn=Button(trackframe,text='Play',command=playsong,width=6,height=1,fg='blue',bg='gold').grid(row=0,column=0,padx=10,pady=5)
	playbtn=Button(trackframe,text='Pause',command=pausesong,width=8,height=1,fg='blue',bg='gold').grid(row=0,column=1,padx=10,pady=5)
	playbtn=Button(trackframe,text='Un pause',command=unpausesong,width=10,height=1,fg='blue',bg='gold').grid(row=0,column=2,padx=10,pady=5)
	playbtn=Button(trackframe,text='Stop',command=stopsong,width=6,height=1,fg='blue',bg='red').grid(row=0,column=3,padx=0,pady=5)
	songframe=LabelFrame(root,text='Song playlist',bg='brown',fg='white',bd=5,relief=GROOVE)
	songframe.place(x=600,y=0,width=400,height=200)
	scrol_y=Scrollbar(songframe,orient=VERTICAL)
	playlist=Listbox(songframe,yscrollcommmand=scrol_y.set(0,0),selectbackground='gold',selectmode=SINGLE,bg='silver',fg='blue',bd=5,relief=GROOVE)
	scrol_y.pack(side=RIGHT,fill=Y)
	scrol_y.config(command=playlist.yview)
	playlist.pack(fill=BOTH)
	os.chdir(('D:/Music'))
	songtrack=os.listdir()
	for track in songtrack:
		playlist.insert(END,track)
	root.mainloop()


def playsong(track,status,playlist):
	track.set(playlist.get(ACTIVE))
	status.set("-playing")
	pygame.mixer.music.load(playlist.get(ACTIVE))
	pygame.mixer.music.load()
	pygame.mixer.music.play(loops=0)
def stopsong(status):
	status.set('-stopped')
	pygame.mixer.music.stop()
def pausesong(status):
	status.set('-Paused')
	pygame.mixer.music.pause()
def unpausesong(status):
	status.set('-playing')
	pygame.mixer.music.unpause()
musicplayer()