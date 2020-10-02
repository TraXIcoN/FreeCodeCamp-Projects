sub1 = int(input("Enter marks of Subject 1 "))
sub2 = int(input("Enter marks of Subject 2 "))
sub3 = int(input("Enter marks of Subject 3 "))
sub4 = int(input("Enter marks of Subject 4 "))
sub5 = int(input("Enter marks of Subject 5 "))
maxm = int(input("Enter the maximum marks of each subject "))

total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total/5
pc = avg/maxm *  100
print("Total Marks ",total);
print("Percentage ",pc," %");

if pc < 35 : 
  print("Grade F")
elif pc >= 35 and pc < 65 :
  print("Grade C")
elif pc >= 65 and pc < 85 :
  print("Grade B")
elif pc >= 85 :
  print("Grade A");