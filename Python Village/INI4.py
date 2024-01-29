a = int(input('a = '))
b = int(input('b = '))
suma = 0

for i in range(a, b+1):
        if i % 2 != 0:
            suma = suma + i

print(f"La suma de números pares entre {a} y {b} es: {suma}")

