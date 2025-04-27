from dash import html
import dash_bootstrap_components as dbc

header = html.Div([
    html.A("Max Effort Cycling - Balkans by Bike",
                href='/', className="display-6 text-center text-dark", style={'text-decoration': 'none'})
], style={"background-color": "rgba(255,255,255,0.5)", "width": "100%", 'padding': '10px'})

drive_video_link = dbc.Container(
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


def wrap_layout(body_, style=None):
    style_default = {
        'maxWidth': '100%', 'fontFamily': 'Arial',
        'minHeight': '100vh',  # Full viewport height
        'width': '100%',
        'flexDirection': 'column',
        'justifyContent': 'center',
        'alignItems': 'center',
        'textAlign': 'center',
        'color': 'white',  # Light text on dark image
        'textShadow': '2px 2px 4px rgba(0,0,0,0.3)',  # Make text pop over image
    }
    if style is None:
        style = style_default
    else:
        style = {
            **style_default,
            **style,
        }
    return html.Div(
        style=style,
        children=[
            header,
            html.Div(body_, style={'padding': '20px'})
        ]
    )
