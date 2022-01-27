n=[12,89,67,34,90,32,54,109]
n.sort()

def binary_search(n,key):

 l=0
 h=len(n)-1
 m=0
 
 while(l<=h):
   m=int((l+h)/2)
   if(key==n[m]):
    return n[m]
   if(key>n[m]):
    l=m+1
   else  :
    h=m-1
 return "Not found"

print(binary_search(n,109))
 
