z = [1,2,3,4,5]
#z[2] = 6
print("que operacion deseas ralizar?")


def a1():
    print('VER ELEMENTO')
    print(z)
def a2():
    print('ADD ELEMENTO')
    z.append(int(input("inserta un nuevo elemento: ")))
    print(z)
def a3():
    print('MODIFICAR ELEMENTO')
    print(z)
    print("que posiciOn deseas modificar? ")
    #z[int(input("inserta aquI: "))] = 6
    z.__setitem__(int(input(": ")), int(input("inserta aquI el nuevo elemento: ")))
    print(z)
def a4():
    print('SUPR ELEMENTO')
    z.remove(int(input("inserta el elemento a eliminar: ")))
    print(z)
def a5():
    print('SALIR')


op = 1
while op != 5:  # Se ejecuta mientras op sea diferente de 4
    print('1.ver elemento\n2.agregar elemento\n3.modificar elemento\n4.eliminar elemento\n5.salir')
    op = int(input('Ingresa una opcion: '))  # Usuario ingresa opcion

    if op == 1:
        a1()
    elif op == 2:
        a2()
    elif op == 3:
        a3()
    elif op == 4:
        a4()
    elif op == 5:
        print('exit...')
    else:
        print('Ingrese una opcion valida')