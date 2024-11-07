#include <cmath>
#include <cstdio>
#include <omp.h>  // Para ejecutar el codigo en paralelo

double f(double x) {
    return exp(-x * x);  // f(x) = e^(-x^2)
}


//  metodo de Simpson 3/8 multiple (paralela)
double simpson_3_8(double a, double b, int n) {
    if (n % 3 != 0) {
        printf("n debe ser un múltiplo de 3\n");
        return -1; 
    }

    double h = (b - a) / n;
    double result = 0.0;

    // Aplicar la regla de Simpson 3/8 en paralelo
    #pragma omp parallel
    {
        double local_sum = 0.0;

        #pragma omp for
        for (int i = 0; i <= n; ++i) {
            double x = a + i * h;

            if (i == 0 || i == n) {
                local_sum += f(x); // f(a) + f(b)
            } else if (i % 3 == 0) {
                local_sum += 2 * f(x); // 2 * f(x_{3i})
            } else {
                local_sum += 3 * f(x); // 3 * f(x_{i})
            }
        }

        // Sumar resultados locales
        #pragma omp atomic
        result += local_sum;
    }

    result *= (3.0 / 8.0) * h; // Multiplicar por 3/8 * h

    return result;
}

int main() {
    double a = -1.0, b = 1.0;
    int n = 30;  

    // Medir el tiempo de la implementación paralela
    double start_time = omp_get_wtime();
    double result_paralelo = simpson_3_8(a, b, n);
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
