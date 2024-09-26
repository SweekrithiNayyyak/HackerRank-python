from collections import deque

def sorting(a):
    stack = float('inf')  # Start with an infinitely large value
    a = deque(a)  # Convert the list to a deque for efficient popping from both ends
    
    while a:
        # Choose the larger of the two ends
        if a[0] >= a[-1]:
            chosen = a.popleft()  # Pop from the left end
        else:
            chosen = a.pop()  # Pop from the right end
        
        # If chosen element is larger than the stack's top, it fails
        if chosen > stack:
            return "No"
        
        # Update stack's top to the chosen element
        stack = chosen
    
    return "Yes"

# Reading input and processing each test case
num = int(input())
for i in range(num):
    n = int(input())
    l = list(map(int, input().split()))
    print(sorting(l))
