N = int(input())
a = []
t1 = 0
t2 = 0
for i in range (N):
    t1,t2 = input().split()
    t1 = int(t1)
    t2 = int(t2)
    t1 = t1 + t2
    a.append(t1)
for y in range (N):
    print(a[y])