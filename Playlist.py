class Song:
    def __init__(self, title, artist, genre, duration):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration 
        
def display_songs_by_genre(songs, genre):
    print(f"{genre} Songs:")
    for song in songs:
        if song.genre == genre:
            print(f"Title: {song.title}, Artist: {song.artist}, Duration: {song.duration} seconds")

def main():
    songs = [
        Song("APT", "Rose", "Pop", 210),
        Song("SOS", "SVT", "Dance", 180),
        Song("YES OR NO", "JK", "Pop", 240)
    ]

    current_song = -1

    if current_song == -1:
        print("No song is currently playing.")
    
    current_song = 0
    print(f"Currently Playing: {songs[current_song].title} by {songs[current_song].artist}")
    current_song = 1
    print(f"Currently Playing: {songs[current_song].title} by {songs[current_song].artist}")
    current_song = 0
    print(f"Currently Playing: {songs[current_song].title} by {songs[current_song].artist}")
    print("\n")

    display_songs_by_genre(songs, "Dance")
    print("\n")
    display_songs_by_genre(songs, "Pop")

if __name__ == "__main__":
    main()
