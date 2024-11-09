#12 t
class cursos:
    def __init__(self):
        self.prog = set()
        self.reds = set()

    def add(self, a, c):
        if c == 1:
            self.prog.add(a)
        else:
            self.reds.add(a)

    def showall(self):
        if len(self.prog and self.reds) == 0:
            print("No hay elementos. ")
        else:
            print(self.prog | self.reds)

    def showprg(self):
        if len(self.prog) == 0:
            print("No hay elementos. ")
        else:
            print(self.prog)

    def showred(self):
        if len(self.reds) == 0:
            print("No hay elementos. ")
        else:
            print(self.reds)

if __name__ == "__main__":
    cursos = cursos()

salir = False
while not salir:
    print("\nELEGIR OPCION: \n"
          "1 - Agregar alumno a Programacion. \n"
          "2 - Agregar alumno a Redes. \n"
          "3 - Mostrar alumnos en ambos cursos.\n"
          "4 - Mostrar alumnos de Programacion.\n"
          "5 - Mostrar alumnos de Redes.\n"
          "6 - Salir. \n")
    op = input("QuE deseas realizar? ")
    match op:
        case "1":
            alumno = input("Agrega elemento: ")
            x = 1
            cursos.add(alumno, x)
        case "2":
            alumno = input("Agrega elemento: ")
            x = 0
            cursos.add(alumno, x)
        case "3":
            cursos.showprg()
        case "4":
            cursos.showall()
        case "5":
            cursos.showall()
        case "6":
            salir = True