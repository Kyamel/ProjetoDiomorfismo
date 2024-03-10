from grafico import np, sd
from dash import html, dcc
import definicoes as df

blank = html.Div([
    
], style={'width':'100%', 'clear': 'both', 'height':'16px'})

title = html.Div(
        children=[
            html.H2('Sistemas Dinâmicos no Hiperespaço dos contínuos e Difeomorfismo Morse-Smale'),
        ], className='title')

logo = html.Div(children=[
    html.Img(src='/assets/Logomarca_ufop.jpg', 
             style={'width': '100%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}
            ),
    ],className='logo')

introdution = html.Div([
    html.H3("Sistemas Dinâmicos no Hiperespaço dos contínuos e Difeomorfismo Morse-Smale"),
    
], style={'width': '80%', 'float': 'right'})

text_for_graph_1 = html.Div([
    dcc.Markdown(
        """
        A seguir, um gráfico feito com a função: x + k \sin(x).

        Essa função está definida no intervalo [0, 2π) e é um homeomorfismo. 
        Possui 2 pontos fixos, sendo (0, π) atrator e (0, 0) repulsor. 
        Sua inversa possui os mesmos pontos fixos, porém repulsor e atrator se invertem.
        Quando levada ao hiperespaço, outros 3 pontos fixos aparecem além de (0, π) e (0, 0) representados no círculo por: (1, 0) e (-1, 0). 
        São eles: A origem e os pontos (0, 0.5) e (0, -0.5).
        """,
       style={'font-size': '16px', 'font-family': 'Arial', 'text-align': 'justify', 'padding': '16px'}
    ),
    ], className='text_for_graph_1'
)

first_graph_layout = html.Div([
    blank,
    html.Div([
        dcc.Graph(
            id='grafico_1',
            style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'}
        ),
    ],
    className='graph'),
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
        ], className='checklist'),
    ],
    className='graph_menu'),
    blank,
    html.Div([
        html.A("Valor inicial: A"),
        dcc.Slider(
            id='slider-x-inicial',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_valores_iniciais_step,
            value=sd.x_inicial,
            marks=df.marks_valores_iniciais,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoA',
            updatemode='drag',
        ),
        html.A("Valor inicial: B"),
        dcc.Slider(
            id='slider-xb-inicial',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_valores_iniciais_step,
            value=sd.xb_inicial,
            marks=df.marks_valores_iniciais,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoB',
            updatemode='drag',
        ),
        html.A("Número de iterações"),
        dcc.Slider(
            id='slider-num-iteracoes',
            min=df.slider_iteracoes_min_value,
            max=df.slider_iteracoes_max_value,
            step=df.slider_iteracoes_step,
            value=sd.num_iteracoes,
            marks=df.marks_iteracoes,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-iteracoes',
            updatemode='drag',
        ),
    ], 
    className='graph_slider'),

], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'})

second_graph_layout = html.Div([
    blank,
    html.Div([
        dcc.Graph(
            id='grafico_2',
            style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'}
        ),
    ],
    className='graph'),

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
        ], className='checklist'),
    ],
    className='graph_menu'),
    blank,
    html.Div([
        html.A("Valor Inicial: A"),
        dcc.Slider(
            id='slider-x-inicial-2',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_valores_iniciais_step,
            value=sd.x_inicial,
            marks=df.marks_valores_iniciais,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoA',
            updatemode='drag',
        ),
        html.A("Valor Inicial: B"),
        dcc.Slider(
            id='slider-xb-inicial-2',
            min=df.slider_min_value,
            max=df.slider_max_value,
            step=df.slider_valores_iniciais_step,
            value=sd.xb_inicial,
            marks=df.marks_valores_iniciais,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-pontoB',
            updatemode='drag',
        ),
        html.A("Numero de iterações"),
        dcc.Slider(
            id='slider-num-iteracoes-2',
            min=df.slider_iteracoes_min_value,
            max=df.slider_iteracoes_max_value,
            step=df.slider_iteracoes_step,
            value=sd.num_iteracoes,
            marks=df.marks_iteracoes,
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider common-slider slider-iteracoes',
            updatemode='drag',
        ),
    ],
    className='graph_slider'),

], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto'})