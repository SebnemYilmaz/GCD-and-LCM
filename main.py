def GCD(a,b):
  x=[]
  for i in range(1,min(a,b)+1):
    if a%i== 0 and b%i==0:
      x.append(i)
  print(max(x))

def LCM(n,m):
  t=[]
  for i in range(1,n*m+1):
    if i%n==0 and i%m==0:
      t.append(i)
  print(min(t))

LCM(60,80)



