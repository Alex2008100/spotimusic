class Song:
    id = 0

    def __init__(self, title, artist, genre, dir, bpm, age):
        #All str
        self.title = title
        self.artist = artist
        self.genre = genre
        self.dir = dir
        #All int
        self.bpm = bpm
        self.age = age
        self.id = Song.get_id()

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.title, self.artist, self.genre, self.bpm, self.age)

    @staticmethod
    def get_id():
        Song.id += 1
        return Song.id
