import math as ma
import numpy as np
import pandas as excel
from prettytable import PrettyTable

# Función que elige entre las dos distribuciones

def chooseDistribution():
    option = -1
    print("Introduce un número para seleccionar la distribución generadora de un número aleatorio:")
    print("0: Poisson")
    print("1: Exponencial")
    print("Cualquier otro número cierra el programa")
    sel = input()
    option = int(sel)
    return option

# Función con el display para introducir la valor de 0 a 1.

def inputValue():
    print("Enter a valid number (from 0 to 1):")
    value = input()
    return value


# Función con el display para introducir la lambda

def inputParam(value):
    if(value == 0):
        print("Introduce una Lambda para la distribución de Poisson:")
        pick = input()
    elif (value == 1):
        print("Introduce una Beta para la distribución Exponencial:")
        pick = input()
    return pick

# Funcion que ejecuta la distribución de Poisson

def poissonDistributionRandomGen(lambdaparam):
    sol = list()
    u = 0
    while(u < 100):
        a = pow(ma.e, -float(lambdaparam))
        b = float(1)
        n = int(0)
        np.random.seed()
        arr = np.random.uniform(0, 1, 100)
        i = int(0)
        while(b >= a and i < 100):
            b = arr[i] * b
            i = i + 1
            n = n + 1
        sol.append(n)    
        u = u + 1
    return sol

# Función que ejecuta la distribución de Exponencial

def exponentialDistributionRandomGen(betaparam):
    sol = list()
    i = 0
    while(i < 100):
        arr = np.random.uniform(0, 1, 1)
        logparam = arr[0]
        division = float(1 / float(betaparam))
        result = division * float(ma.log(float(logparam)))
        sol.append(abs(result))
        i = i + 1
    return sol

# Función que contiene la totalidad del programa

def main():
    val = int(chooseDistribution())
    exp = list()
    poisson = list()
    while(val > -1 and val < 2):
        if val == 0:
            lamb = inputParam(val)
            print("El resultado es:")
            poisson = poissonDistributionRandomGen(lamb)
            tabulate([])
        elif val == 1:
            beta = inputParam(val)
            print("El resultado es:")
            exp = exponentialDistributionRandomGen(beta)
            tabulate(list(range(100)), beta, headers = ["Xi", "Número generado"])
    data = excel.DataFrame({"Poisson":poisson, "Exponencial":exp})
    data.to_excel("Datos_Generados.xlsx", index = False)

main()

