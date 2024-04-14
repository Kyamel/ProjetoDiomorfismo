from dash import html, dcc
import definitions as df
import sistemasDinamicos as sd

blank = html.Div([
    
], style={'width':'100%', 'clear': 'both', 'height':'16px'})

user_graph_layout = html.Div([
    blank,
    html.Div([
        dcc.Graph(
            id='grafico_user',
            style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'}
        ),
    ],
    className='graph'),
    html.Div([
        dcc.Dropdown(
            id='plot-selector-u',
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
            id='interval-component-u',
            interval=df.interval_time,
            n_intervals=df.num_intervals
        ),
        blank,
        html.Div([
            html.Div("Digite sua função aqui"),
            dcc.Input(id='user-func', type='text', value="x + sin(x)/2"),
            html.Div(id='output-user-func'),
        ], className='userFuncBox'),
        blank,
        html.Div([
        dcc.Checklist(
            id='auto-update-slider-u',
            options=[
                {'label': 'Incrementar valores iniciais automaticamente', 'value': 'auto-update'}
            ],
            value=[],
        ),
        dcc.Input(id='auto-step-graph-u', type='number', value=0.05, step=0.001),
        html.Div(id='auto-step-graph-u-value'),
        ], className='checklist'),
    ],
    className='graph_menu'),
    blank,
    html.Div([
        html.A("Valor inicial: A"),
        dcc.Slider(
            id='slider-x-inicial-u',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_valores_iniciais_step,
            value=sd.xu_inicial,
            marks=df.marks_valores_iniciais,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoA',
            updatemode='drag',
        ),
        html.A("Valor inicial: B"),
        dcc.Slider(
            id='slider-xb-inicial-u',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_valores_iniciais_step,
            value=sd.xu_inicial,
            marks=df.marks_valores_iniciais,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoB',
            updatemode='drag',
        ),
        html.A("Número de iterações"),
        dcc.Slider(
            id='slider-num-iteracoes-u',
            min=df.slider_iteracoes_min_value,
            max=df.slider_iteracoes_max_value,
            step=df.slider_iteracoes_step,
            value=sd.num_iteracoes_u,
            marks=df.marks_iteracoes,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-iteracoes',
            updatemode='drag',
        ),
    ], 
    className='graph_slider'),

], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'})