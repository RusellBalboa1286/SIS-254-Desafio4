import math as m

# Definir la función logarítmica
def funcion(x):
    return m.log(x)

# Definir las primeras derivadas
def derivada1(x):
    return 1/x

def derivada2(x):
    return -1/x**2

def derivada3(x):
    return 2/x**3

def derivada4(x):
    return -6/x**4

def derivada5(x):
    return 24/x**5

"""PROGRAMA PRINCIPAL"""

print("Parámetros iniciales")
x_inicial = 1
x_final = 2.5

valor_inicial = funcion(x_inicial)

print("x_inicial =", x_inicial)
print("x_final =", x_final)

print("f(x_inicial) = ", valor_inicial)
print("f(x_final) = ?")

# Calcular el paso (h)
diferencia = x_final - x_inicial
print("h =", diferencia)

# SERIE DE TAYLOR
resultado_taylor = float(valor_inicial)

# Almacenar las derivadas evaluadas en x_inicial
derivadas = [derivada1(x_inicial), derivada2(x_inicial), derivada3(x_inicial), derivada4(x_inicial), derivada5(x_inicial)]

print()
print("#", "\t", "|", "f(x)", "\t", "|", "Término Rn")
print("-" * 30)
for i in range(5):
    termino_residual = derivadas[i] * (diferencia**(i+1) / m.factorial(i+1))
    print(i, "\t", "|", resultado_taylor, "\t", "|", termino_residual)
    resultado_taylor += termino_residual
