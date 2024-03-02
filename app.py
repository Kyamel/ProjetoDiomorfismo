import dash
from dash import html, dcc, Input, Output, State
import update
import layout
import definicoes as df

app = dash.Dash(__name__)

# Adiciona o layout dos graficos ao aplicativo
app.layout = html.Div([
    layout.title,
    layout.introdution,
    layout.text_for_graph_1,
    layout.first_graph_layout,
    layout.second_graph_layout,

    ])

# Adicionar o arquivo CSS local
app.css.append_css({
    'external_url': '/assets/styles.css'
})

# Callback para atualizar o gráfico com base nos sliders


@app.callback(
    [
        Output('slider-x-inicial', 'value'),
        Output('slider-xb-inicial', 'value'),
        Output('interval-component', 'disabled'),
    ],
    [
        Input('auto-update-slider', 'value'),
        Input('interval-component', 'n_intervals')
    ],
    [   
        State('slider-x-inicial', 'value'),
        State('slider-xb-inicial', 'value')
    ],
    prevent_initial_call=True
)

def update_sliders(auto_update_value, n_intervals, x, xb):
    return update.update_sliders(auto_update_value, n_intervals, x, xb)

@app.callback(
    [
        Output('slider-x-inicial-2', 'value'),
        Output('slider-xb-inicial-2', 'value'),
        Output('interval-component-2', 'disabled'),
    ],
    [
        Input('auto-update-slider-2', 'value'),
        Input('interval-component-2', 'n_intervals')
    ],
    [   
        State('slider-x-inicial-2', 'value'),
        State('slider-xb-inicial-2', 'value')
    ],
    prevent_initial_call=True
)

def update_sliders(auto_update_value, n_intervals, x, xb):
    return update.update_sliders(auto_update_value, n_intervals, x, xb)

@app.callback(
    Output('grafico_1', 'figure'),
    [
        Input('slider-x-inicial', 'value'),
        Input('slider-xb-inicial', 'value'),
        Input('slider-num-iteracoes', 'value'),
        Input('plot-selector', 'value'),
    ],
    prevent_initial_call=False,
)

def update_grafico_callback(x_inicial, xb_inicial, num_iteracoes, selected_option='All'):
    return update.update_grafico(x_inicial, xb_inicial, num_iteracoes, selected_option)

@app.callback(
    Output('grafico_2', 'figure'),
    [
        Input('slider-x-inicial-2', 'value'),
        Input('slider-xb-inicial-2', 'value'),
        Input('slider-num-iteracoes-2', 'value'), 
        Input('plot-selector-2', 'value'),
    ],
    prevent_initial_call=False,
)

def update_grafico_2_callback(x2_inicial, xb2_inicial, num_iteracoes_2, selected_option='All'):
    return update.update_grafico_2(x2_inicial, xb2_inicial, num_iteracoes_2, selected_option)

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
