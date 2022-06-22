from dash import *
import pandas as pd
import dash_bootstrap_components as dbc
from buttons import *
from Footer import footer
from datasets_load import *


dataset =  dbc.Container([
    html.Br(),
    html.Div([
        html.Div(['Demo Dataset'],className="col card-title")
    ], className='row text-center'),
    dash_table.DataTable(fooddemo.to_dict('records'),[{"name": i, "id": i} for i in fooddemo.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
    html.Br(),
    html.Div([
        html.Div([
            "(Demo) World Food Production:",
            html.Br(),save_datasetdemo,
            dcc.Download(id='ddemo')
        ], className='col bttn name-data'),
        html.Div([
            "(Org) World Food Production:",
            html.Br(),save_datasetorg,
            dcc.Download(id='dorg')
        ], className='col bttn name-data')
    ], className="row text-center"),
    html.Hr()
]), footer

@callback(
    Output('tbl_out', 'children'), 
    Input('tbl', 'active_cell')
)
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"

@callback(
    Output('ddemo', 'data'),
    Input('demo', 'n_clicks'),
    prevent_initial_call=True,
)
def demodataset(n_clicks):
    return dcc.send_data_frame(fooddemo.to_csv, '(Demo) World Food Production.csv')

@callback(
    Output('dorg', 'data'),
    Input('org', 'n_clicks'),
    prevent_initial_call=True,
)
def orgdataset(n_clicks):
    return dcc.send_data_frame(foodorg.to_csv, '(Org) World Food Production.csv')
