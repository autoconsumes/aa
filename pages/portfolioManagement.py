from dash import dcc
from dash import html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_equity_char = pd.read_csv(DATA_PATH.joinpath("df_equity_char.csv"))
df_equity_diver = pd.read_csv(DATA_PATH.joinpath("df_equity_diver.csv"))
from pips import *
fftabla=tablaIII()

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Portfolio"],
                                         className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="rows",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P(["Stock style"], style={
                                           "color": "#7a7a7a"}),
                                    html.Img(src=fftabla, style={
                                        'width': '55vh', 'height': '50vh'}),
                                ],
                                className="four columns",
                            ),
                            html.Div(
                                [
                                    html.P(
                                        "Calibre Index Fund seeks to track the performance of\
                        a benchmark index that measures the investment return of large-capitalization stocks."
                                    ),
                                    html.P(
                                        "Learn more about this portfolio's investment strategy and policy."
                                    ),
                                ],
                                className="eight columns middle-aligned",
                                style={"color": "#696969"},
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Br([]),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Equity characteristics as of 01/31/2018"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(
                                        make_dash_table(df_equity_char),
                                        className="tiny-header",
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Equity sector diversification"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(
                                        make_dash_table(df_equity_diver),
                                        className="tiny-header",
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
