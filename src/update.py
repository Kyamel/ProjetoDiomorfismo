from graph_data import gerar_dados, gerar_dados_2, gerar_dados_user, go
import definitions as df

def selectTraces(dados: tuple, selected_option: str) -> tuple[tuple, tuple]:
    range = df.all_scale
    if selected_option == 'circle':
        range = df.circle_scale
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name'] or 'points_b' in trace['name']]
    elif selected_option == 'circle_a':
        range = df.circle_scale
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name']]
    elif selected_option == 'circle_b':
        range = df.circle_scale
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_b' in trace['name']]
    elif selected_option == 'segments':
        range = df.segment_scale
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'segments_b' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'segments_a':
        range = df.segment_scale
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'segments_b':
        range = df.segment_scale
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'a':
        range = df.all_scale
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'points_a' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == 'b':
        range = df.all_scale
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'points_b' in trace['name'] or 'f1(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name'] or 'f1_inv(x)' in trace['name']]
    elif selected_option == '2D':
        range = df.circle_scale
        dados = [trace for trace in dados if 'circle' in trace['name'] or "2D" in trace['name'] or 'arc' in trace['name']]
    return dados, range

def update_grafico(x2_inicial: float, xb2_inicial: float, num_iteracoes_2: int, selected_option='All') -> go.Figure:
    dados = gerar_dados(x2_inicial, xb2_inicial, num_iteracoes_2)
    dados, range = selectTraces(dados, selected_option)  
    figura = go.Figure(data=dados, 
        layout=go.Layout(
            title="Gráfico 1",
            xaxis=dict(
                range = range,
                scaleratio=1,
                scaleanchor='y',
            ),
            yaxis=dict(
                range = range,
                scaleratio=1,
                scaleanchor='x',
            ),
            margin=dict(l=0, r=0, t=40, b=40),
        )
    )                     
    return figura

    
def update_grafico_2(x_inicial: float, xb_inicial: float, num_iteracoes: int, selected_option='All') -> go.Figure:
    dados = gerar_dados_2(x_inicial, xb_inicial, num_iteracoes)
    dados, range = selectTraces(dados, selected_option)
    figura = go.Figure(data=dados, 
        layout=go.Layout(
            
            title="Gráfico 2",
            xaxis=dict(
                range = range,
                scaleratio=1,
                scaleanchor='y',
            ),
            yaxis=dict(
                range = range,
                scaleratio=1,
                scaleanchor='x',
            ),
            margin=dict(l=0, r=0, t=40, b=40),
        )
    )                    
    return figura

def update_grafico_u(x_inicial: float, xb_inicial: float, num_iteracoes: float, func, selected_option='All') -> go.Figure:
    dados = gerar_dados_user(x_inicial, xb_inicial, num_iteracoes, func)
    dados, range = selectTraces(dados, selected_option)
    figura = go.Figure(data=dados, 
        layout=go.Layout(
            
            title="Gráfico User",
            xaxis=dict(
                range = range,
                scaleratio=1,
                scaleanchor='y',
            ),
            yaxis=dict(
                range = range,
                scaleratio=1,
                scaleanchor='x',
            ),
            margin=dict(l=0, r=0, t=40, b=40),
        )
    )                    
    return figura

def update_sliders(auto_update_value: str, _, x: float, xb: float) -> tuple[float, float, bool]:

    if 'auto-update' in auto_update_value:
        # Lógica para atualizar gradualmente os valores dos sliders
        max_value = df.slider_max_value
        min_value = df.slider_min_value
        step = df.interval_step
        # Verifica se x atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if x + step > max_value:
            x = min_value
        elif x + step < min_value:
            x = max_value
        else:
            x += step
        # Verifica se xb atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if xb + step > max_value:
            xb = min_value
        elif xb + step < min_value:
            xb = max_value
        else:
            xb += step
        return x, xb, False
    else:
        return x, xb, True

def update_sliders_2(auto_update_value: str, _, x: float, xb: float) -> tuple[float, float, bool]:
    if 'auto-update' in auto_update_value:
        # Lógica para atualizar gradualmente os valores dos sliders
        max_value = df.slider_max_value
        min_value = df.slider_min_value
        step = df.interval_step_2
        # Verifica se x atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if x + step > max_value:
            x = min_value
        elif x + step < min_value:
            x = max_value
        else:
            x += step
        # Verifica se xb atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if xb + step > max_value:
            xb = min_value
        elif xb + step < min_value:
            xb = max_value
        else:
            xb += step
        return x, xb, False
    else:
        return x, xb, True
    
def update_sliders_u(auto_update_value: str, _, x: float, xb: float) -> tuple[float, float, bool]:
    if 'auto-update' in auto_update_value:
        # Lógica para atualizar gradualmente os valores dos sliders
        max_value = df.slider_max_value
        min_value = df.slider_min_value
        step = df.interval_step_2
        # Verifica se x atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if x + step > max_value:
            x = min_value
        elif x + step < min_value:
            x = max_value
        else:
            x += step
        # Verifica se xb atingiu o valor máximo e ajusta para o mínimo com a mesma quantidade de passos
        if xb + step > max_value:
            xb = min_value
        elif xb + step < min_value:
            xb = max_value
        else:
            xb += step
        return x, xb, False
    else:
        return x, xb, True