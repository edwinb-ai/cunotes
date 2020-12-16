# Esenciales de CUDA

Algunas **definiciones:**

- Un **kernel** es una _subrutina_ que contiene instrucciones específicas para la GPU.
- Un **CUDA core** es el análogo a un _núcleo_ o _procesador_ de un CPU.

# Jerarquía de la memoria

La GPU tiene **mallas** con un número definido de **bloques**, y estos a su vez tienen un número
fijo de **hilos**.

- Existen **1024** hilos por bloque.
- Los _bloques_ y los _hilos_ tienen **dimensionalidad** 3: _x_, _y_ y _z_.
- Existen $2^{31} - 1$ bloques por _malla_ para la dimensión _x_ y 65535 para las otras dos.[^1]

# Uso de kernels

La sintáxis para usar _kernels_ es

```Fortran
call nombre_kernel<<<numero_bloques, hilos_por_bloque>>>(argumentos, ...)
```

Los _kernels_ pueden tener cualquiera de los siguientes **atributos:**

- `host`: Solamente se puede llamar desde el CPU y **no** se ejecuta en GPU.
- `global`: Puede ser llamado en CPU o en GPU, y **si** se ejectua en GPU.
- `device`: Solamente puede ser llamado en GPU, y **si** se ejectua en GPU.

[^1]: [Tabla de referencia de specificaciones técnicas.](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#features-and-technical-specifications)