import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    # html.A(
                    #     html.Img(
                    #         src=app.get_asset_url("dash-financial-logo.png"),
                    #         className="logo",
                    #     ),
                    #     href="https://eee.solar/",
                    # ),
                    # html.A(
                    #     html.Button(
                    #         "E3",
                    #         id="learn-more-button",
                    #         style={"margin-left": "-10px"},
                    #     ),
                    #     href="https://eee.solar/",
                    # ),
                    # html.A(
                    #     html.Button("Source Code", id="learn-more-button"),
                    #     href="https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Sistema FV")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            # dcc.Link(
                            #     "E3",
                            #     href="/dash-financial-report/full-view",
                            #     className="full-view-link",
                            # ),
                            dcc.Link(
                                "Completo",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Resumen ejecutivo",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Balace de Energia",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Instalacion",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "Finanazas", href="/dash-financial-report/fees", className="tab"
            ),
            dcc.Link(
                "Instalacion. Garantías",
                href="/dash-financial-report/distributions",
                className="tab",
            ),
            dcc.Link(
                "Parametros",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
