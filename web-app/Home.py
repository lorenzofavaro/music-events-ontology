from init import *

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Music Ontology 🎼')
st.markdown('''---''')
st.write('This musical ontology focuses primarily on the realm of **events**. '
         'It is possible to search and view the events and the relative artists present and songs performed. '
         'It is also possible to filter by event size and also by tags (music genres) associated with it.')
st.write('You can explore it through the side menu or by using the search tool below.')

col1, col2, = st.columns(2)

with col1:
    search = st.text_input('To search', placeholder='Bob Dylan').lower()
with col2:
    category = st.selectbox('Category', ('Musicians', 'Songs', 'Albums', 'Events', 'Labels', 'Genres')).lower()

query = onto_prefix + queries['list'][category]
result = g.query(query)
df = pd.DataFrame(result, columns=result.vars, dtype=str)

if search:
    df = df[df.iloc[:, 0].str.lower().str.contains(search)]

st.dataframe(beautify_df(df), use_container_width=True)
