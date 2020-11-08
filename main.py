# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 08:40:14 2020

@author: tjcombs

"""

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from data import get_generation_data, get_weather_data

generation = get_generation_data()
generation = generation[('2020-05-15' <= generation['DATE_TIME']) & (generation['DATE_TIME'] <= '2020-06-17')]
weather = get_weather_data()

panel = generation[generation['SOURCE_KEY']=='vOuJvMaM2sgwLmb']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

generation_agg = generation.groupby(by=['PLANT_ID', 'DATE_TIME']).agg(MEAN_AC_POWER=('AC_POWER', 'mean')).reset_index(drop=False)
generation_agg = pd.merge(left=generation_agg, right=weather, on=['DATE_TIME', 'PLANT_ID'])


fig1 = px.line(data_frame = generation_agg, 
              x='DATE_TIME', 
              y='MEAN_AC_POWER', 
              line_group = 'PLANT_ID',
              color = 'PLANT_ID',
              title = 'Mean AC Power from Panels by Plant',
              height = 500)

app.layout = html.Div(children=[
    html.H1(children='Solar Power Generation'),

    html.Div(children='''
        Built with Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='ac_power',
        figure=fig1
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
