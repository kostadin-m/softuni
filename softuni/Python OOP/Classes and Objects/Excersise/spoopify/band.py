from .album import Album


class Band:
    def __init__(self, name: str, ):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        album_existing = self.contains_album(album.name)
        if album_existing:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album: str):
        album_in_albums = self.contains_album(album)
        if not album_in_albums:
            return f"Album {album} is not found."
        if album_in_albums.published:
            return f'Album has been published. It cannot be removed.'

        self.albums.remove(album_in_albums)
        return f'Album {album} has been removed.'

    def details(self):
        return f"Band {self.name}\n" + '\n'.join([x.details() for x in self.albums])

    def contains_album(self, album: str):
        for x in self.albums:
            if x.name == album:
                return x
        return False
