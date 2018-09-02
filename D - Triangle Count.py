for i in range(1, int(input()) + 1, 1):
    N, L = map(int, input().split())
    temp = 0
    if N >= L:
        temp = N - L + 1
        temp = (temp * (temp + 1) // 2)
    print("Case {}: {}".format(i, int(temp)))
