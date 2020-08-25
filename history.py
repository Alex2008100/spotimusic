import song

#Counter class
#Counts how many times each song parameter is played
#Can be used to make favourites and recommendations
class History:

    def __init__(self):
        self.counter = History.Counter()

    class Counter:

        def __init__(self):
            self.artist = {}
            self.genre = {}
            self.bpm = {}
            self.age = {}

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

            print(self.__dict__)

            [func(param) for func, param in zip(funcs, params)]
