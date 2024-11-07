import time 
import numpy as np
import matplotlib.pyplot as plt


#Definicion de funcion para diferencia minima 
def dif_min(arreglo):
    
    #Calcular la suma total de los valores dentro del arreglo 
    sum_total= sum(arreglo)
    
    #Calcular el tamaño del arreglo 
    tam= len(arreglo)
    
    #Crear una tabla booleana sumas_posibles, donde sumas_posibles[i] indica si es posible formar una suma i
    #con algunos elementos del arreglo, teniendo en cuenta que nos interesan las sumas que no superen 
    #la mitad de la suma toatl del arreglo. 
    sumas_posibles= np.zeros((tam + 1, sum_total // 2 + 1), dtype=bool)
    
    # Inicializar la primera fila. Es posible formar la suma 0 solo con el conjunto vacío,
    # pero dado que no queremos subconjuntos vacíos, asi que se toma solo como caso base.
    sumas_posibles[0][0] = True
    
    #Llenar la tabla sumas_posibles usando programación dinámica para subconjuntos no vacíos
    for i in range(1, tam + 1):  # Tomamos solo subconjuntos no vacíos
        for j in range(1, sum_total // 2 + 1):
            # Si no se incluye el elemento actual arreglo[i-1]
            sumas_posibles[i][j] = sumas_posibles[i-1][j]
            
            # Si se incluye el elemento actual arreglo[i-1]
            if arreglo[i-1] <= j:
                sumas_posibles[i][j] = sumas_posibles[i][j] or sumas_posibles[i-1][j - arreglo[i-1]]
                
     #Buscar la mayor suma posible que sea menor o igual a la mitad de la suma total
    max_sum = 0
    for j in range(sum_total // 2, -1, -1):
        if sumas_posibles[tam][j]:
            max_sum = j
            break
        
    #La diferencia mínima es la diferencia entre la suma total y el doble de la suma
    # del subconjunto más cercano a la mitad.
    return abs(sum_total - 2 * max_sum)

# Función principal 
def principal():
    # Ingresar el número de casos de prueba
    try:
        num_casos = int(input("Ingresa el número de casos de prueba: "))
        # Verificar que el número de casos sea mayor que cero
        if num_casos <= 0:
            raise ValueError("El número de casos de prueba debe ser mayor que cero.")
    except ValueError as e:
        print(f"Error: {e}")
        return  # Salir de la función si hay un error

    resultados = []  # Lista para almacenar los resultados de cada caso
    tiempos = []     # Lista para almacenar los tiempos de ejecución

    # Para cada caso
    for i in range(num_casos):
        try:
            # Leer el arreglo
            arreglo = list(map(int, input(f"Ingresa los elementos del arreglo {i+1}, separados por espacios: ").split()))
            # Verificar que el arreglo no esté vacío
            if len(arreglo)  <2:
                raise ValueError("El arreglo debe tener al menos dos elementos para formar dos subconjuntos no vacíos.")
        except ValueError as e:
            print(f"Error: {e}")
            continue  # Continuar con el siguiente caso si hay un error

        # Capturar el tiempo de inicio
        tiempo_inicio = time.time()
        
        # Llamar a la función y calcular el resultado
        resultado = dif_min(arreglo)
        
        # Capturar el tiempo de finalización
        tiempo_fin = time.time()
        
        # Calcular el tiempo de ejecución
        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        
        # Mostrar el resultado y el tiempo de ejecución
        print(f"Diferencia mínima para el caso {i+1}: {resultado}")
        print(f"Tiempo de ejecución para el caso {i+1}: {tiempo_ejecucion:.6f} segundos\n")

        # Almacenar resultados y tiempos para la visualización
        resultados.append(resultado)
        tiempos.append(tiempo_ejecucion)

    # Visualización de resultados usando matplotlib
    plt.figure(figsize=(10, 5))
    plt.bar(range(1, num_casos + 1), resultados, color='skyblue', label='Diferencia Mínima')
    plt.xlabel('Caso de Prueba')
    plt.ylabel('Diferencia Mínima')
    plt.title('Diferencia Mínima entre Subconjuntos por Caso de Prueba')
    plt.xticks(range(1, num_casos + 1))
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Llamar a la función principal
if __name__ == "__main__":
    principal()
    