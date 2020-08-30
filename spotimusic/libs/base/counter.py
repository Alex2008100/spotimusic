from .stack import Stack

class Counter:
    #Magic
    def __init__(self, artist = {}, genre = {}, bpm = {}, age = {}):
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.age = age
        self.songs = Stack(False)
    #Counter

    #Add 1 to each counter, or all at the same tiime
    #adds objects if no such in dict
    def add_artist(self, artist):
        if not artist in self.artist:
            self.artist[artist] = 0
        self.artist[artist] += 1

    def add_genre(self, genre):
        if not genre in self.genre:
            self.genre[genre] = 0
        self.genre[genre] += 1

    def add_bpm(self, bpm):
        if not bpm in self.bpm:
            self.bpm[bpm] = 0
        self.bpm[bpm] += 1

    def add_age(self, age):
        if not age in self.age:
            self.age[age] = 0
        self.age[age] += 1

    def add_all(self, song):
        data = song.__dict__

        funcs = [self.add_artist, self.add_genre, self.add_bpm, self.add_age]
        params = [data['artist'], data['genre'], data['bpm'], data['age']]

        [func(param) for func, param in zip(funcs, params)]

    def add_song(self, song):
        if len(self.songs) >= 5:
            print('History: popped ' + str(self.songs.pop()))
        self.songs.push(song)

        print('History: songs ' + str(self.songs))

    def max(self):
        max = {
                'artist': {str(value):key for key, value in self.artist.items()},
                'genre': {str(value):key for key, value in self.genre.items()},
                'bpm': {str(value):key for key, value in self.bpm.items()},
                'age': {str(value):key for key, value in self.age.items()}
                }
        print('Max : ' + str(max))
        #Return max
        return max
