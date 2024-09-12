import time
#se recibe la cadena para verificar,los indices que quiero comparar y el diccionario
def EsPalindromo(string, inicio, fin, memoizacion):
    #aqui verficiamos si ya llegamos al cado base que es donde ya se llego a la mitad de la cadena si llega a este punto
    #es por que es un palidromo
    if inicio >= fin:
        return True
    #si no hemos terminado de analizar la cadena verificamos si el caso que tenemos ya esta contenido en el diccionario
    if (inicio, fin) in memoizacion:
        return memoizacion[(inicio, fin)]
    #si el caracter en los indices que estoy comparando son diferentes retorno false
    if string[inicio] != string[fin]:
        memoizacion[(inicio, fin)] = False
        return False
    #se hace la llamada recursiva
    memoizacion[(inicio, fin)] = EsPalindromo(string, inicio + 1, fin - 1, memoizacion)
    return memoizacion[(inicio, fin)]

print("Ingrese las cadenas que quiere verificar separadas por espacio")
#se crea la lista string para contener las palabras que se quieren verificar
string = input().split()
#con un for recorremos cada elemento de la lista para verificar si es un palindromo
for i in range(len(string)):
    #se crea el diccionario memoizacion que me contendra los resultados obtenidos
    memoizacion = {}
    start_time = time.time()
    #se hace llamada a la funcion desde ambos extremos de la cadena con el diccionario 
    resultado = EsPalindromo(string[i], 0, len(string[i]) - 1, memoizacion)
    end_time = time.time()
    elapsed_time = end_time - start_time
     # Ajusta el formato para eliminar ceros innecesarios
    if elapsed_time < 1e-6:  # Si el tiempo es menor a 1 microsegundo
        time_str = f"{elapsed_time:.10e}"  # Notación científica
    else:
        # Usa el formato en cadena para eliminar ceros a la derecha
        time_str = f"{elapsed_time:.10f}".rstrip('0').rstrip('.')
    
    # Imprime el resultado en la consola
    print(f"¿La cadena '{string[i]}' es un palíndromo? {resultado}")
    print(f"Tiempo de ejecución para '{string[i]}': {time_str} segundos")
   