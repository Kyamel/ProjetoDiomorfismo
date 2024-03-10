import dash
from dash import html
import layout
import callbacks as cb
import comentarios
app = dash.Dash(__name__, external_stylesheets=['/assets/styles.css'])

disqus_script = comentarios.disqus_script

# Adiciona o layout dos graficos ao aplicativo
app.layout = html.Div(children=[
    layout.title,
    layout.logo,
    layout.introdution,
    layout.text_for_graph_1,
    layout.first_graph_layout,
    layout.second_graph_layout,

    html.Div([html.Script(disqus_script)])
    ], 
    className='graph_page'
)

# Callback para atualizar o gráfico com base nos sliders

cb.register_auto_slider_callback(app)
cb.register_grafico_callback(app)
cb.register_enter_step_callback(app)
#cb.register_graph_scale_callback(app)

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
