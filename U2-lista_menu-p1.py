#1 t
z = [2,5,4,7,6,8,9]
print(z)
#z[2] = 6
print("quE deseas ralizar?")

'''
array.insert(1,4)
array.pop(*indice*)

if x in array:
    print("Existe en el arreglo")
    
for num in lista
    print(num)
'''


def a1():
    print('ANNADIR UNO O MAS ELEMENTOS')
    z.extend(input([]))
    print(z)
def a2():
    print('ORDENAR ELEMENTOS DE MANERA ASCENDENTE')
    z.sort()
    print(z)
def a3():
    print('ORDENAR ELEMENTOS DE MANERA DESCENDENTE')
    z.reverse()
    print(z)
def a4():
    print('SALIR')

op = 1
while op != 4:
    print('1.annadir elementos\n2.ordenamiento ascendente\n3.ordenamiento descendente\n4.salir')
    op = int(input('elige una opcion: '))
    if op == 1:
        a1()
    elif op == 2:
        a2()
    elif op == 3:
        a3()
    elif op == 4:
        print('exit...')
    else:
        print('Ingrese una opcion valida')