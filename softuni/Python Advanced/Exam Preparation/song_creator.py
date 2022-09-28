def add_songs(*args):
    songs = {}
    for title, lyrics in args:
        songs[title] = songs.get(title, []) + lyrics
    result = ''
    for name, lyrics in songs.items():
        result += f'- {name}' + '\n' + '\n'.join(lyrics)
        if lyrics:
            result += '\n'
    return result
