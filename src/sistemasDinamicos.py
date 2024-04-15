# sistemasDunamicos.py
import numpy as np
import cameloMath as cm
from scipy.optimize import fsolve
import definitions as df
import sympy as sp
from typing import Callable


# >>>>>> DEFINIÇÃO DE VALORES INICIAIS <<<<<<
n = df.n

# >>>>>> DEFINIÇÃO DAS FUNÇÕES MATEMÁTICAS <<<<<<
def f1(x: float) -> float:
    return x + np.pi + n * np.sin((2*x))
def f2(x: float) -> float:
    return x + n * np.sin((2*(x - 2*(np.pi)))) - np.pi
def f3(x: float) -> float:
    return x + n * np.sin(x)

def string_to_function(string: str) -> Callable[[float], float]:
    x = sp.symbols('x')  # Define a variável simbólica x
    expr = sp.sympify(string)  # Converte a string em uma expressão sympy
    func = sp.lambdify(x, expr, modules=['numpy'])  # Converte a expressão sympy em uma função Python
    return func

def UserFunc(func: Callable[[float], float]) -> Callable[[float], float]:
    return func

def CalculateUserFunc(x: float, userFunc: Callable[[float], float]) -> float:
    return userFunc(x)

def inverse_UserFunc(y: float, func) -> float:
    # Defina a função a ser resolvida: f(x) - y = 0
    equation = lambda x: CalculateUserFunc(x, func) - y 
    
    # Adivinhe um valor inicial para a solução
    guess = 0.0
    
    # Use fsolve para encontrar a solução
    solution = fsolve(equation, guess)
    
    return solution[0]  # Retorna a solução encontrada


def inverse_f3(y: float) -> float:
    # Defina a função a ser resolvida: f(x) - y = 0
    equation = lambda x: f3(x) - y
    
    # Adivinhe um valor inicial para a solução
    guess = 0.0
    
    # Use fsolve para encontrar a solução
    solution = fsolve(equation, guess)
    
    return solution[0]  # Retorna a solução encontrada

def inverse_f2(y: float) -> float:
    equation = lambda x: f2(x) - y
    guess = 0.0
    solution = fsolve(equation, guess)
    #return (solution[0] + 2 * np.pi) % (2 * np.pi)
    return solution[0] - 2*np.pi

def inverse_f1(y: float) -> float:
    equation = lambda x: f1(x) - y
    guess = 0.0
    solution = fsolve(equation, guess)
    #return (solution[0] + 2 * np.pi) % (2 * np.pi)
    return solution[0] + 2*np.pi

def iteracoes(x: float,
            numero_iteracoes: int,
            f1: Callable[[float], float], f2: Callable[[float], float],
            string: list[str]) -> tuple[np.array, np.array, np.array, np.array, list[str]]:
    
    inputs = np.array([x])
    outputs = np.array([0])
    labels = []
    xc = np.array([np.cos(x)])
    yc = np.array([np.sin(x)])
    labels.append(f'Ponto 0')  # Adiciona rótulo ao ponto
    
    with open('log.txt', 'a') as file:
        file.write("valor inicial do " + string + " : " + str(x) + "\n")

    for i in range(abs(numero_iteracoes)):
        inputs = np.append(inputs, x)
        
        if x < np.pi:
            x = f1(x)
            xc = np.append(xc, np.cos(x))
            yc = np.append(yc, np.sin(x))
        elif x >= np.pi:
            x = f2(x)
            xc = np.append(xc, np.cos(x))
            yc = np.append(yc, np.sin(x))
        
        outputs = np.append(outputs, x)
        inputs = np.append(inputs, x)
        outputs = np.append(outputs, x)
        labels.append(f'Ponto {i+1}')  # Adiciona rótulo ao ponto
    
    inputs = inputs[:-1]
    outputs = outputs[:-1]

    with open('log.txt', 'a') as file:
        file.write(f"valor da {numero_iteracoes} iteracao do {string}: {x}\n")

    return inputs, outputs, xc, yc, labels

def hiperespaco(arc: cm.ArcOfCircle, string: list[str]) -> cm.MultiPoint:

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

    with open('log.txt', 'a') as file:
        file.write(f"valores no hiperespaco dos Pontos {string}: {pontos_hiperespaco}\n")
        file.write(50 * '#' + '\n')

    return pontos_hiperespaco
