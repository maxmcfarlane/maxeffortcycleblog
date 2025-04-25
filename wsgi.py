import dash
import pandas as pd
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Bashed the Balkans"
                )
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Bashed the Balkans</title>
        <link rel="icon" href="https://example.com/your_favicon.ico">
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# pd.read_clipboard().to_pickle(open('./data.pickle', '+wb'))
# data: pd.DataFrame = pd.read_pickle(open('./data.pickle', 'rb'))
data = pd.read_excel(r"C:\Users\maxmc\Documents\Code\blog\data.xlsx", index_col=0).replace(np.nan, None)

strava_comp = lambda c: html.Iframe(
            src=f"assets/{c}Strava.html",
            style={
                "width": "100%",
                "height": "550px",
                "border": "none",
                "overflow": "hidden"
            }
        )
tab1_content = lambda n, c: html.Div([
    dbc.Row([
        dbc.Col([
            strava_comp(c) if n.get('strava_embed') else None,
        ], xs=12, sm=12, md=4, lg=4, xl=4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    html.P(n.get('title'), className="card-text") if n.get('title') else html.P(f'Navigating {c}', className="card-text")
                ),
                dbc.CardBody([
                    dcc.Markdown(n.get('content_markdown'), className="card-text") if n.get('content_markdown') else html.P(n.get('content'), className="card-text"),

                    html.Img(
                        src=n.get('img_src'),
                        style={'width': '100%', 'borderRadius': '10px'}
                    ) if n.get('img_src') else None,

                    html.Video(
                        controls=True,
                        style={"width": "100%", "borderRadius": "10px"},
                        children=[
                            html.Source(src=n.get('vid_src'), type="video/mp4")
                        ]
                    ) if n.get('vid_src') else None,
                ])
            ], className="mt-3")
        ], xs=12, sm=12, md=8, lg=8, xl=8),
    ])
], style={"width": "100%", "height": "100%"})

tabs = dbc.Tabs([
            dbc.Tab(
                tab1_content(data.to_dict()[c], c),
                label=c) for c in data.columns
        ]
)

app.layout = html.Div(
    style={'maxWidth': '100%', 'margin': 'auto', 'padding': '20px', 'fontFamily': 'Arial'},
    children=[
        html.H1("Bashed the Balkans", style={'textAlign': 'center'}),
        dbc.Tab(
            dbc.Container(
                dbc.Card(
                    dbc.CardBody(
                        html.A("📹 Watch the video on Google Drive",
                               href="https://drive.google.com/file/d/1FviTwPUO8vtA5Pii6Ao2nLcoHxVnzWqa/view?usp=sharing",
                               target="_blank",
                               style={"textDecoration": "none", "fontWeight": "bold", "fontSize": "1.2rem"})
                    ),
                    className="mt-4 m-3"
                )
            )
        ),
        tabs
    ]
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
