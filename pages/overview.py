import plotly.express as px
import dash_core_components as dcc
# import dash_html_components as html
from dash import html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

from pips import *


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


###################################
lat, lon = 36.664187, -4.458605

# libro = readAllSheets(DATA_PATH.joinpath('FV.xlsx'))
# df_fv = libro['LOC']



###################################


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            # html.Img(src='data:image/png;base64,{}'.format(encoded_image)),

            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [

                                    html.H5("Dimensionado del sistema"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    La estimación correcta de la energía consumida por el sistema fotovoltaico sólo es sencilla en \
                                    aquellas aplicaciones en las que se conocen exactamente las características de la carga (por \
                                    ejemplo, sistemas de telecomunicación). Sin embargo, en otras aplicaciones, como puede ser la \
                                    electrificación de viviendas, la tarea no resulta fácil pues intervienen multitud de factores que \
                                    afectan al consumo final de electricidad: tamaño y composición de las familias (edad, formación, \
                                    etc.), hábitos de los usuarios, capacidad para administrar la energía disponible, etc.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Localizacion"], className="subtitle padded"
                                    ),
                                    html.Img(src=mapa_ubicacion(lat, lon), style={
                                        'width': '20vh', 'height': '20vh'}),
                                ],
                                
                                className="four columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        " Vista satelite",
                                        className="subtitle padded",
                                    ),
                                    html.Img(src=foto_satelite(lat, lon), style={
                                        'width': '20vh', 'height': '20vh'}),
                                ],
                                className="six columns",
                            ),

                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Resumen de consumo - Estimado",
                                        className="subtitle padded",
                                    ),

                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [

                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Resumen de Ahorros", className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url(
                                            "risk_reward.png"),
                                        className="risk-reward",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
