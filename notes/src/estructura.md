# Curso CUDA

1. Introducción
   1. ¿Qué es CUDA? Computación heterogenea, para qué se necesita.
   2. Elementos esenciales de CUDA: compiladores, lenguajes de programación.
2. Elementos básicos de GPUs, parte 1.
   1. Mallas, bloques e hilos.
   2. Esquema general de la memoria. Memoria de textura, constante y global.
   3. **Primer proyecto:** Conjunto de Julia.
3. Elementos básicos de GPUs, parte 2.
   1. Aplicaciones simples, uso de bloques.
   2. Uso de bloques e hilos. Sincronización.
   3. **Segundo proyecto:** Producto punto (eficiente).
4. Elementos avanzados.
   1. Memoria de textura en dos dimensiones.
   2. **Tercer proyecto:** Ecuación de calor en dos dimensiones.
   3. Operaciones atómicas.
   4. **Cuarto proyecto:** Cómputo de un histograma.

# Proyecto final

Implementación de un algoritmo de simulación molecular usando la mayoría de estas
técnicas.
Se requieren de los siguientes elementos:

- Memoria global y compartida para hacer eficientes los cálculos de la fuerza.
- Operaciones atómicas y memoria compartida para el cómputo de la RDF.
- **Opcional:** Implementación de listas de vecinos y métodos de celdas para reducir el tiempo de cómputo de la fuerza por partícula.