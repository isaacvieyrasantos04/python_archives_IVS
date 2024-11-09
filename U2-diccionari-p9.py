#9 t
#hacer un diccionario donde hayan almenos cinco datos personales de un usuario
#edad, nombre, grado, escuela, pais

'''
dicci = {
"key" : "val",
"name" : "isaac",
"pais" : "mx"
}

print(dicci["pais"])
dicci["pais"] = "us"
'''

di = {
    "nombre" : "",
    "edad" : None,
    "grado" : None,
    "escuela" : "",
    "pais" : ""
}


di["nombre"]=input("NOMBRE: ")
di["edad"]=int(input("EDAD: "))
di["grado"]=int(input("GRADO: "))
di["escuela"]=input("ESCUELA: ")
di["pais"]=input("PAIS: ")
print(di["nombre"])
print(di["edad"])
print(di["grado"])
print(di["escuela"])
print(di["pais"])


