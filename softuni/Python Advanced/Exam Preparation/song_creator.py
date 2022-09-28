def add_songs(*args):
    songs = {}
    for title, lyrics in args:
        if title in songs and lyrics:
            songs[title] += "\n".join([str(x) for x in lyrics]) + '\n'
        elif title not in songs and lyrics:
            songs[title] = "\n".join([str(x) for x in lyrics]) + '\n'
        elif title not in songs and not lyrics:
            songs[title] = ''

    result = ''
    for name, lyrics in songs.items():
        result += f'- {name}' + '\n'
        result += lyrics
    return result

