import datetime




def fibonacci(n):
    """funcion fibonacci
    Una función que reciba un número entero positivo n
    y calcule el número de fibonacci asociado a ese número usando bucle for i in


    Parámetros:
        - n : un numero enter
    Salida:
        - a: un numero entero
        Es el numero asociado de fibonacci."""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a




def recursiva_fibo(n):
    """funcion fibonacci
    Una función que reciba un número entero positivo n
    y calcule el número de fibonacci asociado a ese número de forma recursiva


    Parámetros:
        - n : un numero enter
    Salida:
        - a: un numero entero
        usando la plantilla de la primera funcion para calcular la secuencia de fibonaci hago un
        contador con nllamando a la funcion hasta que este acabe."""
    a, b = 0, 1
    a, b = b, a + b
    if n>= 0:
        n-= 1
        recursiva_fibo(n)
    return a
"""prueba de rendimiento por fuerza bruta"""






print("funcion de fibonacci:")
for n in (1, 10, 20, 30, 40):
    start_time = datetime.datetime.now()
    fibonacci(n)
    end_time = datetime.datetime.now()
    print (f"El tiempo de ejecución para {n} es:", end_time - start_time)


print("funcion de recursiva de fibonacci:")


for n in (1, 10, 20, 30, 40):
    start_time = datetime.datetime.now()
    recursiva_fibo(n)
    end_time = datetime.datetime.now()
    print (f"El tiempo de ejecución para {n} es:", end_time - start_time)
