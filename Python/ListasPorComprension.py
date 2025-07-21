x = int(input())
y = int(input())
z = int(input())
n = int(input())


x += 1
y += 1
z += 1


respuesta = [[i, j, z1] for i in x for j in y for z1 in z if i + j + z1 != n]

print(respuesta)
