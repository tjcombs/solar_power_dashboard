# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 08:40:14 2020

@author: tjcombs

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from data import get_generation_data, get_weather_data

generation = get_generation_data()
weather = get_weather_data()

panel = generation[generation['SOURCE_KEY']=='vOuJvMaM2sgwLmb']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.line(data_frame = panel, x='DATE_TIME', y='AC_POWER', title = 'AC Power from Panel')

app.layout = html.Div(children=[
    html.H1(children='Solar Power Generation'),

    html.Div(children='''
        Built with Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)