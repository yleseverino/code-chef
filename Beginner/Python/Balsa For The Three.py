for i in range (int(input())):
  n = int(input())
  while (True):
    n +=1
    l =  [int (d) for d in str(n)]
    if l.count(3) >= 3:
      print(n)
      break