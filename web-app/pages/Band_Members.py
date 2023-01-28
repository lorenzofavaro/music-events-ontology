import pandas as pd
import streamlit as st
from init import *

st.title('Band Members')
band_members = list(default_world.sparql('''PREFIX musica: <http://www.semanticweb.org/lorenzo/ontologies/music#>
                                    SELECT ?band ?membro WHERE { ?band musica:haComponente ?membro } ORDER BY ?band'''))
df = pd.DataFrame([[band.name, member.name] for band, member in band_members], columns=['Band', 'Member'])
st.write(df)
