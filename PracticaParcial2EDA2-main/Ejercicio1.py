import time 
import numpy as np
#muestra la matriz de memoizacion
def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(int(elem)) for elem in fila))
    print()

def contar_caminos(matriz): 
    filas = len(matriz) #numero de filas de la matriz pasada por parametro
    columnas = len(matriz[0]) #numero de las columnas de la matriz pasada por parametro

    #reviso que la matriz en [0][0] y en [filas -1][columnas -1] sea diferente de 1 por que no se podrian hacer los calculos en ese caso
    if matriz[0][0] == 1 or matriz[filas - 1][columnas - 1] == 1: 
        return 0
    #creo una matriz llena de ceros para mirar el numero de caminos 
    memoizacion = np.zeros((filas, columnas))
    #aqui inicializo [0][0]=1 por que solo hay 1 camino para llegar a el 
    memoizacion[0][0] = 1
    
    # relleno la primera columna buscando que no hayan 1 en la matriz pasada por parametro
    i = 1  # Inicializo i en 1
    while i < filas:  
        if matriz[i][0] == 0:  # Si no hay obstáculo
            # Copio el valor de arriba que en caso de que no hayan obstaculos seria 1 por qu ehay un camino para llegar
            memoizacion[i][0] = memoizacion[i - 1][0]  
        i += 1

    # relleno la primera fila buscando que no hayan 1 en la matriz pasada por parametro
    j = 1  
    while j < columnas:  
        if matriz[0][j] == 0:  # Si no hay obstáculo
            memoizacion[0][j] = memoizacion[0][j - 1] # Copio el valor de la izquierda que en caso de que no hayan obstaculos seria 1 por qu ehay un camino para llegar
        j += 1
        
    i = 1 
    while i < filas:
        j = 1 
        while j < columnas:
            if matriz[i][j] == 0:  # Si no hay obstáculo
                memoizacion[i][j] = memoizacion[i - 1][j] + memoizacion[i][j - 1]  # suma de caminos desde arriba y desde la izquierda para saber cuantos caminos hay
            j += 1  # Incrementamos j en 1
        i += 1  # Incrementamos i en 1
    mostrar_matriz(memoizacion)  # Mostrar la matriz de memoización
    return int(memoizacion[filas - 1][columnas - 1])  # retorna el numero de la ultima celda el cual es el total de los caminos que se pueden tomar



A = np.array(eval(input("Ingrese la matriz de 0 y 1:")))
inicio = time.time()  # tiempo de inicio
resultado = contar_caminos(A)
fin = time.time()  # tiempo de fin

print(f"Número de caminos posibles: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

            







