def reverse(x):
 s=0
 while(x>0):
  r=x%10
  s=s*10+r
  x=x/10
 return s
print(reverse(435))