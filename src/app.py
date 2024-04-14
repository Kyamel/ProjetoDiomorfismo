import dash
from dash import html, dcc, Input, Output
import callbacks as cb
import comentarios
import pages

app = dash.Dash(__name__, external_stylesheets=['/assets/styles.css'], suppress_callback_exceptions=True)

disqus_script = comentarios.disqus_script

# Adiciona o layout dos graficos ao aplicativo
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.Nav([
        dcc.Link('Home Page.', href='/home_page'),
        dcc.Link('Sandbox Page.', href='/sandbox_page'),
    ]),
])

# Callback para alterar página
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    # Determina qual layout será exibido
    if pathname is None or pathname == "/":
        layout = pages.home_page_layout()
    elif pathname == '/home_page':
        layout = pages.home_page_layout()
    elif pathname == '/sandbox_page':
        layout = pages.sandbox_page_layout()
    else:
        layout = '404 - Page not found'
    return layout

cb.register_activate_arc_callback(app)
cb.reister_arc_size_callback(app)
cb.register_graph_callback(app)
cb.register_auto_slider_callback(app)
cb.register_enter_step_callback(app)

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
