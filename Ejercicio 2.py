import cProfile


def capitalizado2(fichero):
    """funcion para capitalizar el nombre de una lsita de nombres.


    Parámetros:
        - fichero : el fichero o elemnto de informacion para hacer el capitalizado
    Salida:
        - captz: Una lista que contine la misma informacion que el fichero introducido pero capitalizado
       
        Se abre el fichero y lo guardo en una variable con readlines
        se recorre la nueva variable se capitaliza con la fucnion .title
        se separa con split los elementos
        como hal separa con split va hacer dos elemntos []"josué peiró oliver,77638473", ""]
        solo cojo el primero elemnto y lo vuelvo a separar con split
        y se añade a captz """
    captz = []
    with open(fichero, 'r') as file:
        listacap = file.readlines()
        for capitalizado in listacap:
            capitalizado =capitalizado.title()
            capitalizado = capitalizado.split("\n")
            capitalizado = capitalizado[0].split(",")
            for j in capitalizado:
                    captz.append(j)
    return captz
def cal_num_dni(fichero):
    """funcion para clacular la letra del DNI dependiendo del numero de dni


    Parámetros:
        - fichero : el fichero o elemnto de informacion para realizar la funcion
    Salida:
        - diccionario: Un diccionario que va contener el numero de DNI assignado a su letra correspondiente
       
        Mismo proceso que en la funcion capitalizacion2 para hacer una lista con la informacion del fichero
        para poder trabajar
       
        Para calcular la letra dependiendo del numero de dni
        Se hace un bucle for recorriendo las lista cal_dni que contien la informacion
        y cono lista va primero el nombre y despues el numero,
        el numero esta situado en un numero par (hay que sumarle 1 por que empieza en zero)
        calculo la poscion del elemento recorrido por for i y si es par
        se hace la division entre 23
        y el valor de la division es la poscion de la letra en la secuencia de dni_letra"""
   
    calc_dni=[]
    dni_letra = "TRWAGMYFPDXBNJZSQVHLCKE"
    diccionario = {}
    with open(fichero, 'r') as file:
        listadni = file.readlines()
        for numero_dni in listadni:
            numero_dni = numero_dni.split("\n")
            numero_dni = numero_dni[0].split(",")
            for j in numero_dni:
                    calc_dni.append(j)
    for i in calc_dni:
        par = calc_dni.index(i) + 1
        if par%2 == 0:
            i = int(i)
            resto = i%23
            diccionario[calc_dni[par-1]] = dni_letra[resto]


    return diccionario




def leerficheros():
    """funcion que usa las dos funciones anteriores de capitalizado y calcular letra
        de dos lista csv de 50 y 1000 personas
    Parámetros:
        ninguno
    Salida:
        ninguno"""


    fichero = "50.csv"
    capitalizado2(fichero)
    cal_num_dni(fichero)
    fichero = "1000.csv"
    capitalizado2(fichero)
    cal_num_dni(fichero)  
    return  


cProfile.run("leerficheros()")
