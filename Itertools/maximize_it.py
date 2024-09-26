# Enter your code here. Read input from STDIN. Print output to STDOUT
num,divisor=map(int,input().split())
number=0
for _ in range(num):
    li=list(map(int,input().split()))
    number+=(max(li)**2)
    print(number)
print(number%divisor)