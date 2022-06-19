import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, dcc
import pandas as pd
from plots import equipmentPlots, personalPlots, events
from dash.exceptions import PreventUpdate

app = dash.Dash(external_stylesheets=[
                dbc.themes.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.1.0/mdb.min.css'])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# def createCard(img, bodyChildren):
#     return dbc.Card([
#         dbc.CardImg(
#                     src=img,
#                     top=True,
#                     style={"opacity": 0.3},
#                     ),
#         dbc.CardImgOverlay(
#             [dbc.CardBody(bodyChildren)]
#         )
#     ], className='shadow'),


def categoryAnalysis():
    return


search_bar = dbc.Row([
    dbc.Col(
        dbc.Button(
            "Home", color="dark", className="ms-2", n_clicks=0
        ), width="auto"
    ),
    dbc.Col(
        dbc.Button(
            "Dataset", color="dark", className="ms-2", n_clicks=0
        ), width="auto"
    ),
    dbc.Col(
        dbc.Button(
            "About", color="dark", className="ms-2", n_clicks=0
        ), width="auto"
    ),
    dbc.Col(
        dbc.Input(type="search", placeholder="Search")
    ),
    dbc.Col(
        dbc.Button(
            "Search", color="primary", className="ms-2", n_clicks=0
        ), width="auto"
    )
], className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center")

navbar = dbc.Navbar([
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(
                    html.Img(
                        src=PLOTLY_LOGO,
                        height="30px"
                    )
                ),
                dbc.Col(
                    dbc.NavbarBrand([
                        "Russo Ukraine War"
                    ], className="ms-2 dodgerblue")
                )
            ], align="center", className="g-0"),
            href="https://plotly.com", style={"textDecoration": "none"}),
        dbc.NavbarToggler(
            id="navbar-toggler",
            n_clicks=0),
        dbc.Collapse(
            search_bar,
            id="navbar-collapse",
            is_open=False,
            navbar=True)
    ])
], color="dodgerblue", className="fixed-top")

card_img = dbc.Container([
    dbc.Card([
        dbc.CardImg(
            src="/static/images/front pages.webp",
            top=True,
            style={"opacity": 0.2},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody([
                html.P("Russia Ukraine War",
                       className="display-3 fw-bold text-muted"),
                html.P([
                    "Let's stop it"
                ], className="card-text1"),

            ])
        )
    ], className='shadow')
], className="pt-5")

home = html.Div([
    html.Div([
        html.Div([
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/equpment.jpeg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.Button([
                            "Equipment Loss Analysis"
                        ], className="btn btn-primary w-100", id="equipment-button"),
                    ]),
                )
            ], className='shadow'),
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/personal.webp",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.Button([
                            "Personal Loss Analysis"
                        ], className="btn btn-primary w-100", id="personal-button"),
                    ]),
                )
            ], className='shadow'),
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/timeline.jpg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.Button([
                            "Timeline Analysis"
                        ], className="btn btn-primary card-title w-100", id="timeline-button"),
                    ]),
                )
            ], className='shadow'),
        ], className="col-md-3"),
        html.Div([
            card_img
        ], className="col-md-9"),
    ], className="row")

], className="container-fluid mt-5")

cards = html.Div([
    html.Div([
        html.Div([
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/analysis.jpg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.H4([
                            "Analysis"
                        ], className="font-medium card-title"),
                        html.B([
                            "Travel through various types of graphs and interpretations"
                        ], className="card-text"),
                    ]),
                )
            ], className='shadow'),
        ], className="col-4 mb-4"),

        html.Div([
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/info.png",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.H4([
                            "Informative"
                        ], className="card-title"),
                        html.B([
                            "Discover past trends and predict the ones coming"
                        ], className="card-text"),
                    ]),
                )
            ], className='shadow'),
        ], className="col-4 mb-4"),

        html.Div([
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/access.jpg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.H4([
                            "Accessible"
                        ], className="card-title"),
                        html.B([
                            "Open for all - students, public, corporations, government"
                        ], className="card-text"),
                    ]),
                )
            ], className='shadow'),
        ], className="col-4 mb-4")
    ], className="row"),
], className="container", style={"margin-top": "5rem"})

footer = html.Footer([
    html.Div([
        html.H5("Copyright")
    ], className="footer-copyright text-center pt-2 pb-1 shadow")],
    className="page-footer font-small blue down mt-5",
    style={"background-color": "white", "color": "dodgerblue"},
)

app.layout = html.Div([
    navbar,
    home,
    html.Div(id="equipment-div"),
    html.Div(id="personal-div"),
    html.Div(id="timeline-div"),
], className="pt-5")

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)

def pages(pathname):
    if pathname == '/':
        return index
    elif pathname == '/datasets':
        return dataset

@app.callback(
    Output(component_id='equipment-div', component_property='children'),
    Input(component_id='equipment-button', component_property='n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return equipmentPlots


@app.callback(
    Output(component_id='personal-div', component_property='children'),
    Input(component_id='personal-button', component_property='n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return personalPlots


@app.callback(
    Output(component_id='timeline-div', component_property='children'),
    Input(component_id='timeline-button', component_property='n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return events


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
