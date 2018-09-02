for i in range(int(input())):
  n = int(input())
  h = 0
  while(True):
    if n - h <= 0:
      break
    h +=1
    n = n - h
  print(h)