n=[23,78,90,65,12,67]


def maximum(n):
 max=n[0]
 for i in range(len(n)):
  
  if max<n[i]:
    max=n[i]
 return max

def minmum(n):
 min=n[0]
 for i in range(len(n)):
  if min>n[i]:
    min=n[i]
 return min

print(maximum(n))
print(minmum(n))