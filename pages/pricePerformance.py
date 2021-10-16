from pips import *
from dash import dcc
from dash import html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_current_prices = pd.read_csv(DATA_PATH.joinpath("df_current_prices.csv"))
df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))
df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))
df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv"))


###################################
lat, lon = 36.664187, -4.458605
mx, my = 100, 150
inclinacion, orientacion = 20, 30
muro_sur = 50

sombra = [(-150, 0), (-100, 20), (-140, 20), (-10, 0), (-9, 60),
          (10, 60), (11, 0), (39, 0), (40, 25), (90, 25), (91, 0), (-99, 0), ]

sombra_a, horizonte = sombras(lat, lon, sombra)
sombra_p, FS, tmy = sombras_perdidas(lat, lon, horizonte)
# libro = readAllSheets(DATA_PATH.joinpath('FV.xlsx'))
# df_fv = libro['LOC']
radiacion_meses = boxplots_meses(tmy)
fftarifa, dh, hh = tarifa_hora(tarifa='20TD', fecha_ini='2021-01-01')

ffirradiacionXmesYtarifa, gxt_m = irradiacionXmesYtarifa(hh, tmy)

###################################


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Pérdidas por Orientación e inclinación (planta)"], className="subtitle padded"
                                    ),
                                    html.P(
                                        [
                                            "Las pérdidas de radiación causadas por una orientación e inclinación del generador distintas \
                                    a las óptimas en el período de  diseño,"
                                        ],
                                    ),
                                    html.Img(src=paneles_planta(lat, lon, inclinacion, orientacion, mx, my, muro_sur), style={
                                        'width': '15vh', 'height': '20vh'}),
                                    html.Img(src=paneles_lateral(lat, lon, inclinacion, orientacion, mx, my, muro_sur), style={
                                        'width': '15vh', 'height': '20vh'}),

                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Pérdidas por sombras.\n Perfil de obstáculos"],
                                        className="subtitle padded",
                                    ),
                                    html.P(
                                        [
                                            "Cálculo de las pérdidas de radiación solar que \
                                            experimenta una superficie debidas a sombras circundantes. "
                                        ],
                                    ),


                                    html.Img(src=sombra_a, style={
                                        'width': '30vh', 'height': '20vh'}),

                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [

                            html.Div(
                                [
                                    html.H6(
                                        ["Pefil de radiacion horario anual"],
                                        className="subtitle padded",
                                    ),
                                    html.P(
                                        [
                                            ".."
                                        ],
                                    ),
                                    html.Img(src=sombra_p, style={
                                        'width': '30vh', 'height': '20vh'}),

                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "radiacion solar"
                                        ],

                                        className="subtitle padded",
                                    ),

                                    html.P(
                                        [
                                            ".."
                                        ],
                                    ),
                                    html.Img(src=radiacion_meses, style={
                                        'width': '40vh', 'height': '20vh'}),
                                ],
                                className="six columns",
                            )
                        ],
                        className="row ",
                    ),

                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Periodos tarifario"], className="subtitle padded"
                                    ),
                                    html.P(
                                        [
                                            " para valorar la generacion por periodo tarifario"
                                        ],
                                    ),
                                    html.Img(src=fftarifa, style={
                                        'width': '15vh', 'height': '10vh'}),

                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Distancia mínima entre filas de módulos (vli)"], className="subtitle padded"
                                    ),
                                    html.P(
                                        [
                                            ","
                                        ],
                                    ),
                                    html.Img(src=ffirradiacionXmesYtarifa, style={
                                        'width': '30vh', 'height': '20vh'}),

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
