import dash
from dash import html, dcc, Input, Output
import callbacks as cb
import comentarios
import pages
from datetime import datetime

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

init_proc_time = datetime.now()
time_str = init_proc_time.strftime("%Y-%m-%d %H:%M:%S")
with open('log.txt', 'a') as file:
    file.write(f"\n>>>>>> INITIALIZING PROCESS at {time_str} <<<<<<\n")
# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=False)

end_proc_time = datetime.now()
time_str2 = end_proc_time.strftime("%Y-%m-%d %H:%M:%S")
total_time = end_proc_time - init_proc_time
with open('log.txt', 'a') as file:
    file.write(f"\n>>>>>> PROCESS TERMINATED at {time_str2}. PROCESS TIME: {str(total_time)} <<<<<<\n")
