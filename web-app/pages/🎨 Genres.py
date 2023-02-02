import streamlit as st

from init import *

music_genres_query = onto_prefix + queries['list']['genres']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Music Genres 🎨')
result = g.query(music_genres_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)
