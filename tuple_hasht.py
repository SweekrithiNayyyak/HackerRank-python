# Enter your code here. Read input from STDIN. Print output to STDOUT
import builtins
n=input()
t=tuple(map(int,input().strip().split()))
print(builtins.hash(t))
