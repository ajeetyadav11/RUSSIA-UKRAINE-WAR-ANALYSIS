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


df = readData("datasets/russia_losses_equipment (1) (1).csv")
df2 = readData("datasets/russia_losses_personnel.csv")

equipmentPlots = html.Div([

    html.Div([
        html.Div([
            html.H3('AirCraft Loss', className="text-center"),
            dcc.Graph(
                id='graph-1',
                figure=plotEquipment(df, 'aircraft')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('Tank Loss over Days', className="text-center"),
            dcc.Graph(
                id='graph-2',
                figure=plotEquipment(df, 'tank')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('APC Loss', className="text-center"),
            dcc.Graph(
                id='graph-3',
                figure=plotEquipment(df, 'APC')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('field Artillery Loss', className="text-center"),
            dcc.Graph(
                id='graph-4',
                figure=plotEquipment(df, 'field artillery')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('MRL Loss', className="text-center"),
            dcc.Graph(
                id='graph-5',
                figure=plotEquipment(df, 'MRL')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('military auto Loss', className="text-center"),
            dcc.Graph(
                id='graph-6',
                figure=plotEquipment(df, 'military auto')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('fuel tank Loss', className="text-center"),
            dcc.Graph(
                id='graph-7',
                figure=plotEquipment(df, 'fuel tank')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('drone Loss',className="text-center"),
            dcc.Graph(
                id='graph-8',
                figure=plotEquipment(df, 'drone')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('Naval Ship Loss', className="text-center"),
            dcc.Graph(
                id='graph-9',
                figure=plotEquipment(df, 'naval ship')
            )
        ], className="card-body")
    ], className="card mt-5"),
])


personalPlots = html.Div([

    html.Div([
        html.Div([
            html.H3('personnel', className="text-center"),
            dcc.Graph(
                id='graph-10',
                figure=plotEquipment(df2, 'personnel')
            )
        ], className="card-body")
    ], className="card mt-5"),

    html.Div([
        html.Div([
            html.H3('Prisoners Of War', className="text-center"),
            dcc.Graph(
                id='graph-11',
                figure=plotEquipment(df2, 'POW')
            )
        ], className="card-body")
    ], className="card mt-5"),
])

events = html.Div([

    html.Div([
        html.Div([
            html.H3('Major Conflict Areas', className="text-center"),
            html.H5("The Russian attacks mostly focus on the Eastern region. The most dangerous areas are Kyiv, Kharkiv, Luhans'K, and Donets'k, with over 200 military events happening in each province. Whereas the middle and Western Ukraine seems to be safer with less military operations reported."),
            html.Img(src="./static/conflict_map.png"),
        ], className="card-body")
    ], className="card mt-5"),
    
    html.Div([
        html.Div([
            html.H3('Russian Equipment And Personnel Losses', className="text-center"),
            html.H5("The Intensive Battle shown above also came with high attrition in equipment and personnel. By May 19th, the Russian military has suffered severe losses in equipment. Most of the losses belong to ground vehicles including APC (Armed Personnel Carrier) and tanks. This is mostly caused by the poor supply situation and Ukraine's newly equipped anti-tank weapons provided by NATO. Notably, despite the lack of aircraft and helicopters, the Ukrainians were able to bring down a considerable amount of Russian aircraft and helicopters using anti-air weapons."),
            html.Img(src="./static/Screenshot.png"),
        ], className="card-body")
    ], className="card mt-5"),
   
   html.Div([
        html.Div([
            html.H3('% Dependency on Russian Gas Exports', className="text-center"),
             html.Img(src="./static/Screenshot1.png"),
             html.Img(src="./static/Screenshot2.png"),
             html.Img(src="./static/Screenshot3.png"),
        ], className="card-body")
    ], className="card mt-5"),
    html.Div([
        html.Div([
            html.H3('Civilians Injured in Ukraine', className="text-center"),
             html.Img(src="./static/Civilians Injured.png"),
                     ], className="card-body")
    ], className="card mt-5"),
    html.Div([
        html.Div([
            html.H3('Civilians Killed in Ukraine', className="text-center"),
             html.Img(src="./static/Civilians Killed.png"),
                     ], className="card-body")
    ], className="card mt-5"),
])
