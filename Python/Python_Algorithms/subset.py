#Printing all the subsets of a string using recursion

#Takes input string
ip = input("Enter the string you want subsets for: ")
op = ""
x = []

def solve(a, b):
    if (len(a) == 0):
        x.append(b)
        return
    else:
        b1 = b
        b2 = b
        b2 = b2 + a[0]
        a = a[1:]
        solve(a, b1)
        solve(a, b2)
        return

solve(ip, op)
x.sort()
#Prints the list of all the subsets of the input string
print(x)
