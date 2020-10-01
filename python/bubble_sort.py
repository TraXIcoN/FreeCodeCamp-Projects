
def bubblesort(a):
  n = len(a)
  for i in range(n):
    for j in range(n-1):
      if a[j]>a[j+1]:
        a[j],a[j+1] = a[j+1],a[j]
  return a

a = list(map(int, input().strip().split(' ')))
a = bubblesort(a)
