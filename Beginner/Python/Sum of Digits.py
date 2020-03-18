def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

N = int(input())

a =  []

for i in range (0,N):
  a.append(int(input()))

for y in range (0,N,+1):
  print(sum_digits(a[y]))
