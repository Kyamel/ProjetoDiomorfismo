import sistemasDinamicos as sd
import numpy as np
import plotly.graph_objects as go
import cameloMath as cm
import definitions as df
from typing import Tuple

# Função para gerar os dados do gráfico
def gerar_dados_2(x_inicial: float,
                xb_inicial: float, 
                num_iteracoes: int) -> Tuple[go.Scatter, ...]:
    
    X1 = np.linspace(0.0, np.pi, 50, endpoint=True)
    X2 = np.linspace(np.pi, 2 * np.pi, 50, endpoint=True)
    X = np.linspace(0.0, 2 * np.pi, 100, endpoint=True)

    Y1 = sd.f1(X1)
    Y2 = sd.f2(X2)
    Y_inv1 = np.empty_like(Y1)
    Y_inv2 = np.empty_like(Y2)

    for i, x_value in enumerate(X1):
        Y_inv1[i] = sd.inverse_f1(x_value)
    for i, x_value in enumerate(X2):
        Y_inv2[i] = sd.inverse_f2(x_value)

    if num_iteracoes >= 0:
        trace_f1 = go.Scatter(x=X1, y=Y1, name='f1(x)', line=dict(color=df.col_func))
        trace_f2 = go.Scatter(x=X2, y=Y2, name='f2(x)', line=dict(color=df.col_func))
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x_inicial, num_iteracoes, sd.f1, sd.f2, 'Ponto A (grafico 2)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb_inicial, num_iteracoes, sd.f1, sd.f2, 'Ponto B (grafico 2)')
    else:
        trace_f1 = go.Scatter(x=X1, y=Y_inv1, name='f1_inv(x)', line=dict(color=df.col_func))
        trace_f2 = go.Scatter(x=X2, y=Y_inv2, name='f2_inv(x)', line=dict(color=df.col_func))
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x_inicial, num_iteracoes, sd.inverse_f1, sd.inverse_f2, 'Ponto A (grafico 2)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb_inicial, num_iteracoes, sd.inverse_f1, sd.inverse_f2, 'Ponto B (grafico 2)')

    trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b, trace_points_a, trace_points_b, trace_hiperespaco = makeTraces(X, labels, inputs_a, inputs_b, outputs_a, outputs_b, xc_a, xc_b, yc_a, yc_b, '(Grafico 2)')
    #Draw arc
    if df.arco2_ativo:
        draw_arc = np.linspace(x_inicial, xb_inicial, 1000, endpoint=True)
        trace_arc = go.Scatter(x=np.cos(draw_arc), y=np.sin(draw_arc),
                                mode='lines', name='arc', marker=dict(color=df.col_value_A))
    else:
        trace_arc = go.Scatter(x=[], y=[], name='arc')

    return [trace_f1, trace_f2, trace_yx, trace_circle, trace_segmentos_a,
             trace_segmentos_b, trace_points_a, trace_points_b, trace_hiperespaco, trace_arc]

def gerar_dados(x2_inicial: float, xb2_inicial: float, num_iteracoes_2: int) ->  Tuple[go.Scatter,...]:
    X = np.linspace(0.0, 2 * np.pi, 100, endpoint=True)
    Y = sd.f3(X)
    Y_inv = np.empty_like(Y)
    for i, x_value in enumerate(X):
        Y_inv[i] = sd.inverse_f3(x_value)

    if num_iteracoes_2 >= 0:
        trace_f1 = go.Scatter(x=X, y=Y, name='f1(x)', line=dict(color=df.col_func))
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x2_inicial, num_iteracoes_2, sd.f3, sd.f3, 'Ponto A (grafico 1)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb2_inicial, num_iteracoes_2, sd.f3, sd.f3, 'Ponto B (grafico 1)')
    else:
        trace_f1 = go.Scatter(x=X, y=Y_inv, name='f1_inv(x)', line=dict(color=df.col_func))
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x2_inicial, num_iteracoes_2, sd.inverse_f3, sd.inverse_f3, 'Ponto A (grafico 1)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb2_inicial, num_iteracoes_2, sd.inverse_f3, sd.inverse_f3, 'Ponto B (grafico 1)')

    trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b, trace_points_a, trace_points_b, trace_hiperespaco = makeTraces(X, labels, inputs_a, inputs_b, outputs_a, outputs_b, xc_a, xc_b, yc_a, yc_b, '(Grafico 1)')
    # Draw Arc
    if df.arco_ativo:
        draw_arc = np.linspace(x2_inicial, xb2_inicial, 1000, endpoint=True)
        trace_arc = go.Scatter(x=np.cos(draw_arc), y=np.sin(draw_arc),
                                mode='lines', name='arc', marker=dict(color=df.col_value_A))
    else:
        trace_arc = go.Scatter(x=[], y=[], name='arc')

    return [trace_f1, trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b,
             trace_points_a, trace_points_b, trace_hiperespaco, trace_arc]

def gerar_dados_user(xu_inicial: float,
                    xbu_inicial: float,
                    num_iteracoes_u: int,
                    func) ->  Tuple[go.Scatter, ...]:
    
    X = np.linspace(0.0, 2 * np.pi, 100, endpoint=True)
    Y = sd.CalculateUserFunc(X, func)
    Y_inv = np.empty_like(Y)
    for i, x_value in enumerate(X):
        Y_inv[i] = sd.inverse_UserFunc(x_value, func)

    if num_iteracoes_u >= 0:
        trace_f1 = go.Scatter(x=X, y=Y, name='f1(x)')
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(xu_inicial, num_iteracoes_u, sd.UserFunc(func), sd.UserFunc(func), 'Ponto A (grafico user)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xbu_inicial, num_iteracoes_u, sd.UserFunc(func), sd.UserFunc(func), 'Ponto B (grafico user)')
    else:
        trace_f1 = go.Scatter(x=X, y=Y_inv, name='f1_inv(x)')
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(xu_inicial, num_iteracoes_u, sd.inverse_UserFunc(func, 1), sd.inverse_UserFunc(func, 1), 'Ponto A (grafico user)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xbu_inicial, num_iteracoes_u, sd.inverse_UserFunc(func, 1), sd.inverse_UserFunc(func, 1), 'Ponto B (grafico user)')

    trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b, trace_points_a, trace_points_b, trace_hiperespaco = makeTraces(X, labels, inputs_a, inputs_b, outputs_a, outputs_b, xc_a, xc_b, yc_a, yc_b, '(Grafico user)')
    # Draw Arc
    if df.arco_ativo_u:
        draw_arc = np.linspace(xu_inicial, xbu_inicial, 1000, endpoint=True)
        trace_arc = go.Scatter(x=np.cos(draw_arc), y=np.sin(draw_arc),
                                mode='lines', name='arc', marker=dict(color=df.col_value_A))
    else:
        trace_arc = go.Scatter(x=[], y=[], name='arc')

    return [trace_f1, trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b,
             trace_points_a, trace_points_b, trace_hiperespaco, trace_arc]

def makeTraces(X: np.ndarray, labels: list[str], 
               inputs_a: np.ndarray, inputs_b: np.ndarray, 
               outputs_a: np.ndarray, outputs_b: np.ndarray, 
               xc_a: np.ndarray, xc_b: np.ndarray, 
               yc_a: np.ndarray, yc_b: np.ndarray, 
               str: str = 'graph') -> Tuple[go.Scatter, ...]:
    
    trace_yx = go.Scatter(x=X, y=X, name='y=x', line=dict(color=df.col_identity))
    trace_circle = go.Scatter(x=np.cos(X), y=np.sin(X), name='circle', line=dict(color=df.col_circle))

    labels_aux_2 = labels.copy()
    if labels_aux_2:
        labels_aux_2.pop(0)
    labels_aux = []
    for i, labels_aux_2 in enumerate(labels_aux_2):
        labels_aux.extend(['', labels_aux_2])
    if labels_aux:
        labels_aux[0] = 'Ponto 0'

    trace_segmentos_a = go.Scatter(x=inputs_a, y=outputs_a, mode='lines+markers', name='segments_a', line=dict(color=df.col_value_A), text=labels_aux)
    trace_segmentos_b = go.Scatter(x=inputs_b, y=outputs_b, mode='lines+markers', name='segments_b', line=dict(color=df.col_value_B), text=labels_aux)
    trace_points_a = go.Scatter(x=xc_a, y=yc_a, mode='markers', name='points_a', marker=dict(color=df.col_value_A), text=labels)
    trace_points_b = go.Scatter(x=xc_b, y=yc_b, mode='markers', name='points_b', marker=dict(color=df.col_value_B), text=labels)

    xm, ym = np.zeros_like(xc_a), np.zeros_like(yc_a)
    # Criar arrays para begin_point, center_point, e end_point
    begin_point = np.array([cm.Point(x, y) for x, y in zip(xc_a, yc_a)])
    center_point = np.array([cm.Point(x, y) for x, y in zip(xm, ym)])
    end_point = np.array([cm.Point(x, y) for x, y in zip(xc_b, yc_b)])

    # Criar array para arc
    arc = np.array([cm.ArcOfCircle(b, c, e) for b, c, e in zip(begin_point, center_point, end_point)])
    hiperespaco = sd.hiperespaco(arc, string=str)

    trace_hiperespaco = go.Scatter(x=hiperespaco.x, y=hiperespaco.y, mode='markers',name='2D', marker=dict(color=df.col_hiperspace), text=labels)

    return trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b, trace_points_a, trace_points_b, trace_hiperespaco
