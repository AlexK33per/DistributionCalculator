import math as ma

# Función que elige entre las dos distribuciones


def chooseDistribution():
    option = -1
    while(option > 1 or option < 0):
        print("Pick a Distribution to generate a random number:")
        print("0: Poisson")
        print("1: Exponential")
        sel = input()
        option = int(sel)
    return option

# Función con el display para introducir la valor de 0 a 1.


def inputValue():
    print("Enter a valid number (from 0 to 1):")
    value = input()
    return value


# Función con el display para introducir la lambda


def inputLambda():
    print("Introduce una Lambda para la distribución")
    pick = input()
    return pick

# Funcion que ejecuta la distribución de Poisson


def poissonDistributionRandomGen(lambdaparam):
    print("todo")
# Función que ejecuta la distribución de Exponencial


def exponentialDistributionRandomGen(lambdaparam):
    logparam = inputValue()
    division = float(1 / float(lambdaparam))
    result = division * float(ma.log(float(logparam)))
    print(ma.fabs(result))

# Función que contiene la totalidad del programa


def main():
    lamb = inputLambda()
    exponentialDistributionRandomGen(float(lamb))


main()
