ontology_path = '../ontology/music.ttl'

with open(ontology_path, encoding='utf-8') as f:
    text = f.read()

text = text.replace('@it', '@ita')

with open(ontology_path, 'w', encoding='utf-8') as f:
    f.write(text)
