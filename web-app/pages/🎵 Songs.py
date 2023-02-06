from init import *


def filtered_query(genre):
    filtered_songs_query = onto_prefix + queries['list_filter']['songs']
    filter = f"REGEX(?Genre, '^{genre if genre else '[A-Z]'}*', 'i')"
    return filtered_songs_query.format(filter)


st.markdown(hide_st_style, unsafe_allow_html=True)
category_filters = ['Song', 'Album', 'Composer']
genre_filters = ['', 'Pop', 'Rock', 'Folk', 'Jazz']
st.title('Songs 🎵')

genre = st.selectbox('Genre', genre_filters)
col1, col2 = st.columns(2)
with col1:
    search = st.text_input('To search', placeholder='Hey Jude').lower()
with col2:
    category = st.selectbox('Category', category_filters)

result = g.query(filtered_query(genre))
df = pd.DataFrame(result, columns=result.vars)

if search:
    df.dropna(inplace=True)
    df = df[df.iloc[:, category_filters.index(category)].str.lower().str.contains(search, na=False)]

st.dataframe(beautify_df(df), use_container_width=True)
