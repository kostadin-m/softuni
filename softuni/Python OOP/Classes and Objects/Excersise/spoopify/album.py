from .song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.published = False
        self.songs = [x for x in args]

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.contains_song(song.name):
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        if not self.contains_song(song):
            return "Song is not in the album."

        for x in self.songs:
            if x.name == song:
                self.songs.remove(x)
                return f"Removed song {song} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f'Album {self.name}\n' + ''.join([f'== {x.get_info()}\n' for x in self.songs])

    def contains_song(self, song: str):
        for x in self.songs:
            if x.name == song:
                return True
        return False
