import streamlit as st

from init import *

record_company_query = onto_prefix + queries['free']['labels']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Labels 👥')
result = g.query(record_company_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df)
