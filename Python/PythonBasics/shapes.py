import math
print("Choose from Circle(C), Rectangle(R), Triangle(T)")
shape = input("Enter the character corresponding to the shape ")

if shape == "C" :
  r = float(input("Enter the radius of the circle"))
  print("Perimeter is ",(2 * math.pi * r))
  #math.pi = 3.141592
  print("Area is ",(math.pi * r * r))

elif  shape == "R" :
  l = float(input("Enter the length of the rectangle"))
  b = float(input("Enter the breath of the rectangle"))
  print("Perimeter is ",(2*(l+b)))
  print("Area is ",(l * b))

elif shape == "T" :
  h = float(input("Enter the height of the triangle"))
  b = float(input("Enter the base of the trianlge"))
  s = math.sqrt(h**2 + b**2)
  print("Perimeter is ",(s + s + b))
  print("Area is ",(1/2)*h*b)