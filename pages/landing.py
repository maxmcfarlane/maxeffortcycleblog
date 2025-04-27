import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import components as cpts

page = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

card_wrap = lambda header_, body_, footer_: dbc.Card([
    dbc.CardHeader(header_),
    dbc.CardBody(body_, style={
    'justifyContent': 'left',
    'alignItems': 'left',
    'textAlign': 'left',
    'color': 'black',
}),
    dbc.CardFooter(footer_) if footer_ is not None else None,
], style={
    "background-color": "rgba(255,255,255,0.5)",
})

komoot_comp = card_wrap(
    None,
    html.Iframe(
        src=f"https://www.komoot.com/collection/3362081/embed",
        style={
            "width": "100%",
            "height": "440px",
            "border": "none",
            "overflow": "hidden",
        }
    ),
    None,
)

landing_activity = card_wrap(None,
                             html.Iframe(
                                 src=f"assets/LandingActivity.html",
                                 style={
                                     "width": "100%",
                                     "height": "80vh",
                                     "border": "none",
                                     "overflow": "hidden"
                                 }
                             ),
                             None)

body = [
    dbc.Row([
        dbc.Col(landing_activity, xs=12, sm=12, md=4, lg=4, xl=4),
        dbc.Col([

            card_wrap(None, dbc.Row([
                    dbc.Col([
                        dbc.Container([
                            dbc.Button(
                                "🚴‍♂️ Enter the Journey",
                                href="/main",  # You will need a route or a link to your main app
                                color="light", className="me-1",
                                size="md",
                            )
                        ]),
                    ]),
                    dbc.Col([
                        dbc.Container(
                            dbc.Button(
                                "📹 Drone Footage",
                                href="https://drive.google.com/file/d/1FviTwPUO8vtA5Pii6Ao2nLcoHxVnzWqa/view?usp=sharing",
                                # You will need a route or a link to your main app
                                color="light", className="me-1",
                                size="md",
                            )
                        ),
                    ]),
            ]), None),

        ], xs=12, sm=12, md=4, lg=4, xl=4),
        dbc.Col(komoot_comp, xs=12, sm=12, md=4, lg=4, xl=4),

    ]),

]
background_url = "/assets/frame3.jpg"
style = {
    'backgroundImage': f'url({background_url})',
    'backgroundSize': 'cover',
    'backgroundPosition': 'top center',
    'backgroundRepeat': 'repeat',

}

page.layout = cpts.wrap_layout(body, style=style)
layout = page.layout

if __name__ == "__main__":
    page.run(debug=True)
