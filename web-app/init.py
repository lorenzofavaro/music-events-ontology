import json

import pandas as pd
from pandas.io.formats.style import Styler
from rdflib import Graph

hide_st_style = '<style>#MainMenu{visibility:hidden;}footer{visibility:hidden;}header{visibility:hidden;}</style>'
core_prefix = 'http://www.semanticweb.org/lorenzo/ontologies/music#'
onto_prefix = f'PREFIX musica: <{core_prefix}>'
g = Graph().parse('res/music-inferred.rdf')
with open('res/queries.json') as f:
    queries = json.load(f)


def beautify_df(df: pd.DataFrame) -> Styler:
    df = df.replace(to_replace=core_prefix, value='', regex=True)
    df.columns = [col.replace('_', ' ') for col in df.columns]
    return df.style.highlight_null(props="color: transparent;")
