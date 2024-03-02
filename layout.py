from grafico import np, sd
from dash import html, dcc
import definicoes as df

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

title = html.Div(style={'backgroundColor': colors['background']},
        children=[
            html.H1('Sistemas Dinâmicos no Hiperespaço dos contínuos e Difeomorfismo Morse-Smale',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            )
        ])

introdution = html.Div([

    html.H2("Sistemas Dinâmicos no Hiperespaço dos contínuos e Difeomorfismo Morse-Smale")
])

text_for_graph_1 = html.Div([
    html.H3("Função: "),
    html.Span("x + ", style={'font-size': '18px'}),  # Parte fixa do texto
    html.Span(html.Span(["sin", html.Sup("2"), "x"]), style={'font-size': '18px'}),  # sin^2(x)
    html.Span(" / 2", style={'font-size': '18px'}),  # Divisão por 2
])

first_graph_layout = html.Div([
    dcc.Graph(id='grafico_1'),

            dcc.Slider(
                id='slider-x-inicial',
                min=df.slider_min_value,
                max=df.slider_max_value,
                step=df.slider_step,
                value=sd.x_inicial,
                marks={i: f'{i:.2f}' for i in np.arange(0, np.pi, 1)},
                tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
                className='slider common-slider slider-pontoA',
                updatemode='drag',
            ),

            dcc.Slider(
                id='slider-xb-inicial',
                min=df.slider_min_value,
                max=df.slider_max_value,
                step=df.slider_step,
                value=sd.xb_inicial,
                marks={i: f'{i:.2f}' for i in np.arange(0, np.pi, 1)},
                tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
                className='slider common-slider slider-pontoB',
                updatemode='drag',  # Atualiza enquanto arrasta
            ),

            dcc.Slider(
                id='slider-num-iteracoes',
                min=df.slider_iteracoes_min_value,
                max=df.slider_iteracoes_max_value,
                step=df.iteracoes_step,
                value=sd.num_iteracoes,
                marks={i: str(i) for i in range(-25, 26, 1)},
                tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
                className='slider common-slider slider-iteracoes',
                updatemode='drag'
            ),

    dcc.Dropdown(
        id='plot-selector',
        options=[
            {'label': 'Círculo', 'value': 'circle'},
            {'label': 'Pontos A', 'value': 'circle_a'},
            {'label': 'Pontos B', 'value': 'circle_b'},
            {'label': 'Segmentos', 'value': 'segments'},
            {'label': 'Segmentos A', 'value': 'segments_a'},
            {'label': 'Segmentos B', 'value': 'segments_b'},
            {'label': 'A', 'value': 'a'},
            {'label': 'B', 'value': 'b'},
            {'label': '2 dimensoes', 'value': '2D'},
            {'label': 'Tudo', 'value': 'all'},
        ],
        value='all',  # Valor padrão
        multi=False,  # Permitir seleção única
        clearable=False,  # Não permitir que o usuário limpe a seleção
        style={'display': 'inline-block', 'textAlign': 'left', 'width': '30%'}
    ),

    dcc.Interval(
        id='interval-component',
        interval=df.interval_time,  # Intervalo de atualização em milissegundos
        n_intervals= df.num_intervals
    ),

    dcc.Checklist(
        id='auto-update-slider',
        options=[
            {'label': 'Atualizar Sliders Automaticamente', 'value': 'auto-update'}
        ],
        value=[]  # Nenhum valor selecionado inicialmente
    ),
])

second_graph_layout = html.Div([
    dcc.Graph(id='grafico_2'),
    dcc.Slider(
        id='slider-x-inicial-2',
        min=df.slider_min_value,
        max=df.slider_max_value,
        step=df.slider_step,
        value=sd.x2_inicial,  # Substitua pelo valor inicial adequado
        marks={i: f'{i:.2f}' for i in np.arange(0, 2*np.pi, 1)},
        tooltip={"placement": "bottom", "always_visible": True},
        className='slider common-slider slider-pontoA',
        updatemode='drag',

    ),

    dcc.Slider(
        id='slider-xb-inicial-2',
        min=df.slider_min_value,
        max=df.slider_max_value,
        step=df.slider_step,
        value=sd.xb2_inicial,
        marks={i: f'{i:.2f}' for i in np.arange(0, 2*np.pi, 1)},
        tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
        className='slider common-slider slider-pontoB',
        updatemode='drag',  # Atualiza enquanto arrasta
    ),

    dcc.Slider(
        id='slider-num-iteracoes-2',
        min=df.slider_iteracoes_min_value,
        max=df.slider_iteracoes_max_value,
        step=df.iteracoes_step,
        value=sd.num_iteracoes_2,
        marks={i: str(i) for i in range(-25, 26, 1)},
        tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
        className='slider common-slider slider-iteracoes',
        updatemode='drag',
    ),

     dcc.Dropdown(
        id='plot-selector-2',
        options=[
            {'label': 'Círculo', 'value': 'circle'},
            {'label': 'Pontos A', 'value': 'circle_a'},
            {'label': 'Pontos B', 'value': 'circle_b'},
            {'label': 'Segmentos', 'value': 'segments'},
            {'label': 'Segmentos A', 'value': 'segments_a'},
            {'label': 'Segmentos B', 'value': 'segments_b'},
            {'label': 'A', 'value': 'a'},
            {'label': 'B', 'value': 'b'},
            {'label': '2 dimensoes', 'value': '2D'},
            {'label': 'Tudo', 'value': 'all'},
        ],
        value='all',  # Valor padrão
        multi=False,  # Permitir seleção única
        clearable=False,  # Não permitir que o usuário limpe a seleção
        style={'display': 'inline-block', 'textAlign': 'left', 'width': '30%'}
    ),

    dcc.Interval(
        id='interval-component-2',
        interval=df.interval_time,
        n_intervals= df.num_intervals  
    ),

    dcc.Checklist(
        id='auto-update-slider-2',
        options=[
            {'label': 'Atualizar Sliders Automaticamente', 'value': 'auto-update'}
        ],
        value=[]  # Nenhum valor selecionado inicialmente
    ),
])

