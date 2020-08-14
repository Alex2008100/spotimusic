#Libs
from tkinter import filedialog
from tkinter import *
import random
import pygame

#Class for work with songs
class Song:
    #Song controls
    def back():
        Song.select_song(-1)

    def play():
        #If the music wasn't playing
        if play_btn['text'] == 'Play':
            song = song_list.get(ACTIVE)
            song = '/home/alex/Project/spotimusic/songs/{}.mp3'.format(song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 0)
            play_btn['text'] = 'Stop'
            print('Play ' + song)
        #If the music was playing
        else:
            pygame.mixer.music.stop()
            play_btn['text'] = 'Play'
        #Reset pause button if it was paused
        pause_btn['text'] = 'Pause'

    def pause():
        #If unpaused
        if pause_btn['text'] == 'Pause':
            pygame.mixer.music.pause()
            pause_btn['text'] = 'Unpause'
        #If paused
        else:
            pygame.mixer.music.unpause()
            pause_btn['text'] = 'Pause'

    def forward():
        Song.select_song(1)

    def select_song(step):
        #Find next
        next = song_list.curselection()
        next = next[0] + step
        #Choose song and start playing
        song = song_list.get(next)
        if song is not None:
            song = 'songs/{}.mp3'.format(song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 0)
            play_btn['text'] = 'Stop'

            #Select next in song_list
            song_list.selection_clear(0, END)
            song_list.activate(next)
            song_list.selection_set(next, last = None)

    #Playlists controls
    #Selects playlist if exists,
    #or creates new one and saves it
    def select_playlist(title):
        #Save active playlist
        global active_playlist, playlists
        playlists[active_playlist['name']] = active_playlist
        if title in playlists:
            #Select
            active_playlist = playlists[title]
        else:
            #Create and save
            new_playlist = {'songs' : [], 'name': title}
            active_playlist = new_playlist
            playlists[title] = new_playlist
            #Add to menu
            add_playlist_menu.add_command(label = title, command = lambda:Song.select_playlist(title))

        update_list()

    def shuffle():
        for i in range(len(active_playlist['songs'])-1, 0, -1):
            j = random.randint(0, i)
            active_playlist['songs'][j], active_playlist['songs'][i] = active_playlist['songs'][i], active_playlist['songs'][j]
        print('Shuffled playlist ' + active_playlist['name'])
        update_list()

#Class for menu functions
class Menu_f:
    def add_song():
        song = filedialog.askopenfilename(
            initialdir = 'songs/',
            title = 'Choose a song',
            filetypes = (('mp3 files', '*.mp3'),) )
        #Clean up the name for list
        song = song.replace('/home/alex/Project/spotimusic/songs/', '')
        song = song.replace('.mp3', '')
        #Add to playlist
        active_playlist['songs'].append(song)

        #Update and debug
        update_list()
        print('Song added to ' + active_playlist['name'])
        print(active_playlist)

    def add_songs():
        pass

    def add_playlist():
        #Make a pop up window
        pop_up = Tk()
        pop_up.title('')
        pop_up.geometry('200x300')
        #Entry for playlist name
        submit_entry = Entry(pop_up)
        #Button to submit
        submit_btn = Button(pop_up, text = 'Submit playlist name', command = lambda: Song.select_playlist(submit_entry.get()))

        #Pack
        submit_entry.pack()
        submit_btn.pack()

#Update list
def update_list():
    song_list.delete(0, END)
    song_list.insert(END, active_playlist['name'])
    for song in active_playlist['songs']:
        song_list.insert(END, song)
    print('Listbox updated for playlist ' + active_playlist['name'])
    print(active_playlist)

#Init

window = Tk()
window.title('Mp3 player')
window.geometry("300x500")

pygame.mixer.init()

playlists = {}
playlists['base'] = {'songs' : [], 'name': 'base'}

active_playlist = playlists['base']
#List init
song_list = Listbox(window,
    bg = 'grey', fg = 'white',
    selectbackground = 'white', selectforeground = 'black',
    width = 50, height = 33)
song_list.pack()
update_list()

#Controls init
controls_frame = Frame(window)
controls_frame.pack()

back_btn = Button(controls_frame,text = 'Back' , command = Song.back)
play_btn = Button(controls_frame,text = 'Start' , command = Song.play)
pause_btn = Button(controls_frame,text = 'Pause' , command = Song.pause)
frwd_btn = Button(controls_frame,text = 'Forward' , command = Song.forward)

back_btn.grid(row = 0, column = 0)
play_btn.grid(row = 0, column = 1)
pause_btn.grid(row = 0, column = 2)
frwd_btn.grid(row = 0, column = 3)

#Menu Init
menu = Menu(window)
window.config(menu = menu)

add_song_menu = Menu(menu)
menu.add_cascade(label = 'Add Song', menu = add_song_menu)
add_song_menu.add_command(label = 'Add song to active playlist', command = Menu_f.add_song)

add_playlist_menu = Menu(menu)
menu.add_cascade(label = 'Playlist', menu = add_playlist_menu)
add_playlist_menu.add_command(label = 'New playlist', command = Menu_f.add_playlist)
add_playlist_menu.add_command(label = 'Shuffle', command = Song.shuffle)
add_playlist_menu.add_command(label = 'base', command = lambda:Song.select_playlist('base'))
#Mainloop
window.mainloop()
