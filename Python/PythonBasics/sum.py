a = int(input("Enter 1st Number"))
b = int(input("Enter 2st Number"))

try:
  ## make sure if a, b are number
  for e in [a, b]:
    assert type(e) in [int, float]
  c = a + b

  if c <= 20 :
    print("no operation performed")
  elif c > 20 and c <= 40 :
    print("product is ",(a*b))
  elif c > 40 and c <= 60 :
    print("difference is ",(a-b))
  else :
    print("sum is ",c)
except:
  print("invalid input")