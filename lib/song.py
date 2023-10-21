class Song:
    count = 0 
    genres = []
    artists = []
    genre_count = dict()
    artist_count = dict()

    def __init__(self,name,artist,genre):
        self.add_song_to_count() 
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.name = name 
        self.artist = artist
        self.genre = genre    

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls,genre):       
        if genre not in cls.genres:
            cls.genres.append(genre)     
            
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count.keys():
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count.keys():
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1