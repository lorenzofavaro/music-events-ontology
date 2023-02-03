import json
import re
import streamlit as st

import pandas as pd
from pandas.io.formats.style import Styler
from rdflib import Graph, Namespace, Literal, URIRef, RDF, RDFS, XSD

hide_st_style = '<style>#MainMenu{visibility:hidden;}footer{visibility:hidden;}header{visibility:hidden;}</style>'
ontology_path = 'res/music-inferred.rdf'
g = Graph().parse(ontology_path)
with open('res/queries.json') as f:
    queries = json.load(f)

onto_prefix = queries['prefix']
core_prefix = re.findall(r'<(.*?)>', onto_prefix)[0]
music = Namespace(core_prefix)


def beautify_df(df: pd.DataFrame) -> Styler:
    df = df.replace(to_replace=core_prefix, value='', regex=True)
    df.columns = [col.replace('_', ' ') for col in df.columns]
    return df.style.highlight_null(props="color: transparent;")
