n = ''
n = input("INGRESA TU NOMBRE: ")
print(n)

ed = int(input("INGRESA TU EDAD: "))

if ed < 0:
    print("edad no valida")
if ed == 0:
    print("eres un recien nacido")
if ed > 0 and ed < 5:
    print("eres un ninno pequenno")
if ed >= 5 and ed < 10:
    print("eres un ninno")
if ed >= 10 and ed < 18:
    print("eres un puberto")
if ed >= 18 and ed < 30:
    print("eres un adulto joven")
if ed >= 30 and ed < 55:
    print("eres un adulto de mediana edad")
if ed >= 55 and ed < 80:
    print("eres un adulto viejo")
if ed >= 80 and ed < 120:
    print("eres un anciano")
if ed >= 120:
    print("probablemente estes muerto")