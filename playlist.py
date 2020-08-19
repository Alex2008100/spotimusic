import random

class Playlist:
    id = 0

    def __init__(self, title, songs):
        #Title is str
        self.title = title
        #Songs is list
        self.songs = songs
        self.id = Playlist.get_id()

    def __str__(self):
        return '{} {} {}'.format(self.id, self.title, self.songs)

    @staticmethod
    def get_id():
        Playlist.id += 1
        return Playlist.id


    def shuffle(self):
        for i in range(len(self.songs)-1, 0, -1):
            j = random.randint(0, i)
            self.songs[j], self.songs[i] = self.songs[i], self.songs[j]

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_id):
        for id in range(len(self.songs)-1):
            if self.songs[id].id is song_id:
                self.songs.remove(self.songs[id])


    def song_by_id(self, song_id):
        for id in range(len(self.songs)-1):
            if self.songs[id].id is song_id:
                return self.songs[id]

    def songs_by_id(self):
        return [song.id for song in self.songs]
