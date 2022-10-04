from .album import Album

class Band:
    def __init__(self, name: str, ):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album: str):
        for x in self.albums:
            if x.name == album:
                if x.published:
                    return f'Album has been published. It cannot be removed.'

                self.albums.remove(x)
                return f'Album {album} has been removed.'
        return f"Album {album} is not found."

    def details(self):
        return f"Band {self.name}\n" + '\n'.join([x.details() for x in self.albums])