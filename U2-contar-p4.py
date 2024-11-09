#4 t
z=[]
x=0
y=input("INGRESAR VALORES: ")
z.extend(y.split(","))
print(z)

ii=0
nm= 0
r=0
for n in z:
    ii=z.count(n)
    if ii>r:
        r=ii
        nm=n
print(nm)
print(r)