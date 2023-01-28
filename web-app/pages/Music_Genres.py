import pandas as pd
import streamlit as st
from init import *

st.title('Music Genres')
music_genres = list(default_world.sparql('''PREFIX musica: <http://www.semanticweb.org/lorenzo/ontologies/music#>
                                    SELECT ?genere WHERE { ?genere a musica:GenereMusicale }'''))
df = pd.DataFrame([s.name for m in music_genres for s in m], columns=['Music Genres'])
st.write(df)
