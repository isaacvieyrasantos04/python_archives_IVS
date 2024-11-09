#7 t
class stack:
    def __init__(self):
        self.z=[]
        for i in range(11):
            self.z.append(i+1)

    def  void(self):
        return len(self.z) == 0

    def add(self, elem):
        self.z.append(elem)

    def elementos(self):
        for i in self.z:
            print(i)

    def out(self):
        self.z.pop(len(self.z)-1)

if __name__=="__main__":
    stack = stack()

if stack.void():
    print("LISTA VACIA")

salir = False
while not salir:
    print("\nEliga una opción: \n"
          "1 - Agregar elemento. \n"
          "2 - Eliminar ultimo elemento.\n"
          "3 - Revisar elementos. \n"
          "4 - Salir. \n")
    op = input("¿Qué deseas realizar? : ")
    match op:
        case "1":
            elem=(int(input("Agrega elemento: ")))
            stack.add(elem)
            stack.elementos()
        case "2":
            stack.out()
            stack.elementos()
        case "3":
            stack.elementos()
        case "4":
            salir= True