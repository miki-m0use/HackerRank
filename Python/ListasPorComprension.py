# x = int(input("Enter value for x: "))
# y = int(input("Enter value for y: "))
# z = int(input("Enter value for z: "))
# n = int(input("Enter value for n: "))

x = 2
y = 2
z = 2
n = 2


resp = [[i, j, z1] for i in range(x+1) for j in range(y+1)
        for z1 in range(z+1) if i + j + z1 != n]

print(resp)
