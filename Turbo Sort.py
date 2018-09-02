n = int(input())

lista = []
for i in range (n):
    lista.append(int(input()))

lista.sort()

for y in range(n):
    print(lista[y])