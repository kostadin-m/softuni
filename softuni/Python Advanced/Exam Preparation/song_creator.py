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


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))