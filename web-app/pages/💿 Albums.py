import streamlit as st

from init import *

albums_query = onto_prefix + queries['list']['albums']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Albums 💿')
result = g.query(albums_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)
