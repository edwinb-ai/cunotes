# `saxpy`, el "Hola Mundo" de las GPU

La operación coloquialmente conocida como `saxpy` es la siguiente
operación matemática

$$
\mathbf{y} = a \mathbf{x} + \mathbf{y}
$$

`saxpy` significa, en inglés

> Single-Precision A times X Plus Y

Esta operación se considera el "hola mundo" porque enseña una de las lecciones
más importantes de la programación en GPU:

> Las operaciones vectoriales son el **lenguaje nativo** de la programación en paralelo.

## Operaciones vectoriales

Las operaciones vectoriales, o vectorizadas, son las operaciones que **queremos** paralelizar.
Ejemplos de esto son:

- Suma y(o) multiplicación de vectores,
- suma y(o) multiplicación de matrices con vectores,
- suma y(o) multiplicación de matrices con matrices.

Otros algoritmos tienen que ser reescritos y reimplementados para que puedan funcionar de esta
forma, como por ejemplo:

- Transformada rápida de Fourier (FFT),
- álgebra lineal numérica,
- algoritmos particulares (simulación molecular, dinámica de fluidos computacional, etc.).

## Hilos y bloques

En este ejemplo de `saxpy` se aprovechará el hecho de que cada bloque cuenta con un número definido
de hilos, lo que permite que el trabajo se distribuya en bloques y en hilos y se puedan hacer
operaciones con arreglos mucho más grandes.

Es importante notar que para escoger el índice del hilo se usa el siguiente código

```fortran
i = blockDim%x * (blockIdx%x - 1) + threadIdx%x
```

debido a que los arreglos en FORTRAN comienzan en uno, a diferencia de cero, como en `C/C++`.