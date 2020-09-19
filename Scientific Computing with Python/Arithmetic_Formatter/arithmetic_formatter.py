def arithmetic_arranger(problems):
  temp1a,temp2a = [], []
  for i in problems:
    temp1,op,temp2 = i.split()
    if len(temp1) > len(temp2):
      temp1a.append(" " + temp1)
      temp2a.append(op +" " + " "*(len(temp1)-len(temp2)-1) +  temp2)
    else:
      temp1a.append(" " + " "*(len(temp2) - len(temp1) + 1) +  temp1)
      temp2a.append(op + " " +  temp2)
  for i in range(len(temp1a)):
    if i < len(temp1a) -1:
      print(temp1a[i], end="    ")
    else:
      print(temp1a[i])
  for j in range(len(temp2a)):
    if j < len(temp1a) -1:
      print(temp2a[j], end="    ")
    else:
      print(temp2a[j])
  for k in temp2a:
    print("-"*len(k),end="    ")
  return ''