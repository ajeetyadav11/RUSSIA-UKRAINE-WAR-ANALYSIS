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
        html.H3('AirCraft Loss'),
        dcc.Graph(
            id='graph-1',
            figure=plotEquipment(df, 'aircraft')
        )
    ], className="card-body")
], className="card mt-5")
