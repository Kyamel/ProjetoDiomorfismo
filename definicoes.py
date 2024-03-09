import numpy as np

# >>>>>> VALORES INICIAIS <<<<<<
n = 0.5
x_inicial = 0.0 # Valor Inicial
x2_inicial = 0.0
num_iteracoes = 0
num_iteracoes_2 = 0

# >>>>>> NÂO IMPLEMENTADO <<<<<<
arco_ativo = False # False para não exibir arco, True para exibir
arco_tamanho = 1.0   

# >>>>>> SLIDERS <<<<<<
slider_max_value = 2*np.pi
slider_min_value = 0.0
slider_iteracoes_max_value = 26
slider_iteracoes_min_value = -25
slider_step = 0.01
slider_iteracoes_step = 1

# >>>>> AUTO UPDATE SLIDER <<<<<<
interval_step = 0.05
interval_step_2 = 0.05
interval_time = 100 #milisegundos
num_intervals = 0

# >>>>>> GRAPH SCALE <<<<<<
all_scale = [-1.5, 6.5]
circle_scale = [-1.1, 1.1]
segment_scale = [-0.5, 6.5]
