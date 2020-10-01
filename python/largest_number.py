# your code goes here#Uses python3

import sys

def largest_number(a):
	used = [0]*len(a)
	res = ""
	maxd = -1
	while 0 in used: 
		maxd = 0
		for i in range(len(a)):
			if better_value(a[i],maxd) and used[i]==0:
				maxd = a[i]
				index = i
		used[index]	=1	
		res+=str(maxd)
	return res			










    


def better_value(x,y):
	a = str(x)
	b = str(y)
	temp=b
	b+=a
	a+=temp
	
	if int(a)>int(b):
		return True
	return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
