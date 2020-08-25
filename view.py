from tkinter import filedialog
from tkinter import *
from song import Song
from playlist import Playlist
from history import History
import pygame

class Player:

    #Parameters
    def set_parameters(self):
        self.active_playlist = Playlist('base', [])
        self.playlists = {'base': self.active_playlist}
        self.history = History()

    #Functions

    #Play or stop toggle function
    def toggle_song(self, title):
        #If wasn't playing
        if self.play_btn['text'] != 'Stop':
            #Find
            for iter in range(len(self.active_playlist.songs)):
                print(self.active_playlist.songs[iter].title + ' ' + title)
                if self.active_playlist.songs[iter].title == title:
                    #And play
                    pygame.mixer.music.load(self.active_playlist.songs[iter].dir)
                    pygame.mixer.music.play(loops = 0)

                    self.history.counter.add_all(self.active_playlist.songs[iter])

                    print(self.active_playlist.sort_by(self.history ,'artist'))
                    self.favourites('artist')

                    self.play_btn['text'] = 'Stop'

        #If was playing
        else:
            #Stop
            pygame.mixer.music.stop()
            self.play_btn['text'] = 'Play'
            #Reset pause button
            self.pause_btn['text'] = 'Pause'

    #Pause or unpause toggle function
    def pause_song(self):
        #If unpaused
        if self.pause_btn['text'] == 'Pause':
            pygame.mixer.music.pause()
            self.pause_btn['text'] = 'Unpause'
        #If paused
        else:
            pygame.mixer.music.unpause()
            self.pause_btn['text'] = 'Pause'

    #Update song list box
    def update_list(self):
        self.song_list.delete(0, END)
        for song in self.active_playlist.songs:
            self.song_list.insert(END, song.title)


    def favourites(self, parameter):
        list = self.active_playlist.sort_by(self.history, parameter)
        for song in self.active_playlist.songs:
            if song.artist == list[0]:
                print(song)

    #Menu functions

    #Add song
    def add_song(self):
        #Get directory
        song_dir = filedialog.askopenfilename(
            initialdir = 'songs/',
            title = 'Choose a song',
            filetypes = (('mp3 files', '*.mp3'),) )
        #Clean up the name for list
        title = song_dir
        title = title.replace('/home/alex/Project/spotimusic/songs/', '')
        title = title.replace('.mp3', '')

        #Pop up window for parameters
        pop_up = Tk()
        pop_up.title('Set parameters')
        pop_up.geometry('500x300')
        artist_entry = Entry(pop_up)
        bpm_entry = Entry(pop_up)
        genre_entry = Entry(pop_up)
        age_entry = Entry(pop_up)
        artist_entry.pack()
        bpm_entry.pack()
        genre_entry.pack()
        age_entry.pack()

        #Submit and add to playlist
        def submit(title, artist, genre, dir, bpm, age):
            print(title)
            song = Song(title, artist, genre, dir, bpm, age)
            self.active_playlist.add_song(song)

            self.update_list()

        submit_btn = Button(
            pop_up,
            text = 'Submit song',
            command = lambda: submit(
                title,
                artist_entry.get(),
                genre_entry.get(),
                song_dir,
                bpm_entry.get(),
                age_entry.get()
                )
            )

        submit_btn.pack()

    #Add playlists
    def add_playlist(self):
        #Pop up window for title
        pop_up = Tk()
        pop_up.title('Set parameters')
        pop_up.geometry('500x300')
        title_entry = Entry(pop_up)
        title_entry.pack()

        #Submit, add to dict and menu
        def submit(title):
            self.playlists[title] = Playlist(title, [])
            self.active_playlist = self.playlists[title]
            #Add to menu
            self.add_playlist_menu.add_command(label = title, command = lambda: self.select_playlist(title))

            self.update_list()

        submit_btn = Button(
            pop_up,
            text = 'Submit playlist',
            command = lambda: submit(title_entry.get())
        )

        submit_btn.pack()

    #Select playlists
    def select_playlist(self, title):
        if title in self.playlists:
            self.active_playlist = self.playlists[title]
            self.update_list()
        else:
            self.add_playlist()

    #Shuffle
    def shuffle(self):
        self.active_playlist.shuffle()
        self.update_list()

    #UI init func, runs the programm
    def build_ui(self):
        #UI

        self.set_parameters()

        self.window = Tk()
        self.window.title('Mp3 player')
        self.window.geometry("300x500")

        pygame.mixer.init()

        #List init
        self.song_list = Listbox(self.window,
            bg = 'grey', fg = 'white',
            selectbackground = 'white', selectforeground = 'black',
            width = 50, height = 33)
        self.song_list.pack()

        #Controls init
        self.controls_frame = Frame(self.window)
        self.controls_frame.pack()

        self.prev_btn = Button(self.controls_frame,text = 'Previous')
        self.play_btn = Button(self.controls_frame,text = 'Play' , command = lambda: self.toggle_song(self.song_list.get(ACTIVE)))
        self.pause_btn = Button(self.controls_frame,text = 'Pause' , command = lambda: self.pause_song())
        self.next_btn = Button(self.controls_frame,text = 'Forward' )

        self.prev_btn.grid(row = 0, column = 0)
        self.play_btn.grid(row = 0, column = 1)
        self.pause_btn.grid(row = 0, column = 2)
        self.next_btn.grid(row = 0, column = 3)

        #Menu Init
        self.menu = Menu(self.window)
        self.window.config(menu = self.menu)

        self.add_song_menu = Menu(self.menu)
        self.menu.add_cascade(label = 'Add Song', menu = self.add_song_menu)
        self.add_song_menu.add_command(label = 'Add song to active playlist', command = lambda: self.add_song())

        self.add_playlist_menu = Menu(self.menu)
        self.menu.add_cascade(label = 'Playlist', menu = self.add_playlist_menu)
        self.add_playlist_menu.add_command(label = 'New playlist', command = lambda: self.add_playlist())
        self.add_playlist_menu.add_command(label = 'Shuffle', command = lambda: self.shuffle())
        self.add_playlist_menu.add_command(label = 'base', command = lambda: self.select_playlist('base'))
        #Mainloop
        self.window.mainloop()

player = Player()
player.build_ui()
