import time

def minimo_monedas_memo(cantidad, monedas, memoizacion=None):
    # Inicializar memo como un diccionario vacío 
    if memoizacion is None:
        memoizacion = {}

    # Si la cantidad es 0 no se necesitan monedas
    if cantidad == 0:
        return 0

    # Si ya se calculó la solución para la cantidad entonces se devuelve directamente el resultado
    if cantidad in memoizacion:
        return memoizacion[cantidad]

    # Inicializar el número mínimo de monedas en un valor infinito
    min_monedas = float('inf')

    # Realizar iteraciones sobre las denominaciones dadas
    for moneda in monedas:
        if moneda <= cantidad:
            # Calcular el número de monedas necesarias para la cantidad restante (cantidad - moneda)
            num_monedas = minimo_monedas_memo(cantidad - moneda, monedas, memoizacion)
            
            # Si es posible formar la cantidad restante (num_monedas no es infinito)
            if num_monedas != float('inf'):
                # Actualizar min_monedas si se encuentra una solución con menos monedas
                min_monedas = min(min_monedas, num_monedas + 1)

    # Almacenar el resultado en memo
    memoizacion[cantidad] = min_monedas

    # Retornar el número mínimo de monedas necesario para formar la cantidad dada
    return memoizacion[cantidad]

# Función principal que maneja el caso en el que no se puede dar cambio exacto
def minimo_monedas(cantidad, monedas):
    # Llamamos a la función recursiva con memoización para calcular el resultado
    resultado = minimo_monedas_memo(cantidad, monedas)
    
    # Si el resultado es infinito significa que no es posible dar el cambio de monedas exacto
    if resultado == float('inf'):
        return -1
    
    # Si es posible dar el cambio retorna el número mínimo de monedas necesarias
    return resultado

# Entrada de datos por parte del usuario
monedas = list(map(int, input("Ingresa las denominaciones de monedas, separadas por espacios: ").split()))
cantidad = int(input("Ingresa la cantidad para la cual deseas encontrar el cambio mínimo: "))

# Medir el tiempo de ejecución
start_time = time.time()  # Inicia el temporizador

resultado = minimo_monedas(cantidad, monedas)

end_time = time.time()  # Finaliza el temporizador

# Impresión del resultado en pantalla
if resultado == -1:
    print(f"No es posible dar el cambio exacto para {cantidad} con las monedas.")
else:
    print(f"El número mínimo de monedas necesario para {cantidad} es: {resultado}")

# Imprimir el tiempo de ejecución
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")


