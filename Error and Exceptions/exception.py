# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        
        try:
            a,b= map(int,input().split())
            print(int(a/b))
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print(f"Error Code: {e}")