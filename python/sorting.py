

def partition3(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r ):
        if a[i] <= x:
            a[i], a[j+1] = a[j+1], a[i]
            j += 1
    a[l],a[j] = a[j], a[l]
    k=1
    for i in range(l,j):
        if a[i] <a[j]:
            a[i], a[k]= a[k], a[i]
            k+=1
    a[l], a[j] = a[j], a[l]
    return k,j

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    
    '''m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);'''

    n1,n2= partition3(a,l,r)
    randomized_quick_sort(a, l, n1);
    randomized_quick_sort(a, n2+1, r);


n=int(input())
a=[int(x) for x in input().split()]
randomized_quick_sort(a, 0, n-1 )
for x in a:
    print(x, end=' ')
