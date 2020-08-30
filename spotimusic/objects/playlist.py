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

    #Shuffle list of songs
    def shuffle(self):
        for i in range(len(self.songs)-1, 0, -1):
            j = random.randint(0, i)
            self.songs[j], self.songs[i] = self.songs[i], self.songs[j]

    #Add songs
    def add_song(self, song):
        self.songs.append(song)

    #Remove song by id
    def remove_song(self, song_id):
        for id in range(len(self.songs)-1):
            if self.songs[id].id is song_id:
                self.songs.remove(self.songs[id])

    #Return song based on id given
    def song_by_id(self, song_id):
        for id in range(len(self.songs)-1):
            if self.songs[id].id is song_id:
                return self.songs[id]

    #Returns dict with songs
    #Title is key, id is value
    def songs_by_id(self):
        songs = {}
        for song in self.songs:
            el = {song.title:song.id}
            songs = {**songs, **el}

        return songs

    #Recommends songs based on 5 best parameters
    def recommend(self, max_dict, parameter):
        songs = []
        for song in self.songs:
            params = {'artist': song.artist, 'genre': song.genre, 'bpm': song.bpm, 'age': song.age}
            param = params[parameter]
            max_par = max_dict[parameter]
            for key in sorted(max_par.keys(), reverse = True)[:5]:
                if param in max_par[key]:
                    songs.append(song)

        return songs

    #Sorting by some parameter (Not working!)
    def sort_by(self, history ,parameter):
        param = {'artist':history.counter.artist, 'genre':history.counter.genre, 'bpm':history.counter.bpm, 'age':history.counter.age}
        dict = param[parameter]

        list = []

        for iter in range(len(dict)):
            max = 0
            max_key = ''
            keys = dict.keys()
            values = dict.values()
            for key, value in dict.items():
                if max < value:
                    max = value
                    max_key = key

            list.append(max_key)
        return list
