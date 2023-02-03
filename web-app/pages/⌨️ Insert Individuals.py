import datetime

from init import *


def add_event(name, start_date, end_date, type, attendance):
    new_event = URIRef(core_prefix + name)
    g.add((new_event, RDF.type, music.Event))
    g.add((new_event, RDFS.label, Literal(name, lang='en')))
    g.add((new_event, RDFS.label, Literal(name, lang='it')))
    g.add((new_event, music.eventType, Literal(type, datatype=XSD.string)))
    g.add((new_event, music.eventStartDate, Literal(start_date, datatype=XSD.date)))
    g.add((new_event, music.eventEndDate, Literal(end_date, datatype=XSD.date)))
    g.add((new_event, music.attendance, Literal(attendance, datatype=XSD.unsignedInt)))
    # g.add((new_event, music.locatedIn, URIRef(core_prefix + location)))
    g.serialize(destination=ontology_path, format='xml')


st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Insert Individuals ⌨️')
st.markdown('''---''')

st.header('New Event')
st.subheader('Data properties')
event_name = st.text_input('Name')

col1, col2 = st.columns(2)
with col1:
    event_start_date = st.date_input('Start Date', min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
    event_type = st.selectbox('Type', ('Festival', 'Concert'))
with col2:
    event_end_date = st.date_input('End Date', min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
    event_attendance = st.text_input('Attendance')

# st.subheader('Object properties')
# col1, col2 = st.columns(2)
# with col1:
# with col2:
st.button('Commit', on_click=lambda: add_event(event_name, event_start_date, event_end_date, event_type, event_attendance))
