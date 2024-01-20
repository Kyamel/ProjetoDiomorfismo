import dash
from dash import html, Input, Output
from update import update_grafico, update_grafico_2
from layout import first_graph_layout, second_graph_layout

app = dash.Dash(__name__)

# Adiciona o layout dos graficos ao aplicativo
app.layout = html.Div([second_graph_layout, first_graph_layout])

# Adicionar o arquivo CSS local
app.css.append_css({
    'external_url': '/assets/styles.css'
})

# Callback para atualizar o gráfico com base nos sliders

@app.callback(
    Output('grafico-interativo-2', 'figure'),
    [
        Input('slider-x-inicial-2', 'value'),
        Input('slider-xb-inicial-2', 'value'),
        Input('slider-num-iteracoes-2', 'value'), 
        Input('plot-selector-2', 'value'),
    ],
    prevent_initial_call=False,
)

def update_grafico_2_callback(x2_inicial, xb2_inicial, num_iteracoes_2, selected_option='All'):
    return update_grafico_2(x2_inicial, xb2_inicial, num_iteracoes_2, selected_option)

@app.callback(
    Output('grafico-interativo', 'figure'),
    [
        Input('slider-x-inicial', 'value'),
        Input('slider-xb-inicial', 'value'),
        Input('slider-num-iteracoes', 'value'),
        Input('plot-selector', 'value'),
    ],
    prevent_initial_call=False,
)

def update_grafico_callback(x_inicial, xb_inicial, num_iteracoes, selected_option='All'):
    return update_grafico(x_inicial, xb_inicial, num_iteracoes, selected_option)

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
