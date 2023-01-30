import streamlit as st

from init import *

events_query = onto_prefix + queries['free']['events']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Events 🎫')
result = g.query(events_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
