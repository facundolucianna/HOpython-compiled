# Reglas para compilar

### Paso 1

Se compilaron en archivos objetos los archivos *add_two.c* y *arrays.c* usando el flag -fPIC

```
gcc -c -fPIC add_two.c -o add_two.o
gcc -c -fPIC arrays.c -o arrays.o
```

Salida cuando se ejecuta *nm* para cada archivo objeto

**add_two.o**

```
[shell]$ nm add_two.o
0000000000000000 T add_float
000000000000002e T add_float_ref
000000000000001a T add_int
0000000000000061 T add_int_ref
```

**arrays.o**

```
[shell]$ nm arrays.o
0000000000000000 T add_int_array
0000000000000073 T dot_product

```

### Paso 2

Se crea la libreria *libmymath.so*

```
gcc -shared arrays.o add_two.o -o libmymath.so
```

### Paso 3
