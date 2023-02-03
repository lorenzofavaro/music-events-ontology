from init import *

albums_query = onto_prefix + queries['list']['albums']
filters = ['Album', 'Owner']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Albums 💿')
result = g.query(albums_query)

col1, col2 = st.columns(2)

with col1:
    search = st.text_input('To search', placeholder='Talking Book').lower()
with col2:
    filter = st.selectbox('Filter', filters)
df = pd.DataFrame(result, columns=result.vars)

if search:
    df = df[df.iloc[:, filters.index(filter)].str.lower().str.contains(search)]

st.dataframe(beautify_df(df), use_container_width=True)

