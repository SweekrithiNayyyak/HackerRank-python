#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j][k]>arr[j+1][k]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    for k in arr:
        for val in k:
            print(val,sep=" ",end=" ")
        print()
        
               
            
