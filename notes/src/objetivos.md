# Objetivos

Los objetivos principales de este curso son:

- Entender cómo compilar código de CUDA Fortran.
- Comprender los términos más comunes de la programación en CUDA.

## Alternativas a CUDA

CUDA es en realidad una colección de librerías y compiladores que trabaja directamente
la empresa NVIDIA, los cuales son los responsables de crear GPUs (Graphical Processing Unit).

Sin embargo, NVIDIA no es la única empresa que elabora GPUs, siendo AMD el otro gran
contendiente, y su plataforma de cómputo [ROCm](https://www.amd.com/en/graphics/servers-solutions-rocm).

## ¿Porqué usar GPUs?

La idea principal es emplear GPUs para reducir el tiempo de cómputo (NO la complejidad algorítmica),
y distribuir el trabajo que pueda ser difícil para el CPU a un tipo de _hardware_ especializado.

Al tener más ancho de banda y un rendimiento mucho más elevado que un CPU convencional, aunado a una
flexibilidad de programación, las GPU tratan de resolver el problema de cómputo de alto rendimiento.

## Cómputo heterogeneo

El hecho de que se puedan usar CPU y GPU simultáneamente para resolver un problema dado es muy bien
conocido como el problema del [cómputo heterogeneo](https://revistaseug.ugr.es/index.php/amgp/article/view/7465).

Existen estándares, como [OpenACC](https://www.openacc.org/) que facilitan este tipo de trabajo
para el usuario (programador).
