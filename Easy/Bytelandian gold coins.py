dic = {}
def maxValue(N):
  if N<12:
    return N
  else:
    try:
      return dic[N]
    except KeyError:
      bestvalue=maxValue(N//2)+maxValue(N//3)+maxValue(N//4)
      bestvalue=max(bestvalue,N)
      dic[N]=bestvalue
      return bestvalue

while True:
  try:
    N = int (input())
    print(maxValue(N))
  except:
    break
  
    