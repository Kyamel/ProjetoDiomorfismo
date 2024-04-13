from graph_data import gerar_dados, gerar_dados_2, gerar_dados_user, go
import definicoes as df

def update_grafico(x2_inicial, xb2_inicial, num_iteracoes_2, selected_option='All'):
    dados = gerar_dados(x2_inicial, xb2_inicial, num_iteracoes_2)
    range = df.all_scale

    if selected_option == 'circle':
        # Remova todos os traços, exceto o do círculo
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
    figura_2 = go.Figure(data=dados, 
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
                        
    return figura_2

    
def update_grafico_2(x_inicial, xb_inicial, num_iteracoes, selected_option='All'):
    dados = gerar_dados_2(x_inicial, xb_inicial, num_iteracoes)
    range = df.all_scale

    if selected_option == 'circle':
        # Remova todos os traços, exceto o do círculo
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name'] or 'points_b' in trace['name']]
        range = df.circle_scale
    elif selected_option == 'circle_a':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name']]
        range = df.circle_scale
    elif selected_option == 'circle_b':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_b' in trace['name']]
        range = df.circle_scale
    elif selected_option == 'segments':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'segments_b' in trace['name'] or 'f1(x)' in trace['name']
                  or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
        range = df.segment_scale
    elif selected_option == 'segments_a':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'f1(x)' in trace['name']
                  or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
        range = df.segment_scale
    elif selected_option == 'segments_b':
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or
                  'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
        range = df.segment_scale
    elif selected_option == 'a':
        range = df.all_scale
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'points_a' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name']]
    elif selected_option == 'b':
        range = df.all_scale
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'points_b' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name']]
    elif selected_option == '2D':
        range = df.circle_scale
        dados = [trace for trace in dados if 'circle' in trace['name'] or "2D" in trace['name'] or 'arc' in trace['name']]

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

def update_grafico_u(x_inicial, xb_inicial, num_iteracoes, func, selected_option='All'):
    dados = gerar_dados_user(x_inicial, xb_inicial, num_iteracoes, func)
    range = df.all_scale

    if selected_option == 'circle':
        # Remova todos os traços, exceto o do círculo
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name'] or 'points_b' in trace['name']]
        range = df.circle_scale
    elif selected_option == 'circle_a':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_a' in trace['name']]
        range = df.circle_scale
    elif selected_option == 'circle_b':
        dados = [trace for trace in dados if 'circle' in trace['name'] or 'points_b' in trace['name']]
        range = df.circle_scale
    elif selected_option == 'segments':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'segments_b' in trace['name'] or 'f1(x)' in trace['name']
                  or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
        range = df.segment_scale
    elif selected_option == 'segments_a':
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'f1(x)' in trace['name']
                  or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
        range = df.segment_scale
    elif selected_option == 'segments_b':
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or
                  'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name']]
        range = df.segment_scale
    elif selected_option == 'a':
        range = df.all_scale
        dados = [trace for trace in dados if 'segments_a' in trace['name'] or 'points_a' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name']]
    elif selected_option == 'b':
        range = df.all_scale
        dados = [trace for trace in dados if 'segments_b' in trace['name'] or 'points_b' in trace['name'] or 'f1(x)' in trace['name'] or 'f2(x)' in trace['name'] or 'y=x' in trace['name'] or 'circle' in trace['name']]
    elif selected_option == '2D':
        range = df.circle_scale
        dados = [trace for trace in dados if 'circle' in trace['name'] or "2D" in trace['name']]

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

def update_sliders(auto_update_value, _, x, xb):

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

def update_sliders_2(auto_update_value, _, x, xb):
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
    
def update_sliders_u(auto_update_value, _, x, xb):
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