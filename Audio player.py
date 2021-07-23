#                                           IN THE NAME OF ALLAH
# import the required libraries
from tkinter import *
import pygame
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import webbrowser


root=Tk()    # Make a widget
root.title('Mp3 Player')    # make title
root.geometry("470x310")      # personal width and height
# root.iconbitmap('D:/icon/mp32.gif')     # make an icon

# use from PIl to make an image in our program
# my_image=ImageTk.PhotoImage(Image.open("M:/icon/pic.jpg"))
# my_label=Label(image=my_image)
# my_label.place(x=0,y=0)

root.resizable(False,False)    # no one can resize the window
pygame.mixer.init()
root.song_added=False

def add_one_song():
	file = filedialog.askopenfilename(title='select your cool music track')
	song = file.replace("M:/Music", "")
	song = song.replace(".mp3", "")
	song_box.insert(END, song)
	status_bar['text']=file
	root.song_added=True

def add_songs():
	# use from filedialog to read any thing
	songs=filedialog.askopenfilenames(initialdir='/',title="Select your cool music tracks"
									  ,filetypes=(('mp3 Files','*.*'),))
	# use for loop for replacing the songs in our listbox
	for song in songs:
		song=song.replace("M:/Music","")
		song=song.replace(".mp3","")
		song_box.insert(END,song)
	root.song_added=True
# define remove song function
def remove_song():
	song_box.delete(ACTIVE)     # delete the active song
	pygame.mixer.music.stop()    # stop the current song hint: it is not absolutely need


def remove_songs():
	song_box.delete(0,END)    # remove all song from listbox give rang it
	pygame.mixer.music.stop()


def play():
	if(root.song_added==False):
		messagebox.showinfo('Hint', 'First add some music')
		status_bar['text']='First add some music'
		file=filedialog.askopenfilename()
		song =file.replace("M:/Music", "")
		song = song.replace(".mp3", "")
		song_box.insert(END, song)
		root.song_added=True
		status_bar['text']='First add some music'
	else:
		song=song_box.get(ACTIVE)    # get the active song
		song=f"M:/Music/{song}.mp3"   # from this directory
		pygame.mixer.music.load(song)  # loading the song
		pygame.mixer.music.play()
		status_bar['text']='Playing Music'


# define stop function
def stop():
	if (root.song_added == False):
		messagebox.showinfo('Hint', 'First add some music')
		status_bar['text'] = 'First add some music'
	else:
		pygame.mixer.music.stop()    # stop the song
		status_bar['text']='Music Stopped'

# introduction	paused variable
global paused
paused=False
def pause(is_paused):
	if (root.song_added == False):
		messagebox.showinfo('Hint', 'First add some music')
		status_bar['text'] = 'First add some music'
	else:
		# because pause function do two action and we need it to use lambda
		global paused
		paused=is_paused

		if is_paused:
			pygame.mixer.music.unpause()
			paused= False
			status_bar['text']='Music Resumed'

		else:
			pygame.mixer.music.pause()
			paused= True
			status_bar['text']='Music paused'


# define back function to play the previous song
def back():
	if (root.song_added == False):
		messagebox.showinfo('Hint', 'First add some music')
		status_bar['text'] = 'First add some music'
	else:
		try:
			if song_box:
				back_song = song_box.curselection()
				back_song=back_song[0]-1
				song=song_box.get(back_song)
				song=f"M:/Music/{song}.mp3"
				pygame.mixer.music.load(song)
				pygame.mixer.music.play()
				song_box.selection_clear(0,END)
				song_box.activate(back_song)
				song_box.selection_set(back_song)

		except:
			status_bar['text']='no previous song'

# define the forward function to play the next song
def forward_song():
	if (root.song_added == False):
		messagebox.showinfo('Hint', 'First add some music')
		status_bar['text'] = 'First add some music'
	else:
		try:
			if song_box:
				forward_song=song_box.curselection()
				forward_song=forward_song[0]+1
				song=song_box.get(forward_song)
				song=f"M:/Music/{song}.mp3"
				pygame.mixer.music.load(song)
				pygame.mixer.music.play()
				song_box.selection_clear(0,END)
				song_box.activate(forward_song)
				song_box.selection_set(forward_song)
		except:
			forward_song=song_box.selection_set(0)
			forward_song = song_box.curselection()
			forward_song = forward_song[0]
			song = song_box.get(forward_song)
			song = f"M:/Music/{song}.mp3"
			pygame.mixer.music.load(song)
			pygame.mixer.music.play()
			song_box.selection_clear(0, END)
			song_box.activate(forward_song)
			song_box.selection_set(forward_song)


def set_vol(val):
	volume = float(val) / 100
	pygame.mixer.music.set_volume(volume)  # set_value takes value from 0 to 1
	

# make the volume
scale=ttk.Scale(root,from_=0,to=5,orient=VERTICAL,command=set_vol,length=100)
scale.set(70)
pygame.mixer.music.set_volume(0.7)
scale.place(x=450,y=0)



def about():
	messagebox.showinfo('Created by','Mirwais Jafari\n'
								'Rohullah Sarabi\n'
								'Yaser Saei\n'
								'Amanullah Ruzi\n'
								'Qurban Motahari\n'
								'version 1.3')
def fullscreen():
	root.attributes('-fullscreen',True)

def Minimize():
	root.attributes('-fullscreen',False)
	root.geometry("470x310")

def help():
	webbrowser.open('https://telegram.me//Mirwais jafari')

def contact():
	webbrowser.open("https://facebook.com//Mir Wais")

# make the theme menus
def theme1():
	song_box.config(bg='cyan',fg='white',selectbackground='pink',selectforeground='yellow')
	play_button.config(bg='cyan',activebackground='pink',activeforeground='yellow')
	back_button.config(bg = 'cyan', activebackground = 'pink', activeforeground = 'yellow')
	stop_button.config(bg='cyan', activebackground='pink', activeforeground='yellow')
	pause_button.config(bg='cyan', activebackground='pink', activeforeground='yellow')
	forward_button.config(bg='cyan', activebackground='pink', activeforeground='yellow')
	status_bar.config(bg='cyan',)

def theme2():
	song_box.config(bg='white',fg='red',selectbackground='steel blue',selectforeground='light gray')
	play_button.config(bg='white',activebackground='steel blue',activeforeground='light gray')
	back_button.config(bg = 'white', activebackground = 'steel blue', activeforeground = 'light gray')
	stop_button.config(bg='white', activebackground='steel blue', activeforeground='light gray')
	pause_button.config(bg='white', activebackground='steel blue', activeforeground='light gray')
	forward_button.config(bg='white', activebackground='steel blue', activeforeground='light gray')
	status_bar.config(bg='white')
def theme3():
	song_box.config(bg='navy',fg='azure',selectbackground='snow',selectforeground='green')
	play_button.config(bg='navy',activebackground='black',activeforeground='green')
	back_button.config(bg = 'navy', activebackground = 'black', activeforeground = 'green')
	stop_button.config (bg = 'navy', activebackground = 'black', activeforeground = 'green')
	pause_button.config(bg='navy',activebackground='black',activeforeground='green')
	forward_button.config(bg='navy',activebackground='black',activeforeground='green')
	status_bar.config(bg='navy')
def theme4():
	song_box.config(bg='coral', fg='azure', selectbackground='snow', selectforeground='green')
	play_button.config(bg='coral', activebackground='black', activeforeground='green')
	back_button.config(bg='coral', activebackground='black', activeforeground='green')
	stop_button.config(bg='coral', activebackground='black', activeforeground='green')
	pause_button.config(bg='coral', activebackground='black', activeforeground='green')
	forward_button.config(bg='coral', activebackground='black', activeforeground='green')
	status_bar.config(bg='coral')
def theme5():
	song_box.config(bg='khaki', fg='azure', selectbackground='snow', selectforeground='green')
	play_button.config(bg='khaki', activebackground='black', activeforeground='green')
	back_button.config(bg='khaki', activebackground='black', activeforeground='green')
	stop_button.config(bg='khaki', activebackground='black', activeforeground='green')
	pause_button.config(bg='khaki', activebackground='black', activeforeground='green')
	forward_button.config(bg='khaki', activebackground='black', activeforeground='green')
	status_bar.config(bg='khaki')

# make button
back_button=Button(root,text='back',borderwidth=5,bg='gray',activebackground='green'
				   ,activeforeground='yellow',command=back)
back_button.place(x=50,y=255)


play_button=Button(root,text='play',borderwidth=5,bg='green',activebackground='green'
				   ,activeforeground='yellow',command=play)
play_button.place(x=150,y=255)

stop_button=Button(root,text='Stop',borderwidth=5,bg='red',activebackground='green'
				   ,activeforeground='yellow',command=stop)
stop_button.place(x=100,y=255)

pause_button=Button(root,text='Pause',borderwidth=5,bg='red',activebackground='green'
					,activeforeground='yellow',command=lambda:pause(paused))
pause_button.place(x=200,y=255)

forward_button=Button(text='forward',borderwidth=5,bg='gray',activebackground='green'
					  ,activeforeground='yellow',command=forward_song)
forward_button.place(x=260,y=255)

# make menu
menu_bar=Menu(root)
root.config(menu=menu_bar)

# add menu song
add_song_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Add Song to playlist',menu=add_song_menu)
add_song_menu.add_command(label='Add one song',command=add_one_song)
add_song_menu.add_command(label='Add many songs',command=add_songs)

# add remove song
remove_menu_song=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Remove songs from playlist',menu=remove_menu_song)
remove_menu_song.add_command(label="Remove one song",command=remove_song)
remove_menu_song.add_command(label="Remove all songs",command=remove_songs)

# setting menu
setting=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Setting',menu=setting)
setting.add_command(label='Fullscreen',command=fullscreen)
setting.add_command(label='Minimize',command=Minimize)

# define the theme menu inside the setting menu
theme=Menu(setting,tearoff=0)
setting.add_cascade(label='theme',menu=theme)
theme.add_command(label='theme1',command=theme1)
theme.add_command(label='theme2',command=theme2)
theme.add_command(label='theme3',command=theme3)
theme.add_command(label='theme4',command=theme4)
theme.add_command(label='theme5',command=theme5)
setting.add_command(label='About',command=about)
setting.add_command(label='Help',command=help)
setting.add_command(label='Contact',command=contact)

# add exit menu and about menu
exit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_command(label='Exit',command=root.destroy)

scrol_y=Scrollbar(root,orient=VERTICAL,bg='silver',bd=5,relief=GROOVE,width=20)
scrol_y.place(x=450,y=105)


song_box = Listbox(root,bg='aquamarine',fg='green',width=70,height=13,selectbackground='blue',
selectforeground ='yellow',bd=8,relief=GROOVE,yscrollcommmand=scrol_y.set(0,0),selectmode=SINGLE)
song_box.grid(row=0,column=0,padx=10)
scrol_y.config(command=song_box.yview)

# make status bar
status_bar = Label(root, text='Welcome to music player',relief=GROOVE, anchor=W,width=60,bg='aquamarine',bd=8)
status_bar.place(x=10,y=220)

root.mainloop()