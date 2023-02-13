from init import *

song_genres_query = onto_prefix + queries['list']['song_genres']
event_genres_query = onto_prefix + queries['list']['event_genres']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Music Genres 🎨')

st.subheader('Event Count for Genre')
result = g.query(event_genres_query)
df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)

st.subheader('Song Count for Genre')
result = g.query(song_genres_query)
df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)
