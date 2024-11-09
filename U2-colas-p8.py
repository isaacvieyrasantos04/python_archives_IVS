#8
class queue:
    def __init__(self):
        self.z= []
        for i in range(10):
            self.z.append(i+1)
    def front(self):
        if len(queue.z)==0:
            print("LISTA VACIA ")
        else:
            print(self.z[0])
    def back(self):
        if len(queue.z)==0:
            print("LISTA VACIA ")
        else:
            print(self.z[len(self.z)-1],end=" ")
    def pop(self):
        for x in range(len(self.z)):
            self.z.pop(0)
            print(x,end=" ")
    def push(self, element):
        self.z.append(element)
    def elementos(self):
        for c in range(len(self.z)):
            print(self.z[c],end=" ")

if __name__=="__main__":
    queue = queue()

salir= False
while not salir:
    print("\nelegir opcion: \n"
          "1 - Primer elemento. \n"
          "2 - Ultimo elemento.\n"
          "3 - Agregar elemento. \n"
          "4 - Eliminar elementos. \n"
          "5 - Revisar elementos "
          "6 - Salir. ")
    op = input("¿Qué deseas hacer? : ")
    match op:
        case "1":
            queue.front()
        case "2":
            queue.back()
        case "3":
            elemento = (int(input("Agrega un elemento: ")))
            queue.push(elemento)
        case "4":
            queue.pop()
        case "5":
            queue.elementos()
        case "6":
            salir= True