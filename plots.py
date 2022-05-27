from pydoc import classname
from dash import Input, Output, State, html, dcc
from visualizer import plotEquipment
import pandas as pd


def cleanData(df):
    df['daynum'] = df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year
    return df


def readData(path="datasets/russia_losses_equipment.csv"):
    data = pd.read_csv(path, index_col="date", parse_dates=['date'])
    return cleanData(data)


df = readData()

equipmentPlots = html.Div([
    
html.Div([
    html.Div([
        html.H3('AirCraft Loss'),
        dcc.Graph(
            id='graph-1',
            figure=plotEquipment(df, 'aircraft')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('Tank Loss over Days'),
        dcc.Graph(
            id='graph-2',
            figure=plotEquipment(df, 'tank')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('APC Loss '),
        dcc.Graph(
            id='graph-3',
            figure=plotEquipment(df, 'APC')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('field Artillery Loss'),
        dcc.Graph(
            id='graph-4',
            figure=plotEquipment(df, 'field artillery')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('MRL Loss'),
        dcc.Graph(
            id='graph-5',
            figure=plotEquipment(df, 'MRL')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('military auto Loss'),
        dcc.Graph(
            id='graph-6',
            figure=plotEquipment(df, 'military auto')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('fuel tank Loss'),
        dcc.Graph(
            id='graph-7',
            figure=plotEquipment(df, 'fuel tank')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('drone Loss'),
        dcc.Graph(
            id='graph-8',
            figure=plotEquipment(df, 'drone')
        )
    ], className="card-body")
], className="card mt-5"),

html.Div([
    html.Div([
        html.H3('naval ship Loss'),
        dcc.Graph(
            id='graph-9',
            figure=plotEquipment(df, 'naval ship')
        )
    ], className="card-body")
], className="card mt-5"),
])
