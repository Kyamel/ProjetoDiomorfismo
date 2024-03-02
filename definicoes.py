import numpy as np

# >>>>>> DEFINIÇÃO DE VALORES INICIAIS <<<<<<
n = 0.5
x_inicial = 0.0 # Valor Inicial
x2_inicial = 0.0
arco_ativo = False # False para não exibir arco, True para exibir
arco_tamanho = 1.0
    
num_iteracoes = 0
num_iteracoes_2 = 0

slider_max_value = 2*np.pi
slider_min_value = 0.0
slider_iteracoes_max_value = 26
slider_iteracoes_min_value = -25
slider_step = 0.01

interval_step = 0.1
interval_time = 100 #milisegundos
num_intervals = 0
iteracoes_step = 1