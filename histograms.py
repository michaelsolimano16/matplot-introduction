import matplotlib.pyplot as plt

#Make list of ACT scores
act_scores = [15, 20, 18, 35, 36, 33, 23, 19, 10, 12, 18, 22, 27, 29, 31, 24, 19, 18, 25, 36, 32, 9, 11, 20]

#Assign students an id number (must match ACT scores length)
students = []
for num in range(len(act_scores)):
	students.append(num)

#Plot the ACT scores: x is student id, y is ACT score
plt.bar(students, act_scores)

#labels / titles for our graph
plt.xlabel('Student ID')
plt.ylabel('ACT Score')
plt.title('ACT Score By Student ID Number')
plt.legend()

plt.show()