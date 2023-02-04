from init import *


def filtered_query(certification):
    filtered_albums_query = onto_prefix + queries['list_filter']['albums']
    filter = f"REGEX(?Certification, '^{certification if certification else '[A-Z]'}*', 'i')"
    return filtered_albums_query.format(filter)


st.markdown(hide_st_style, unsafe_allow_html=True)
category_filters = ['Album', 'Owner']
certification_filters = ['', 'Gold Certification', 'Platinum Certification', 'Diamond Certification']
st.title('Albums 💿')

certification = st.selectbox('Certification', certification_filters)
col1, col2 = st.columns(2)
with col1:
    search = st.text_input('To search', placeholder='Talking Book').lower()
with col2:
    filter = st.selectbox('Category', category_filters)

result = g.query(filtered_query(certification))
df = pd.DataFrame(result, columns=result.vars)

if search:
    df = df[df.iloc[:, filters.index(filter)].str.lower().str.contains(search)]

st.dataframe(beautify_df(df), use_container_width=True)
