

def majority_element(a, l, r):
    if l+1==r:
        return a[l]
    elif l+2==r:
        return a[l]
    m = (l+r)//2
    left = majority_element(a, l, m)
    right = majority_element(a, m, r)

    c1, c2 = 0, 0
    for i in a[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else: 
        return -1
n = int(input())
a = [int(i) for i in input().split()]
print(int(majority_element(a, 0, n) != -1))
