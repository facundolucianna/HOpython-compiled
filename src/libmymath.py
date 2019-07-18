import ctypes as C

#Creamos la clase con todas las funciones de C
math = C.CDLL('./libmymath.so')

#Empezamos a probar todas las funciones

#int add_int(int a, int b)
print("Funcion add_int()")
math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int, C.c_int]

var1 = 4
var2 = 3

res = math.add_int(var1, var2)

print("Salida = " + str(res))

#float add_float(float a, float b)
print("Funcion add_float()")
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]

var1 = 2.3
var2 = 1.2

res = math.add_float(var1, var2)

print("Salida = " + str(res))

#int add_int_ref(int *a, int *b, int *c)
print("Funcion add_int_ref()")
math.add_int_ref.restype = C.c_int

var1 = 743
var2 = 2

a = C.c_int(var1)
b = C.c_int(var2)
res = C.c_int()

state = math.add_int_ref(C.byref(a), C.byref(b), C.byref(res))

output = res.value

print("Resultado = " + str(output) + " y salida = " + str(state))

#int add_float_ref(float *a, float *b, float *c)
print("Funcion add_float_ref()")
math.add_float_ref.restype = C.c_int

var1 = 7.4
var2 = 3.1

a = C.c_float(var1)
b = C.c_float(var2)
res = C.c_float()

state = math.add_float_ref(C.byref(a), C.byref(b), C.byref(res))

output = res.value

print("Resultado = " + str(output) + " y salida = " + str(state))
