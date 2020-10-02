#!/usr/bin/env python
# coding: utf-8

# In[37]:


dict = {}
dict = {
    123001:{'student_name': 'Ankita','student_rollno': 1, 'student_age': 12, 'student_marks': [98,78,86,95,67]},
    123002:{'student_name': 'Rahul','student_rollno': 2, 'student_age': 13, 'student_marks': [56,46,76,65,77]},
    123003:{'student_name': 'Sakshi','student_rollno': 3, 'student_age': 14, 'student_marks': [94,72,81,93,64]},
    123004:{'student_name': 'Aakash','student_rollno': 4, 'student_age': 12, 'student_marks': [58,42,53,55,77]},
    123005:{'student_name': 'Sahil','student_rollno': 5, 'student_age': 13, 'student_marks': [88,71,82,90,80]},
}
dict


# In[38]:


max = 0
min = 100
k = 0
individual_avg = []
for i in dict:
    dict[i]['Avg_marks'] = []
    for j in range (0,5):    
        individual_sum = sum(dict[i]['student_marks'])
        if dict[i]['student_marks'][j] > max :
            max = dict[i]['student_marks'][j]
            maxi = i
        if dict[i]['student_marks'][j] < min :
            min = dict[i]['student_marks'][j]
            mini = i
    individual_avg.append(individual_sum / 5)
    dict[i]['Avg_marks'] = individual_avg[k]
    k += 1
print("Student Details with Maximum Marks : ", maxi, dict[maxi])
print("Student Details with Minimum Marks : ", mini, dict[mini])


# In[39]:


total_sum = sum(individual_avg)
total_avg = total_sum / 10

print("Average Marks : ", total_avg)
for i in dict:
    if total_avg < dict[i]['Avg_marks']:
        print("Students scoring above Average : ")
        print(i, dict[i])


# In[ ]:




