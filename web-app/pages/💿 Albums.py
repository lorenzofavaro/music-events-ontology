import streamlit as st

from init import *

albums_query = onto_prefix + queries['albums']

st.title('Albums 💿')
result = g.query(albums_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
