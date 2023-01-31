import streamlit as st

from init import *

all_musicians_query = onto_prefix + queries['free']['musicians']
only_bands_query = onto_prefix + queries['free']['musicians_only_bands']
only_solists_query = onto_prefix + queries['free']['musicians_only_solists']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Musicians 🧑‍🎤')
musician_type = st.selectbox('Type', ('All', 'Only Solists', 'Only Band'))

if musician_type == 'All':
    result = g.query(all_musicians_query)
elif musician_type == 'Only Band':
    result = g.query(only_bands_query)
elif musician_type == 'Only Solists':
    result = g.query(only_solists_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)
