#include <cmath>
#include <cstdio>
#include <omp.h>  // Para ejecutar el codigo en paralelo


double f(double x) {
    return exp(-x * x);  // f(x) = e^(-x^2)
}

//  paralela del  de Simpson 1/3 compuesto
double simpson(double a, double b, int n) {
    double h = (b - a) / n;
    double sum_odd = 0.0, sum_even = 0.0, result = 0.0;

    // Calcular  impares en paralelo
    #pragma omp parallel for reduction(+:sum_odd)
    for (int i = 1; i <= n - 1; i += 2) {
        sum_odd += f(a + i * h);
    }

    // Calcular  pares en paralelo
    #pragma omp parallel for reduction(+:sum_even)
    for (int i = 2; i <= n - 2; i += 2) {
        sum_even += f(a + i * h);
    }

    //  la fórmula de Simpson
    result = (h / 3) * (f(a) + 4 * sum_odd + 2 * sum_even + f(b));

    return result;
}

int main() {
    double a = -1.0 , b = 1.0;
    int n = 20;  // Número de subintervalos

    // Medir el tiempo de la implementación paralela
    double start_time = omp_get_wtime();
    double result_paralelo = simpson(a, b, n);
    double end_time = omp_get_wtime();
    double tiempoParalelo = end_time - start_time;

    int num_threads;
    #pragma omp parallel
    {
        num_threads = omp_get_num_threads();
    }
    //Calculo el tiempo secuencial
    double tiempoSecuencial = tiempoParalelo * num_threads;
    // Calcular el speedup
    double speedup = tiempoSecuencial / tiempoParalelo;

    printf("Resultado paralelo: %f\n", result_paralelo);
    printf("Tiempo paralelo: %f segundos\n", tiempoParalelo);
    printf("Tiempo secuencial estimado: %f segundos\n", tiempoSecuencial);
    printf("Speedup: %f\n", speedup);

    return 0;
}
