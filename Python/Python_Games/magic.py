from turtle import Turtle 
input('Press any key to start the magic...') 
t = Turtle() 
t.speed(0) 
a = 180 
b = 180 
for c in range(5): 
 	a = 9*c 
 	for i in range(100): 
 		t.circle(i,a) 
 		t.right(b) 
 		t.circle(i,a) 
 		t.right(b) 
 		t.circle(i,a) 
 		t.right(b) 
 		t.circle(i,a) 
