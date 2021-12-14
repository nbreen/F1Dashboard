import dash

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from data import *
from callbacks import *

app.layout = html.Div(id='root', children=[
    dcc.Dropdown(id='race-select', 
                 options=[{'label': '{}'.format(weekend.name), 
                           'value': index} for index, weekend in 
                            enumerate(raceWeekends)
                         ]
                 ,value=21
                ),
    html.H1(id='race-name'),
    html.H2(id='race-date'),
    html.Div(id='race-results',
             children=[]),
    dcc.Graph(id='track-temp')
])


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=True)