import streamlit as st

from init import *

# Events List
events_query = onto_prefix + queries['list']['events']

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Events 🎫')
result = g.query(events_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)
st.markdown('''---''')

# Event Details
st.subheader('Display event details')
event_label = st.selectbox("Select event", [row[0] for row in result])

event_details_query = onto_prefix + queries['single']['event'].format(event_label)
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

performed_songs_query = onto_prefix + queries['single']['event_songs'].format(event_label)
result = g.query(performed_songs_query)

df = beautify_df(pd.DataFrame(result, columns=result.vars))
st.dataframe(df, use_container_width=True)
