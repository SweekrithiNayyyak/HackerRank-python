# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
num=set(input().split())
s=set()
for i in num:
    s.add(int(i))

leng=int(input())
for j in range(leng):
    req=input().strip()
    req=req.split()
   
    
    if len(req)<=1:
        s.pop()
        
    
    else:
        a=req[0]
        b=int(req[1])
        #print(a,b)
      
        if a=="remove":
            s.remove(b)
        elif a=="discard":
            s.discard(b)
print(sum(s))
        
