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
                    'color': colors['text'],
                    'width': '80%', 
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'font-family': 'Arial'
                }
            )
        ])

introdution = html.Div([
    html.H2("Sistemas Dinâmicos no Hiperespaço dos contínuos e Difeomorfismo Morse-Smale"),
]) 

text_for_graph_1 = html.Div([
    dcc.Markdown(
        """
        A seguir, um gráfico feito com a função: x + k \sin(x).

        Essa função está definida no intervalo [0, 2π) e é um homeomorfismo. 
        Possui 2 pontos fixos, sendo π atrator e 0 repulsor. 
        Sua inversa possui os mesmos pontos fixos, porém repulsor e atrator se invertem.
        Quando levada ao hiperespaço, outros 3 pontos fixos aparecem além de 0 e π representados por: (1, 0) e (-1, 0). 
        São eles: A origem e os pontos (0, 0.5) e (0, -0.5).
        """,
       style={'font-size': '16px', 'font-family': 'Arial'}
    ), 
], style={'width': '80%', 'margin-left': 'auto', 'float': 'left', 'margin-right': 'auto'})

first_graph_layout = html.Div([
    html.Div([
        dcc.Graph(
            id='grafico_1',
            style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'}
        ),
    ], style={'width': '85%', 'float': 'left', 'margin-left': 'auto', 'margin-right': 'auto'}),
    html.Div([
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
            value='all',
            multi=False,
            clearable=False,
            style={'width': '100%'},
        ),
        dcc.Interval(
            id='interval-component',
            interval=df.interval_time,
            n_intervals=df.num_intervals
        ),
        html.Div([
        dcc.Checklist(
            id='auto-update-slider',
            options=[
                {'label': 'Incrementar valores iniciais automaticamente', 'value': 'auto-update'}
            ],
            value=[],
        ),
        dcc.Input(id='auto-step-graph-1', type='number', value=0.05, step=0.001),
        html.Div(id='auto-step-graph-1-value'),
        ], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '100px', 'margin-bottom': 'auto'}),
    ], style={'width': '15%', 'float': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '40px', 'margin-bottom': 'auto'}),

    html.Div([
        dcc.Slider(
            id='slider-x-inicial',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_step,
            value=sd.x_inicial,
            marks={i: f'{i:.2f}' for i in np.arange(0, np.pi, 1)},
            tooltip={"placement": "bottom", "always_visible": True},
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
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoB',
            updatemode='drag',
        ),
        dcc.Slider(
            id='slider-num-iteracoes',
            min=df.slider_iteracoes_min_value,
            max=df.slider_iteracoes_max_value,
            step=df.slider_iteracoes_step,
            value=sd.num_iteracoes,
            marks={i: str(i) for i in range(-25, 26, 1)},
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-iteracoes',
            updatemode='drag',
        ),
    ], style={'width': '100%', 'clear': 'both', 'margin-left': 'auto', 'margin-right': 'auto'}),

], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'})

second_graph_layout = html.Div([
    html.Div([
        dcc.Graph(
            id='grafico_2',
            style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'}
        ),
    ], style={'width': '85%', 'float': 'left', 'margin-left': 'auto', 'margin-right': 'auto'}),

    html.Div([
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
            value='all',
            multi=False,
            clearable=False,
            style={'width': '100%'},
        ),
        dcc.Interval(
            id='interval-component-2',
            interval=df.interval_time,
            n_intervals=df.num_intervals
        ),
        html.Div([
        dcc.Checklist(
            id='auto-update-slider-2',
            options=[
                {'label': 'Incrementar valores iniciais automaticamente', 'value': 'auto-update'}
            ],
            value=[],
        ),
        dcc.Input(id='auto-step-graph-2', type='number', value=0.05, step=0.001),
        html.Div(id='auto-step-graph-2-value'),
        ], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '100px', 'margin-bottom': 'auto'}),
    ], style={'width': '15%', 'float': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '40px', 'margin-bottom': 'auto'}),

    html.Div([
        html.H3("Valores iniciais")
    ],style={'width': '90%', 'clear': 'both', 'margin-left': 'auto', 'margin-right': 'auto'}),

    html.Div([
        dcc.Slider(
            id='slider-x-inicial-2',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_step,
            value=sd.x_inicial,
            marks={i: f'{i:.2f}' for i in np.arange(0, np.pi, 1)},
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoA',
            updatemode='drag',
        ),
        dcc.Slider(
            id='slider-xb-inicial-2',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_step,
            value=sd.xb_inicial,
            marks={i: f'{i:.2f}' for i in np.arange(0, np.pi, 1)},
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoB',
            updatemode='drag',
        ),
        dcc.Slider(
            id='slider-num-iteracoes-2',
            min=df.slider_iteracoes_min_value,
            max=df.slider_iteracoes_max_value,
            step=df.slider_iteracoes_step,
            value=sd.num_iteracoes,
            marks={i: str(i) for i in range(-25, 26, 1)},
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-iteracoes',
            updatemode='drag',
        ),
    ], style={'width': '100%', 'clear': 'both', 'margin-left': 'auto', 'margin-right': 'auto'}),

], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'})