from grafico import gerar_dados, gerar_dados_2, go
import dash
import numpy as np
import time
import definicoes as df

min_value = 0.0
max_value = 2 * np.pi

def update_grafico(x2_inicial, xb2_inicial, num_iteracoes_2, selected_option='All'):
    dados = gerar_dados_2(x2_inicial, xb2_inicial, num_iteracoes_2)

    if selected_option == 'circle':
        # Remova todos os traços, exceto o do círculo
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name'] or 'points_b' in trace['name']]
    elif selected_option == 'circle_a':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name']]
    elif selected_option == 'circle_b':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_b' in trace['name']]
    elif selected_option == 'segments':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'segments_b' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'segments_a':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'segments_b':
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'a':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'points_a' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'b':
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'points_b' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == '2D':
        dados = [trace for trace in dados if 'points_a' in trace['name'] or 'points_b' in trace['name'] or 'circle' in trace['name'] or "2D" in trace['name']]
    figura_2 = go.Figure(data=dados, layout=go.Layout(
        title="Gráfico 1",
        xaxis=dict(scaleanchor='y', scaleratio=1),
        yaxis=dict(scaleanchor='x', scaleratio=1)))  # vw significa viewport width
                        
    return figura_2

    
def update_grafico_2(x_inicial, xb_inicial, num_iteracoes, selected_option='All'):
    dados = gerar_dados(x_inicial, xb_inicial, num_iteracoes)

    if selected_option == 'circle':
        # Remova todos os traços, exceto o do círculo
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name'] or 'points_b' in trace['name']]
    elif selected_option == 'circle_a':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name']]
    elif selected_option == 'circle_b':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_b' in trace['name']]
    elif selected_option == 'segments':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'segments_b' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
    elif selected_option == 'segments_a':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
    elif selected_option == 'segments_b':
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
    elif selected_option == 'a':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'points_a' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name']]
    elif selected_option == 'b':
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'points_b' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name']]
    elif selected_option == '2D':
        dados = [trace for trace in dados if 'points_a' in trace['name'] or 'points_b' in trace ['name'] or 'circle' in trace['name'] or "2D" in trace['name']]

    figura = go.Figure(data=dados, layout=go.Layout(
        title="Gráfico 2",
        xaxis=dict(scaleanchor='y', scaleratio=1),
        yaxis=dict(scaleanchor='x', scaleratio=1)))  # vw significa viewport width
                        
    return figura

def update_sliders(auto_update_value, n_intervals, x, xb):

    if 'auto-update' in auto_update_value:
        # Lógica para atualizar gradualmente os valores dos sliders
        
        max_value = df.slider_max_value
        min_value = df.slider_min_value
        step = df.interval_step
        
        # Verifica se x atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if x + step > max_value:
            x = min_value + (x + step - max_value)
        else:
            x += step
        
        # Verifica se xb atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if xb + step > max_value:
            xb = min_value + (xb + step - max_value)
        else:
            xb += step

        return x, xb, False
    else:
        return x, xb, True


