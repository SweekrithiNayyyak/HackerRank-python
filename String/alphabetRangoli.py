def print_rangoli(size):
    # your code goes here
    n=2*size-1
    st=1
    sp=2*size-2
    sp2=0
    
    for i in range(n):
        dummy=97+size-1
        for j in range(sp):
            print("-",end="")
        for k in range(st):
            if k==st-1:
                print(chr(dummy),end="")
            else:
                print(chr(dummy),end="-")
            if k<st//2:
                dummy-=1
            else:
                dummy+=1
        for j in range(sp):
            print("-",end="")
        if i<n//2:
            sp-=2
            st+=2
        else:
            sp+=2
            st-=2
        print()
            
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)