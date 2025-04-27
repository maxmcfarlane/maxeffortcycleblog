import dash
from dash import html
import dash_bootstrap_components as dbc

landing_app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Bashed the Balkans - Landing",
)

landing_app.layout = html.Div(
    style={'textAlign': 'center', 'padding': '50px', 'fontFamily': 'Arial'},
    children=[
        html.H1("Bashed the Balkans", style={'fontSize': '3rem', 'marginBottom': '20px'}),
        html.P("One bike. Four weeks. Endless stories from the Balkans.", style={'fontSize': '1.5rem'}),
        html.Img(
            src="https://your_cdn_or_s3_bucket/balkan_hero_image.jpg",
            style={'width': '80%', 'borderRadius': '15px', 'marginTop': '30px'}
        ),
        dbc.Button(
            "Enter the Journey 🚴‍♂️",
            href="/main",  # You will need a route or a link to your main app
            color="primary",
            size="lg",
            style={'marginTop': '40px'}
        )
    ]
)

if __name__ == "__main__":
    landing_app.run(debug=True, host='0.0.0.0')
