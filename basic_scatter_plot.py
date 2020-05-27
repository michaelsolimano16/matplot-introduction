#Make a basic scatterplot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [7, 14, 21, 28, 35, 42, 49, 56]

#Scatter the multiples of 7. Assign color to cyan.
#There are other arguments we can add like size and marker
plt.scatter(x, y, color='c')

plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Mutliples of Seven')
plt.show()