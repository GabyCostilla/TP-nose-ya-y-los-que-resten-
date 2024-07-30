import time
import random
import matplotlib.pyplot as plt

def busqueda_lineal(lista, elemento):

    for indice, valor in enumerate(lista):
        if valor == elemento:
            return indice
    return -1

def busqueda_binaria(lista, elemento):
  
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def prueba_algoritmos():

    tamanos = [10, 100, 1000, 10000, 100000]
    resultados = {}

    for tamano in tamanos:
        lista = sorted(random.sample(range(tamano * 10), tamano))
        elemento = random.choice(lista)

        
        inicio = time.time()
        busqueda_lineal(lista, elemento)
        tiempo_lineal = time.time() - inicio

        
        inicio = time.time()
        busqueda_binaria(lista, elemento)
        tiempo_binaria = time.time() - inicio

        resultados[tamano] = (tiempo_lineal, tiempo_binaria)

    return resultados

def graficar_resultados(resultados):
    
    tamanos = list(resultados.keys())
    tiempos_lineal = [resultados[t][0] for t in tamanos]
    tiempos_binaria = [resultados[t][1] for t in tamanos]

    plt.plot(tamanos, tiempos_lineal, label='Búsqueda Lineal')
    plt.plot(tamanos, tiempos_binaria, label='Búsqueda Binaria')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de algoritmos de búsqueda')
    plt.legend()
    plt.grid(True)
    plt.show()


resultados = prueba_algoritmos()
graficar_resultados(resultados)
