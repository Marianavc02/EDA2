#include <stdio.h>
#include <math.h>
#include <omp.h>  // Para ejecutar en paralelo

// Definir la función que queremos integrar
double f(double x) {
    return exp(-x * x);  // f(x) = e^(-x^2)
}

// Implementación del método de Simpson 3/8 (secuencial o paralelo)
double simpson38(double a, double b, int n, int parallel) {
    if (n % 3 != 0) {
        printf("n debe ser múltiplo de 3.\n");
        return 0.0;
    }

    double h = (b - a) / n;
    double sum = f(a) + f(b);
    double sum_even = 0.0, sum_odd = 0.0;

    if (parallel) {
        // Calcular términos impares y pares en paralelo
        #pragma omp parallel for reduction(+:sum_even, sum_odd)
        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 3 == 0) {
                sum_even += f(x);
            } else {
                sum_odd += f(x);
            }
        }
    } else {
        // Calcular términos impares y pares de forma secuencial
        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 3 == 0) {
                sum_even += f(x);
            } else {
                sum_odd += f(x);
            }
        }
    }

    sum += 2 * sum_even + 3 * sum_odd;

    // Aplicar la fórmula de Simpson 3/8
    double result = (3 * h / 8) * sum;
    return result;
}

int main() {
    double a = -1.0;  // Límite inferior
    double b = 1.0;   // Límite superior
    int n = 12;       // Número de subintervalos (debe ser múltiplo de 3)

    // Medir el tiempo de ejecución para la implementación secuencial
    double start_time = omp_get_wtime();
    double result_secuencial = simpson38(a, b, n, 0); // 0 para secuencial
    double end_time = omp_get_wtime();
    printf("Resultado de la integral (secuencial): %.10f\n", result_secuencial);
    printf("Tiempo de ejecucion (secuencial): %.6f segundos\n", end_time - start_time);

    // Medir el tiempo de ejecución para la implementación paralela
    start_time = omp_get_wtime();
    double result_paralelo = simpson38(a, b, n, 1); // 1 para paralelo
    end_time = omp_get_wtime();
    printf("Resultado de la integral (paralela): %.10f\n", result_paralelo);
    printf("Tiempo de ejecucion (paralela): %.6f segundos\n", end_time - start_time);

    return 0;
}




