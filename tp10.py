import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image

def busqueda_en_imagen(imagen, tono):
    
    resultado = {}
    filas, columnas = imagen.shape

    for x in range(filas):
        for y in range(columnas):
            if imagen[x, y] == tono:
                resultado[(x, y)] = imagen[x, y]

    return resultado

def prueba_busqueda_en_imagen():
    
    tamanos = [(10, 10), (100, 100), (500, 500), (1000, 1000)]
    tono = 128
    resultados = {}

    for tamano in tamanos:
        imagen = np.random.randint(0, 256, size=tamano, dtype=np.uint8)

        inicio = time.time()
        busqueda_en_imagen(imagen, tono)
        tiempo_ejecucion = time.time() - inicio

        resultados[tamano] = tiempo_ejecucion

    return resultados

def resaltar_puntos(imagen, puntos):
    
    imagen_resaltada = np.stack([imagen]*3, axis=-1)  # Convertir a RGB

    for (x, y) in puntos.keys():
        imagen_resaltada[x, y] = [255, 0, 0]  # Resaltar en rojo

    plt.imshow(imagen_resaltada)
    plt.title('Puntos resaltados')
    plt.show()

def graficar_resultados(resultados):
    
    tamanos = [t[0] for t in resultados.keys()]
    tiempos = list(resultados.values())

    plt.plot(tamanos, tiempos, label='Tiempo de ejecución')
    plt.xlabel('Tamaño de la imagen (nxn)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Rendimiento de la búsqueda en imágenes')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejecución de pruebas y visualización de resultados
resultados = prueba_busqueda_en_imagen()
graficar_resultados(resultados)

# Ejemplo de uso de resaltar_puntos
imagen = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
puntos = busqueda_en_imagen(imagen, 128)
resaltar_puntos(imagen, puntos)


#no entendi tanto realmente de la act :/
