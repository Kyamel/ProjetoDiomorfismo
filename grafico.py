import sistemasDinamicos as sd
import numpy as np
import plotly.graph_objects as go
import cameloMath as cm

# Função para gerar os dados do gráfico
def gerar_dados(x_inicial, xb_inicial, num_iteracoes):
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
    
    trace_yx = go.Scatter(x=X, y=X, name='y=x')
    trace_circle = go.Scatter(x=np.cos(X), y=np.sin(X), name='circle')

    if num_iteracoes >= 0:
        trace_f1 = go.Scatter(x=X1, y=Y1, name='f1(x)')
        trace_f2 = go.Scatter(x=X2, y=Y2, name='f2(x)')
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x_inicial, num_iteracoes, sd.f1, sd.f2, 'Ponto A (gráfico 1)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb_inicial, num_iteracoes, sd.f1, sd.f2, 'Ponto B (gráfico 1)')
    else:
        trace_f1 = go.Scatter(x=X1, y=Y_inv1, name='f1(x)')
        trace_f2 = go.Scatter(x=X2, y=Y_inv2, name='f2(x)')
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x_inicial, num_iteracoes, sd.inverse_f1, sd.inverse_f2, 'Ponto A (gráfico 1)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb_inicial, num_iteracoes, sd.inverse_f1, sd.inverse_f2, 'Ponto B (gráfico 1)')

    labels_aux_2 = labels.copy()
    if labels_aux_2:
        labels_aux_2.pop(0)

    labels_aux = []
    for i, labels_aux_2 in enumerate(labels_aux_2):
        labels_aux.extend(['', labels_aux_2])
    
    if labels_aux:
        labels_aux[0] = 'Ponto 0'

    trace_segmentos_a = go.Scatter(x=inputs_a, y=outputs_a, mode='lines+markers', name='segments_a', line=dict(color='orange'), text=labels_aux)
    trace_segmentos_b = go.Scatter(x=inputs_b, y=outputs_b, mode='lines+markers', name='segments_b', line=dict(color='blue'), text=labels_aux)
    trace_points_a = go.Scatter(x=xc_a, y=yc_a, mode='markers', name='points_a', marker=dict(color='orange'), text=labels)
    trace_points_b = go.Scatter(x=xc_b, y=yc_b, mode='markers', name='points_b', marker=dict(color='blue'), text=labels)

    xm, ym = np.zeros_like(xc_a), np.zeros_like(yc_a)
    # Criar arrays para begin_point, center_point, e end_point
    begin_point = np.array([cm.Point(x, y) for x, y in zip(xc_a, yc_a)])
    center_point = np.array([cm.Point(x, y) for x, y in zip(xm, ym)])
    end_point = np.array([cm.Point(x, y) for x, y in zip(xc_b, yc_b)])

    # Criar array para arc
    arc = np.array([cm.ArcOfCircle(b, c, e) for b, c, e in zip(begin_point, center_point, end_point)])

    hiperespaco = sd.hiperespaco(arc, str='(gráfico 1)')
    
    trace_hiperespaco = go.Scatter(x=hiperespaco.x, y=hiperespaco.y, mode='markers', name='2D', marker=dict(color='green'), text=labels)

    return [trace_f1, trace_f2, trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b, trace_points_a, trace_points_b, trace_hiperespaco]

def gerar_dados_2(x2_inicial, xb2_inicial, num_iteracoes_2):
    X = np.linspace(0.0, 2 * np.pi, 100, endpoint=True)
    Y = sd.f3(X)
    Y_inv = np.empty_like(Y)

    for i, x_value in enumerate(X):
        Y_inv[i] = sd.inverse_f3(x_value)

    trace_yx = go.Scatter(x=X, y=X, name='y=x')
    trace_circle = go.Scatter(x=np.cos(X), y=np.sin(X), name='circle')

    if num_iteracoes_2 >= 0:
        trace_f1 = go.Scatter(x=X, y=Y, name='f1(x)')
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x2_inicial, num_iteracoes_2, sd.f3, sd.f3, 'Ponto A (gráfico 2)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb2_inicial, num_iteracoes_2, sd.f3, sd.f3, 'Ponto B (gráfico 2)')
    else:
        trace_f1 = go.Scatter(x=X, y=Y_inv, name='f1_inv(x)')
        inputs_a, outputs_a, xc_a, yc_a, labels = sd.iteracoes(x2_inicial, num_iteracoes_2, sd.inverse_f3, sd.inverse_f3, 'Ponto A (gráfico 2)')
        inputs_b, outputs_b, xc_b, yc_b, labels = sd.iteracoes(xb2_inicial, num_iteracoes_2, sd.inverse_f3, sd.inverse_f3, 'Ponto B (gráfico 2)')

    labels_aux_2 = labels.copy()
    if labels_aux_2:
        labels_aux_2.pop(0)

    labels_aux = []
    for i, labels_aux_2 in enumerate(labels_aux_2):
        labels_aux.extend(['', labels_aux_2])
    
    if labels_aux:
        labels_aux[0] = 'Ponto 0'

    trace_segmentos_a = go.Scatter(x=inputs_a, y=outputs_a, mode='lines+markers', name='segments_a', line=dict(color='orange'), text=labels_aux)
    trace_segmentos_b = go.Scatter(x=inputs_b, y=outputs_b, mode='lines+markers', name='segments_b', line=dict(color='blue'), text=labels_aux)
    trace_points_a = go.Scatter(x=xc_a, y=yc_a, mode='markers', name='points_a', marker=dict(color='orange'), text=labels)
    trace_points_b = go.Scatter(x=xc_b, y=yc_b, mode='markers', name='points_b', marker=dict(color='blue'), text=labels)

    xm, ym = np.zeros_like(xc_a), np.zeros_like(yc_a)
    # Criar arrays para begin_point, center_point, e end_point
    begin_point = np.array([cm.Point(x, y) for x, y in zip(xc_a, yc_a)])
    center_point = np.array([cm.Point(x, y) for x, y in zip(xm, ym)])
    end_point = np.array([cm.Point(x, y) for x, y in zip(xc_b, yc_b)])

    # Criar array para arc
    arc = np.array([cm.ArcOfCircle(b, c, e) for b, c, e in zip(begin_point, center_point, end_point)])

    hiperespaco = sd.hiperespaco(arc, str='(gráfico 2)')

    trace_hiperespaco = go.Scatter(x=hiperespaco.x, y=hiperespaco.y, mode='markers', name='2D', marker=dict(color='green'), text=labels)

    return [trace_f1, trace_yx, trace_circle, trace_segmentos_a, trace_segmentos_b, trace_points_a, trace_points_b, trace_hiperespaco]
