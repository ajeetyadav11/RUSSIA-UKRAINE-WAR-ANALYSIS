import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, dcc
import pandas as pd
from plots import equipmentPlots, personalPlots, events
from dash.exceptions import PreventUpdate

app = dash.Dash(external_stylesheets=[
                dbc.themes.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.1.0/mdb.min.css'])
server = app.server
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
            # search_bar,
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

# home = html.Div([
#     html.Div([
#         html.Div([

#         ], className="col-md-3"),
#         html.Div([

#         ], className="col-md-9"),
#     ], className="row")

# ])

home_tags = [card_img]
cardDetails = [
    {
        'image': '/static/images/equpment.jpeg',
        'title': 'Equipment Loss Anlysis',
        'para': 'View complete Analysis of Loss of Equipments in the War',
        'link': '/equipmentloss'
    },
    {
        'image': '/static/images/personal.webp',
        'title': 'Personal Loss Anlysis',
        'para': 'View complete Analysis of Loss of Militry Personal in the War',
        'link': '/personalloss'
    },
    {
        'image': '/static/images/timeline.jpg',
        'title': 'War Timline Anlysis',
        'para': 'Timeline of events in the War till Date',
        'link': '/timeline'
    },
]

for detail in cardDetails:
    home_tags.append(
        html.A(
                dbc.Card([
                    dbc.CardImg(
                        src=detail.get('image'),
                        top=True,
                        style={"opacity": 0.7},
                    ),
                    dbc.CardBody([
                        html.H3(
                            detail.get('title')
                        ),
                        html.H6(
                            detail.get('para')
                        ),
                    ]),
                ], className='shadow mt-5')
                , href=detail.get('link'))
    )


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

index = [html.Div(home_tags, className='container'), cards]

app.layout = html.Div([dcc.Location(id="url", refresh=False), navbar,
                       html.Div([], id="page-content", className="pt-5")])


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def pages(pathname):
    if pathname == '/':
        return index
    elif pathname == '/datasets':
        return None
    elif pathname == '/equipmentloss':
        return equipmentPlots
    elif pathname == '/personalloss':
        return personalPlots
    elif pathname == '/timeline':
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
