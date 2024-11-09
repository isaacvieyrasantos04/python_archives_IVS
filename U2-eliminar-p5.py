#5 t
z=[]
for i in range(5):
        print("Ingresa los valores: ")
        z.extend(input())
print(z)

ii=0
nm= 0
r=0
for num in z:
    ii=z.count(num)
    if ii>r:
        r=ii
        nm=num

    print(nm)
    print(r)

for num in z:
    if num==nm:
        z.remove(num)

print(z)