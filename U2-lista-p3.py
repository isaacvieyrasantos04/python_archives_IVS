#3 t
z = [2,5,4,7,6,8,9]
print(z)
print("INSERTAR VALOR EN INDICE")
z.insert(int(input("indice: ")),int(input("valor: ")))
print(z)

print("BORRAR VALOR EN INDICE")
z.pop(int(input("indice: ")))
print(z)

x = int(input("ingresa valor: "))
if x in z:
    print(x," SI existe en el arreglo")
else:
    print(x, " NO existe en el arreglo")