with open('../music.owl', encoding='utf-8') as f:
    text = f.read()

text = text.replace('@ita', '@it')
print(text)
with open('../music.owl', 'w', encoding='utf-8') as f:
    f.write(text)
