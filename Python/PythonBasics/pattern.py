n = int(input("Enter n "))

for x in range(0, n) :
  for y in range(x,-1,-1) :
    print(2**y, end = " ")
  print()
