# Enter your code here. Read input from STDIN. Print output to STDO
from collections import deque
queue=deque()
n=int(input())
for _ in range(n):
    inl=input().split()
    # print(inl)
    a=inl[0]
    if a=='pop':
        queue.pop()
    elif a=="popleft":
        queue.popleft()
    
    elif a=='append':
        num=inl[1]
        queue.append(num)
    elif a=='appendleft':
        num=inl[1]
        queue.appendleft(num)
for i in queue:
    print(i,end=" ")
