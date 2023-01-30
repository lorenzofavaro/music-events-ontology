import streamlit as st

from init import *

all_musicians_query = onto_prefix + queries['parametrized']['musicians']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Music Ontology 🎼')
st.markdown("""---""")
st.write('This ontology is about the music domain.')
st.write('You can explore it through the side menu or by using the search tool below.')

col1, col2, = st.columns(2)

with col1:
    search = st.text_input('To search', placeholder='Bob Dylan')
with col2:
    category = st.selectbox('Category', ('Musicians', 'Songs', 'Albums', 'Events', 'Companies', 'Genres'))

if search:
    query = onto_prefix + queries['parametrized'][category.lower()].format(search)
else:
    query = onto_prefix + queries['free'][category.lower()]

result = g.query(query)
df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
