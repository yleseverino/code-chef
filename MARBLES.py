def fac (N,K):
  a = 1
  b = 1
  for h in range(1,K):
    a = a*(n -h)
    b = b*h
  return int(a/b)

for i in range(int(input())):
  n,p = map(int,input().split())
  if p > n - p:
    p = n-p+1
  temp = n-p
  print(int(fac(n,p)))



  def comb(n,k):
    s=max(n-k,k)
    num,den=1,1
    for i in range(s+1,n+1):
        num*=i
    for i in range(2,min(n-k,k)+1):
        den*=i

    return num//den
def main():
  t = int(input())
  for i in range(t):
    n, r = [int(i) for i in input().split()]
    print(comb(n-1, r-1))

if __name__ == '__main__':
  main()
