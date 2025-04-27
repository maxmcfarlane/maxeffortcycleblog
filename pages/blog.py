import dash
import pandas as pd
import numpy as np
import io_
from dash import html, dcc
import dash_bootstrap_components as dbc
import components as cpts
from .landing import card_wrap

page = dash.Dash(__name__,
                 external_stylesheets=[dbc.themes.BOOTSTRAP],
                 title="Bashed the Balkans"
                 )
page.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Bashing the Balkans</title>
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

data = io_.read_data()

strava_comp = lambda c: html.Iframe(
            src=f"assets/{c}Strava.html",
            style={
                "width": "100%",
                "height": "900px",
                "border": "none",
                "overflow": "hidden"
            }
        )

strava_width = 3
tab1_content = lambda n, c: html.Div([
    dbc.Row([
        dbc.Col([
            strava_comp(c),
        ], xs=12, sm=12, md=strava_width, lg=strava_width, xl=strava_width),
        dbc.Col([
            card_wrap(
                html.P(n.get('title'), className="card-text") if n.get('title') else html.P(f'Navigating {c}', className="card-text"),
                [
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
                ], None
            )
        ], xs=12, sm=12, md=12-strava_width, lg=12-strava_width, xl=12-strava_width),
    ])
], style={"width": "100%", "height": "100%", "margin-top": "0.5rem"})

tabs = dbc.Tabs([
            dbc.Tab(
                tab1_content(data.to_dict()[c], c),
                label=c,
                label_style={'color': 'black'}
            ) for c in data.columns
        ]
)

body = [
    tabs
]
background_url = "/assets/frame.jpg"
style = {
    'backgroundImage': f'url({background_url})',
    'backgroundSize': 'cover',
    'backgroundPosition': 'top center',
    'backgroundRepeat': 'repeat-y',

}
page.layout = cpts.wrap_layout(body, style=style)
layout = page.layout

if __name__ == "__main__":
    page.run(debug=True)
