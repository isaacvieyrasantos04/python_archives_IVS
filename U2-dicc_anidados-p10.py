#10 t
'''
crear una estructura de diccionarios
anidados que al final de ejecucion
pida los datos de un alumno especifico
pedido por el usuario
'''
#from struct import pack_into

#q=int(input("cantidad de usuarios: "))
dic = {}

n=int(input("¿Cuántas claves y valores deseas ingresar? "))

for _ in range(n):
    pk = input("Introducir PK: ")
    v = input("Introducir el valor de PK: ")
    dic[pk] = v

print("Diccionario final:", dic)