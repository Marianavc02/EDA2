import time

def swap(conjunto, i, j):
    #intercambio los elementos en las posiciones i y j del conjunto
    conjunto[i], conjunto[j] = conjunto[j], conjunto[i]

def GenerarPermutaciones(conjunto, inicio, fin, memoizacion):
    #genero todas las permutaciones del conjunto entre los índices inicio y fin usando memoización."""
    tupla_conjunto = tuple(conjunto)
    
    if (inicio, fin, tupla_conjunto) in memoizacion:
        return memoizacion[(inicio, fin, tupla_conjunto)]
    
    if inicio == fin:
        # Retorno la permutación actual como una lista
        resultado = [list(conjunto)]
    else:
        resultados = []
        for i in range(inicio, fin + 1):
            swap(conjunto, inicio, i)  # Intercambio el elemento en el índice de inicio con el elemento en el índice i
            sub_resultados = GenerarPermutaciones(conjunto, inicio + 1, fin, memoizacion)  # Llamo recursivamente para el siguiente índice
            resultados.extend(sub_resultados)
            swap(conjunto, inicio, i)  # Restauro el conjunto al estado original 
        
        memoizacion[(inicio, fin, tupla_conjunto)] = resultados
        resultado = resultados
    
    return resultado

#solicito al usuario que ingrese los elementos del conjunto
elementos = input("Ingrese los elementos del conjunto separados por espacio: ")
conjunto = elementos.split()
memoizacion = {}

# Mido el tiempo de ejecución
start_time = time.time()

# genero todas las permutaciones
permutaciones = GenerarPermutaciones(conjunto, 0, len(conjunto) - 1, memoizacion)

end_time = time.time()
elapsed_time = end_time - start_time

# Ajusta el formato para eliminar ceros innecesarios
if elapsed_time < 1e-6:  # Si el tiempo es menor a 1 microsegundo
    time_str = f"{elapsed_time:.10e}"  # Notación científica
else:
    # Usa el formato en cadena para eliminar ceros a la derecha
    time_str = f"{elapsed_time:.10f}".rstrip('0').rstrip('.')

# Imprime todas las permutaciones generadas
for permutacion in permutaciones:
    print(permutacion)

# Imprime el tiempo de ejecución
print(f"Tiempo de ejecución: {time_str} segundos")
