with open('../music.owl') as f:
    text = f.read()

text.replace('@ita', 'it')