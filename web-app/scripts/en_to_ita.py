ontology_path = '../res/music.rdf'

with open(ontology_path, encoding='utf-8') as f:
    text = f.read()

text = text.replace('xml:lang="ita"', 'xml:lang="it"')

with open(ontology_path, 'w', encoding='utf-8') as f:
    f.write(text)
