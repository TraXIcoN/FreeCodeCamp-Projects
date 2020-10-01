import sys
import numpy

def optimal_weight(W, w,n):
    '''value=[[0]*(n+1)]*(W+1)'''
    value = numpy.zeros((W+1, n+1))
    
    for i in range(1,W+1):
        for j in range(1,n+1):
            value[i][j]=value[i][j-1]
            if w[j-1]<=i:
                temp=value[i-w[j-1]][j-1]+w[j-1]
            else:
                temp=0
            if temp> value[i][j]:
                value[i][j]=temp

    return(int(value[W][n]))
    

W,n=input().split()
W,n=[int(W),int(n)]
w=[int(x) for x in input().split() ]
print(optimal_weight(W,w,n))
