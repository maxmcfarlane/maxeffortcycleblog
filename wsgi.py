import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash.dependencies as dd
import pages.landing as landing
import pages.blog as blog

app = dash.Dash(__name__, title='MEC', external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    dd.Output('page-content', 'children'),
    dd.Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/main':
        return blog.layout
    else:
        return landing.layout

server = app.server

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
    # app.run(debug=True)
