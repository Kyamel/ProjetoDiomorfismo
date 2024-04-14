import numpy as np

# >>>>>> VALORES INICIAIS <<<<<<
n = 0.5
x_inicial = 0.0
x2_inicial = 0.0
xu_inicial = 0.0
num_iteracoes = 0
num_iteracoes_2 = 0
num_iteracoes_u = 0

# >>>>>> ARC <<<<<<
arco_ativo = False
arco_tamanho = 1.0
arco2_ativo = False
arco2_tamanho = 1.0
arco_ativo_u = False
arco_tamanho_u = 1.0
if arco_ativo == True:
    xb_inicial = x_inicial + arco_tamanho
elif arco_ativo == False:
    xb_inicial = 0.0
if arco2_ativo == True:
    xb2_inicial = x2_inicial + arco2_tamanho
elif arco2_ativo == False:
    xb2_inicial = 0.0
if arco_ativo_u == True:
    xbu_inicial = xu_inicial + arco_tamanho_u
elif arco_ativo == False:
    xbu_inicial = 0.0

# >>>>>> SLIDERS <<<<<<
slider_max_value = 2*np.pi
slider_min_value = 0.0
slider_iteracoes_max_value = 32
slider_iteracoes_min_value = -32
slider_valores_iniciais_step = 0.001
slider_iteracoes_step = 1
marks_valores_iniciais = {i: str(i) for i in np.arange(0, 2*np.pi, 1)}
marks_iteracoes = {i: str(i) for i in range(-32, 33, 4)}

# >>>>> AUTO UPDATE SLIDERS <<<<<<
interval_step = 0.05
interval_step_2 = 0.05
interval_step_u = 0.05
interval_time = 100 #milisegundos
num_intervals = 0

# >>>>>> GRAPH SCALE <<<<<<
all_scale = [-1.5, 6.5]
circle_scale = [-1.1, 1.1]
segment_scale = [-0.5, 6.5]

# >>>>>> GRAPH ELEMENTS COLORS <<<<<<
col_value_A = 'red'
col_value_B = 'orange'
col_func = 'blue'
col_circle = 'gray'
col_identity = 'black'
col_iteracoes = 'purple'
col_hiperspace = 'green'
