def is_leap(year):
    if (year%400==0) or((year%100!=0)and (year%4==0)):
        return(True)
    
    else:
         return(False)
    
    # Write your logic here
    


year = int(input())