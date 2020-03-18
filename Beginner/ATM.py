


def main():

    S , C = input().split()
    S = int(S)
    C = float(C)


    if S % 5 == 0 and C > (S + 0.5):
        print("{:.2f}".format(C - (float(S) + 0.5)))

    else:
        print("{:.2f}".format(C))

if __name__ == '__main__':
    main()





