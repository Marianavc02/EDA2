import time

def generar_subsecuencias(arr, index=0, subsecuencia=[], memo=None):
    if memo is None:
        memo = {}
    
    # Clave para memoización: estado actual (índice y subsecuencia)
    clave = (index, tuple(subsecuencia))
    
    # Si ya calculamos el resultado para este índice y subsecuencia, lo devolvemos desde memo (usando la tabla hash).
    # Esto evita recomputar subsecuencias que ya se calcularon antes.
    if clave in memo:
        return memo[clave]
    
    # Si hemos llegado al final del arreglo, verificamos si la subsecuencia no está vacía.
    if index == len(arr):
        if len(subsecuencia) > 0:
            # Si la subsecuencia no está vacía, la devolvemos como parte de los resultados.
            return [subsecuencia]
        else:
            # Si la subsecuencia está vacía, no la incluimos y devolvemos una lista vacía.
            return []
    
    # Genera subsecuencias sin incluir el elemento actual
    sin_incluir = generar_subsecuencias(arr, index + 1, subsecuencia, memo)
    
    # Genera subsecuencias incluyendo el elemento actual
    con_incluir = generar_subsecuencias(arr, index + 1, subsecuencia + [arr[index]], memo)
    
    # Guardar en el memo el resultado de la combinación de ambas posibilidades
    memo[clave] = sin_incluir + con_incluir
    return memo[clave]

def contar_subsecuencias_con_suma(arr, s):
    # Genera todas las subsecuencias posibles usando la función anterior
    subsecuencias = generar_subsecuencias(arr)
    contador = 0
    
    # Cuenta cuántas subsecuencias tienen una suma igual a 's'
    for subsecuencia in subsecuencias:
        if sum(subsecuencia) == s:
            contador += 1
    
    return contador

# Medición del tiempo de ejecución
arr = list(map(int, input("Ingrese los elementos del arreglo separados por espacios: ").split()))
s = int(input("Ingrese el valor objetivo S: "))

start_time = time.time()  # Inicio de la medición del tiempo

resultado = contar_subsecuencias_con_suma(arr, s)

end_time = time.time()  # Fin de la medición del tiempo

print(f"El número de subsecuencias cuya suma es igual a {s} es: {resultado}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
