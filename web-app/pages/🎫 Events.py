import streamlit as st

from init import *

events_query = onto_prefix + queries['events']

st.title('Events 🎫')
result = g.query(events_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
