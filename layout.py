from grafico import np, sd
from dash import html, dcc

second_graph_layout = html.Div([
    dcc.Graph(id='grafico-interativo-2'),
    dcc.Slider(
        id='slider-x-inicial-2',
        min=0.0,
        max=2*np.pi,
        step=0.0001,
        value=sd.x2_inicial,  # Substitua pelo valor inicial adequado
        marks={i: f'{i:.2f}' for i in np.arange(0, 2*np.pi, 1)},
        tooltip={"placement": "bottom", "always_visible": True},
        className='slider common-slider slider-pontoA',
        updatemode='drag',
    ),

    dcc.Slider(
        id='slider-xb-inicial-2',
        min=0.0,
        max=2*np.pi,
        step=0.0001,
        value=sd.xb2_inicial,
        marks={i: f'{i:.2f}' for i in np.arange(0, 2*np.pi, 1)},
        tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
        className='slider common-slider slider-pontoB',
        updatemode='drag',  # Atualiza enquanto arrasta
    ),

    dcc.Slider(
        id='slider-num-iteracoes-2',
        min=-25,
        max=25,
        step=1,
        value=sd.num_iteracoes_2,
        marks={i: str(i) for i in range(-25, 26, 1)},
        tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
        className='slider common-slider slider-iteracoes',
        updatemode='drag',
    ),

    dcc.RadioItems(
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
        labelStyle={'display': 'block'},
        style={'display': 'inline-block'},
    ),

    dcc.Interval(
        id='interval-component-2',
        interval=100,  # Intervalo de atualização em milissegundos
        n_intervals=0
    ),
])

first_graph_layout = html.Div([
    dcc.Graph(id='grafico-interativo'),
    dcc.Slider(
        id='slider-x-inicial',
        min=0.0,
        max=np.pi,
        step=0.0001,
        value=sd.x_inicial,
        marks={i: f'{i:.2f}' for i in np.arange(0, np.pi, 1)},
        tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
        className='slider common-slider slider-pontoA',
        updatemode='drag',

    ),

    dcc.Slider(
        id='slider-xb-inicial',
        min=0.0,
        max=np.pi,
        step=0.0001,
        value=sd.xb_inicial,
        marks={i: f'{i:.2f}' for i in np.arange(0, np.pi, 1)},
        tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
        className='slider common-slider slider-pontoB',
        updatemode='drag',  # Atualiza enquanto arrasta
    ),

    dcc.Slider(
        id='slider-num-iteracoes',
        min=-25,
        max=25,
        step=1,
        value=sd.num_iteracoes,
        marks={i: str(i) for i in range(-25, 26, 1)},
        tooltip={"placement": "bottom", "always_visible": True},  # Adiciona tooltip
        className='slider common-slider slider-iteracoes',
        updatemode='drag',
    ),

    dcc.RadioItems(
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
        labelStyle={'display': 'block'},
        style={'display': 'inline-block',
                'textAlign': 'left',
                },

    ),

    dcc.Interval(
        id='interval-component',
        interval=100,  # Intervalo de atualização em milissegundos
        n_intervals=0
    )
])
