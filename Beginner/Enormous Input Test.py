N, K = input().split()

N = int(N)
K = int(K)
temp = 0

lista = []

for i in range(N):
    lista.append(int(input()))
    if lista[i] % K == 0:
        temp = temp + 1

print(temp)