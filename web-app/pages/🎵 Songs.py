import streamlit as st

from init import *

songs_query = onto_prefix + queries['songs']

st.title('Songs 🎵')
result = g.query(songs_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
