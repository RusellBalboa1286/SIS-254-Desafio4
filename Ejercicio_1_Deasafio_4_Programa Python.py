import sympy as sp
import math as m

# Definir la variable simbólica
x = sp.symbols('x')

"""PARAMETROS"""
# Definir la función simbólica
func = 25*x**3 - 6*x**2 + 7*x - 88
x_inicial = 1  # Punto inicial
x_final = 3  # Punto final
max_iter = 4  # Número de iteraciones (orden máximo)
"""-------------"""

# Calcular las derivadas de manera automática
def obtener_derivadas(expr, var, max_orden):
    lista_derivadas = []
    derivada_temp = expr
    for i in range(max_orden + 1):
        lista_derivadas.append(sp.diff(derivada_temp, var))
        derivada_temp = lista_derivadas[-1]
    return lista_derivadas

# Generar la serie de Taylor alrededor de x_inicial
def expandir_taylor(expr, x_inicial, x_final, max_orden):
    # Obtener derivadas
    lista_derivadas = obtener_derivadas(expr, x, max_orden)

    # Evaluar función en x_inicial
    valor_funcion = expr.subs(x, x_inicial)

    # Calcular el valor de h
    delta = x_final - x_inicial

    # Construir la serie de Taylor
    suma_taylor = float(valor_funcion)
    resultados = []

    for i in range(max_orden + 1):
        termino_residual = lista_derivadas[i].subs(x, x_inicial) * (delta**(i+1)) / m.factorial(i+1)
        resultados.append((i, suma_taylor, termino_residual))
        suma_taylor += termino_residual
    return resultados


# Calcular los términos de la serie de Taylor
resultados = expandir_taylor(func, x_inicial, x_final, max_iter)

# Imprimir los resultados
print("Parámetros iniciales")
print("x_inicial =", x_inicial)
print("x_final =", x_final)
print()

print("f(x_inicial) =", float(func.subs(x, x_inicial)))
print("delta =", x_final - x_inicial)
print()

print("#", "\t", "|", "f(x)", "\t", "|", "Término Rn")
print("-" * 30)
for i, suma_taylor, termino_residual in resultados:
    print(i, "\t", "|", round(suma_taylor), "\t", "|", termino_residual)
