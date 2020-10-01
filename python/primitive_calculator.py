# Uses python3
import sys
    
def optimal_sequence(n):
    sequence = [None]*(n+1)
    sequence[0] = 0
    sequence[1] = 0
    if n >=2 :
        for i in range(2,n+1) :
            if(i/2 == i//2 and i/3 == i//3):
                sequence[i] = min (sequence[i//2],sequence[i//3],sequence[i-1])+1
            elif(i/2 == i//2 and  not (i/3 == i//3)):
                sequence[i] =min (sequence[i//2],sequence[i-1]) +1
            elif(not (i/2 == i//2) and  i/3 == i//3):
                sequence[i] = min (sequence[i//3],sequence[i-1])+1
            else :
                sequence[i] = sequence[i-1] +1 
    items = list()
    items.append(n)
    while n>1:
        if(n/3 == n//3 and sequence[n//3] ==sequence[n]-1)  :
            items.append(n//3)
            n = n//3
        elif(n/2 == n//2 and sequence[n//2] ==sequence[n]-1)  :
            items.append(n//2)
            n = n//2
        else:
            items.append(n-1)
            n-=1
    return sequence[-1],reversed(items)         

input = sys.stdin.read()
n = int(input)
n1,items = (optimal_sequence(n))
print(n1)
for x in items :
    print(x, end=' ')
