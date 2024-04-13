# sistemasDunamicos.py
import numpy as np
import cameloMath as cm
from scipy.optimize import fsolve
import definicoes as df
import sympy as sp


# >>>>>> DEFINIÇÃO DE VALORES INICIAIS <<<<<<
n = df.n
x_inicial = df.x_inicial # Valor Inicial
x2_inicial = df.x2_inicial
xu_inicial = df.xu_inicial
arco_ativo = df.arco_ativo # False para não exibir arco, True para exibir
arco_tamanho = df.arco_tamanho

if arco_ativo == True:
    xb_inicial = x_inicial + arco_tamanho
    xb2_inicial = x2_inicial + arco_tamanho
    xbu_inicial = xu_inicial + arco_tamanho
elif arco_ativo == False:
    xb_inicial = 0.0 # Valor inicial de B
    xb2_inicial = 0.0
    xbu_inicial = 0.0
    
num_iteracoes = df.num_iteracoes
num_iteracoes_2 = df.num_iteracoes_2
num_iteracoes_u = df.num_intervals_u

# >>>>>> DEFINIÇÃO DAS FUNÇÕES MATEMÁTICAS <<<<<<
def f1(x):
    return x + np.pi + n * np.sin((2*x))
def f2(x):
    return x + n * np.sin((2*(x - 2*(np.pi)))) - np.pi
def f3(x):
    return x + n * np.sin(x)

def string_to_function(string):
    x = sp.symbols('x')  # Define a variável simbólica x
    expr = sp.sympify(string)  # Converte a string em uma expressão sympy
    func = sp.lambdify(x, expr, modules=['numpy'])  # Converte a expressão sympy em uma função Python
    return func

def UserFunc(func):
    return func

def CalculateUserFunc(x, userFunc):
    return userFunc(x)

def inverse_UserFunc(y, func):
    # Defina a função a ser resolvida: f(x) - y = 0
    equation = lambda x: CalculateUserFunc(x, func) - y 
    
    # Adivinhe um valor inicial para a solução
    guess = 0.0
    
    # Use fsolve para encontrar a solução
    solution = fsolve(equation, guess)
    
    return solution[0]  # Retorna a solução encontrada


def inverse_f3(y):
    # Defina a função a ser resolvida: f(x) - y = 0
    equation = lambda x: f3(x) - y
    
    # Adivinhe um valor inicial para a solução
    guess = 0.0
    
    # Use fsolve para encontrar a solução
    solution = fsolve(equation, guess)
    
    return solution[0]  # Retorna a solução encontrada

def inverse_f2(y):
    equation = lambda x: f2(x) - y
    guess = 0.0
    solution = fsolve(equation, guess)
    return solution[0]

def inverse_f1(y):
    equation = lambda x: f1(x) - y
    guess = 0.0
    solution = fsolve(equation, guess)
    return solution[0]

def iteracoes(x, numero_iteracoes, f1, f2, str):
    inputs = np.array([x])
    outputs = np.array([0])
    labels = []
    xc = np.array([np.cos(x)])
    yc = np.array([np.sin(x)])
    labels.append(f'Ponto 0')  # Adiciona rótulo ao ponto
    
    print()
    print("valor inicial do", str,'é =', x )
    
    for i in range(abs(numero_iteracoes)):
        inputs = np.append(inputs, x)
        
        if x < np.pi:
            x = f1(x)
            xc = np.append(xc, np.cos(float(x)))
            yc = np.append(yc, np.sin(float(x)))
        elif x >= np.pi:
            x = f2(x)
            xc = np.append(xc, np.cos(float(x)))
            yc = np.append(yc, np.sin(float(x)))
        
        outputs = np.append(outputs, x)
        inputs = np.append(inputs, x)
        outputs = np.append(outputs, x)
        labels.append(f'Ponto {i+1}')  # Adiciona rótulo ao ponto
    
    inputs = inputs[:-1]
    outputs = outputs[:-1]

    print(f"valor da {numero_iteracoes}ª iteracao do {str} é = {x}", end="\n")

    return inputs, outputs, xc, yc, labels

def hiperespaco(arc, str):

    alpha = np.empty(len(arc))
    bheta = np.empty(len(arc))
    angulos_absolute = np.empty(len(arc))

    # arcsin funciona enquanto o angulo for menor que 90° e o Ponto A estiver na origem (1,0)
    # arco que começa do ponto A e termina no Ponto B pelo sentido anti_horário
    for i, arc_instance in enumerate(arc):
        alpha[i] = arc_instance.begin_angle()
        bheta[i] = arc_instance.end_angle()
        angulos_absolute[i] = arc_instance.angle_in_between()

    # Valores em radianos
    comprimento_arco = (angulos_absolute)

    pontos_medio_x = np.cos((angulos_absolute / 2)+alpha)
    pontos_medio_y = np.sin((angulos_absolute / 2)+alpha)
    
    pontos_hiperespaco_x = (1 - (comprimento_arco) / (np.pi * 2)) * pontos_medio_x
    pontos_hiperespaco_y = (1 - (comprimento_arco) / (np.pi * 2)) * pontos_medio_y

    pontos_hiperespaco = cm.MultiPoint(pontos_hiperespaco_x, pontos_hiperespaco_y)

    print("valores no hiperespaco dos Pontos", str, 'são =')
    print(pontos_hiperespaco)

    return pontos_hiperespaco
