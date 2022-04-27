# Función que elige entre las dos distribuciones

def chooseDistribution():
    option = -1
    while(option > 1 or option < 0):    
        print("Pick Poisson or Exponential distribution")
        print("0: Poisson")
        print("1: Exponential")
        sel = input()
        option = int(sel)
    return option

# Funcion que ejecuta la distribución de Poisson

def poissonDistribution():
    print("To-Do")


# Función que ejecuta la distribución de Exponencial

def exponentialDistribution():
    print("To-Do")

# Función que contiene la totalidad del programa

def main():
    val = int(chooseDistribution())
    poissonDistribution() if val == 0 else exponentialDistribution()

main()
