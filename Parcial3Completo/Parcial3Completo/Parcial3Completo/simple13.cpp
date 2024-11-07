#include <stdio.h>
#include <math.h>
#include <omp.h>  // Para ejecutar en paralelo

// Definir la función que queremos integrar
double f(double x) {
    return exp(-x * x);  // f(x) = e^(-x^2)
}

// Implementación del método de Simpson 1/3 (secuencial o paralelo)
double simpson(double a, double b, int n, int parallel) {
    double h = (b - a) / n;
    double sum_odd = 0.0, sum_even = 0.0;

    if (parallel) {
        // Calcular términos impares en paralelo
        #pragma omp parallel for reduction(+:sum_odd)
        for (int i = 1; i <= n - 1; i += 2) {
            sum_odd += f(a + i * h);
        }

        // Calcular términos pares en paralelo
        #pragma omp parallel for reduction(+:sum_even)
        for (int i = 2; i <= n - 2; i += 2) {
            sum_even += f(a + i * h);
        }
    } else {
        // Calcular términos impares de forma secuencial
        for (int i = 1; i <= n - 1; i += 2) {
            sum_odd += f(a + i * h);
        }

        // Calcular términos pares de forma secuencial
        for (int i = 2; i <= n - 2; i += 2) {
            sum_even += f(a + i * h);
        }
    }

    // Aplicar la fórmula de Simpson
    double result = (h / 3) * (f(a) + 4 * sum_odd + 2 * sum_even + f(b));
    return result;
}

int main() {
    double a = -1.0;  // Límite inferior
    double b = 1.0;   // Límite superior
    int n = 1000000;  // Número de subintervalos (debe ser par)

    // Medir el tiempo de ejecución para la implementación secuencial
    double start_time = omp_get_wtime();
    double result_secuencial = simpson(a, b, n, 0); // 0 para secuencial
    double end_time = omp_get_wtime();
    printf("Resultado de la integral (secuencial): %.10f\n", result_secuencial);
    printf("Tiempo de ejecucion (secuencial): %.6f segundos\n", end_time - start_time);

    // Medir el tiempo de ejecución para la implementación paralela
    start_time = omp_get_wtime();
    double result_paralelo = simpson(a, b, n, 1); // 1 para paralelo
    end_time = omp_get_wtime();
    printf("Resultado de la integral (paralela): %.10f\n", result_paralelo);
    printf("Tiempo de ejecucion (paralela): %.6f segundos\n", end_time - start_time);

    return 0;
}


