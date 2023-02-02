import streamlit as st

from init import *


def filtered_query(dimension, tag):
    events_tag_filtered_query = onto_prefix + queries['list_filter']['events']
    filter = f"REGEX(?TagLabel, '^{tag if tag else '[A-Z]'}*', 'i') && REGEX(?SubClassLabel, '^{dimension if dimension else '[A-Z]'}*', 'i')"
    return events_tag_filtered_query.format(filter)


# Events List
genres_query = onto_prefix + queries['list']['genres']
single_event_query = onto_prefix + queries['single']['event']
single_event_songs_query = onto_prefix + queries['single']['event_songs']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Events 🎫')
result = g.query(genres_query)

col1, col2 = st.columns(2)
with col1:
    dimension_filter = st.selectbox('Dimensions', ['', 'Small', 'Medium', 'Big'])
with col2:
    tag_filter = st.selectbox('Tags', [''] + [row[0].replace(core_prefix, '') for row in result])
result = g.query(filtered_query(dimension_filter, tag_filter))

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)
st.markdown('''---''')

# Event Details
st.subheader('Display event details')
event_label = st.selectbox("Select event", [row[0] for row in result])

if event_label:
    event_details_query = single_event_query.format(event_label)
    result = g.query(event_details_query)
    df = pd.DataFrame(result, columns=result.vars)
    df = df.replace(to_replace=core_prefix, value='', regex=True)
    event_name, start_date, end_date, attendance, event_type, manifest, tags = df.iloc[0].tolist()

    col1, col2 = st.columns(2)

    with col1:
        st.image(manifest, width=300)

    with col2:
        st.write(f'**Event name**: {event_name}')
        st.write(f'**Start date**: {start_date}')
        st.write(f'**End date**: {end_date}')
        st.write(f'**Attendance**: {attendance}')
        st.write(f'**Event Type**: {event_type}')
        st.write(f'**Tags**: {tags}')

    performed_songs_query = single_event_songs_query.format(event_label)
    result = g.query(performed_songs_query)

    df = beautify_df(pd.DataFrame(result, columns=result.vars))
    st.dataframe(df, use_container_width=True)
