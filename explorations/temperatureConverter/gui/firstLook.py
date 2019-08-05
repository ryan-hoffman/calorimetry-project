# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------
# this small script aspires to capture the basics of plotly/dash (version 1.x) operations, including
#  - updating multiple widgets (two of them)  when a third widget changes
#  - treating an input widget as (also) an output widget
# on the latter point, see:
#   see https://community.plot.ly/t/change-value-of-dcc-input-with-a-callback/18258
#
# this does not yet work.
#
# the three widgets:
#   1) fahrenheitWidget
#   2) centigradeWidget
#   3) calculationaCounterWidget
#
# the desired operation:
#   change either of the temperature values, and the other is updated, and the
#   calculationCounterWidget is incremented
#----------------------------------------------------------------------------------------------------
import sys
sys.path.append("..")
from temperatureConverter import *
#----------------------------------------------------------------------------------------------------
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#----------------------------------------------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
converter = TemperatureConverter(fahrenheit=70, centigrade=30)

fahrenheitWidget = dcc.Input(
    id="fahrenheitWidget",
    type='number',
    value=32,
    debounce=True
    )  

centigradeWidget= dcc.Input(
    id="centigradeWidget",
    type='number',
    value=0,
    debounce=True
    )  

calculationCounterWidget = dcc.Input(
    id="calculationCounterWidget",
    type='number',
    value=0,
    debounce=True
    )  

app.layout = html.Div([
    html.Span("Fahrenheit "),
    fahrenheitWidget,
    html.P(),
    html.Span("Centigrade "),
    centigradeWidget,
    html.P(),
    html.Span("Events    "),
    calculationCounterWidget,
    ])

@app.callback(
    [Output(component_id='calculationCounterWidget', component_property='value')],
    [Input(component_id='fahrenheitWidget',  component_property='value')]
    )
def updateFromFahreneit(input_value):
   print("update")
   return [input_value]

@app.callback(
    [Output(component_id='calculationCounterWidget', component_property='value')],
    [Input(component_id='centigradeWidget',  component_property='value')]
    )
def updateFromCentrigrade(input_value):
   print("update")
   return [input_value]


if __name__ == '__main__':
   app.run_server(debug=True)
