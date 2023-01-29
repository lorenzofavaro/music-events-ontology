import streamlit as st

from init import *

music_genres_query = onto_prefix + queries['genres']

st.title('Music Genres 🎨')
result = g.query(music_genres_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
