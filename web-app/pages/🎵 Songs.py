import streamlit as st

from init import *

songs_query = onto_prefix + queries['free']['songs']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Songs 🎵')
result = g.query(songs_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
