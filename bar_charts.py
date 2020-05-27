#Create bar charts and histograms w matplotlib
#Using multiplication by 2 vs 2^n as an example

#import matplotlib as an alias
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 8 ,16, 32, 64]

x2 = [1, 2, 3, 4, 5, 6]
y2 = [2, 4, 6, 8, 10, 12]

#create bar charts (note call to bar() instead of plot())
#assign different colors to the bars for distinction
plt.bar(x, y, color='g', label='2^n')
plt.bar(x2, y2, color='c', label='*2')

#Add labels to the axes:
plt.xlabel('Input')
plt.ylabel('Output')

#Add a title to our plot:
plt.title("Multiplication versus Exponents")

#Add a legend with the lables from our plotting above:
plt.legend()

#This shows the plot that was in our background:
plt.show()