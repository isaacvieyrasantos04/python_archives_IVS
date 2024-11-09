#11 t
class platos:
    def __init__(self):
        self.q1 = set()
        self.q2 = set()

    def add(self, a, c):
        if c == 1:
            self.q1.add(a)
        else:
            self.q2.add(a)

    def showall(self):
        if len(self.q1 and self.q2) == 0:
            print("VOID")
        if len(self.q1 & self.q2) ==0:
            print("SIN ELEMENTOS COMUNES")
        else:
            print(f"PLATOS EN COMUN: {self.q1 & self.q2}")

    def showp(self):
        if len(self.q1 and self.q2) == 0:
            print("VOID")
        else:
            print(self.q1)
            print(self.q2)

if __name__ == "__main__":
    platos = platos()

salir = False
while not salir:
    print("\nELEGIR OPCION: \n"
          "1 - Agregar plato favorito de Persona 1. \n"
          "2 - Agregar plato favorito de Persona 2. \n"
          "3 - Mostrar platos en comun.\n"
          "4 - Mostrar todos los platos. \n"
          "6 - Salir. \n")
    op = input("QuE deseas realizar? ")
    match op:
        case "1":
            plato = input("Agrega un plato: ")
            x = 1
            platos.add(plato, x)
        case "2":
            plato = input("Agrega un elemento: ")
            x = 0
            platos.add(plato, x)
        case "3":
            platos.showall()
        case "4":
            platos.showp()
        case "5":
            salir = True