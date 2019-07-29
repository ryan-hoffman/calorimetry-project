# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------
import sys
sys.path.append("..")
from temperatureConverter import *
#----------------------------------------------------------------------------------------------------
import dash
import dash_core_components as dcc
import dash_html_components as html
#----------------------------------------------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
converter = TemperatureConverter(fahrenheit=70, centigrade=30)

fahrenheitInput = dcc.Input(
    id="fahrenheitInput",
    placeholder='Enter a value...',
    type='number',
    value=32,
    debounce=True
    )  

centigradeInput = dcc.Input(
    id="centigradeInput",
    placeholder='Enter a value...',
    type='number',
    value=0,
    debounce=True
    )  

app.layout = html.Div([
    html.Span("Fahrenheit "),
    fahrenheitInput,
    html.P(),
    html.Span("Centigrade "),
    centigradeInput,
    ])

if __name__ == '__main__':
   app.run_server(debug=True)
