""""
	practica en clase
	@drmorales4

"""

# importaciones
import codecs
import json

# leer archivo
archivo = codecs.open("datos.txt", "r")
lineas = archivo.readlines()

# imprimir cantidad de lineas del archivo
# print(len(lineas))

linea_diccionario = [json.loads(l) for l in lineas]


# Encontrar todos los que han hecho mas de 3 goles

funcion1 = lambda x: list(x.items())[1][1] > 3
goles = filter(funcion1, linea_diccionario) # filtrando todos los de que tengan mas de 3 goles con la funcion lambda
print(list(goles))


print("\n-----------------------------------------------------------------\n") # linea de separacion

# Encontrar los que son del país Nigeria

funcion2 = lambda x: list(x.items())[0][1] == "Nigeria"
pais = filter(funcion2, linea_diccionario) # filtrando todos los de pais Nigeria con la funcion lambda
print(list(pais))


print("\n---------------------------------------------------------------\n") # linea de separacion

# El valor mínimo y máximo de la caracteristica Height

funcion3 = list(map(lambda x: list(x.items())[2][1], linea_diccionario))
minimo = min(funcion3) # obtener el minimo de height
maximo = max(funcion3) # obtener el maximo de height

# imprimir minimo
print(list(filter(lambda x: list(x.items())[2][1] == minimo, linea_diccionario))) # imprimir toda la linea que tenga el valor minimo en height
print("\n")
# imprimir maximo
print(list(filter(lambda x: list(x.items())[2][1] == maximo, linea_diccionario))) # imprimir toda la linea que tenga el valor maximo en height
