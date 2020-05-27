#Make a basic stackplot based on hourly training for tennis

import matplotlib.pyplot as plt

#looking at training input (in weekly hours) for five tennis tournaments
tournament = [1, 2, 3, 4, 5]

training_on_court = [20, 15, 18, 25, 30]
running = [2, 6, 8, 4, 1]
stretching = [1, 4, 2, 5, 6]

#Set labels for plot:
plt.plot([], [], color='g', label='Training on Court')
plt.plot([], [], color='b', label='Running')
plt.plot([], [], color='c', label='Stretching')

#Graph the stackplot:
plt.stackplot(tournament, training_on_court,running,stretching, colors=['g', 'b', 'c'])

plt.xlabel("Tournament Number")
plt.ylabel("Time spent in training attributes")
plt.title("Tennis Training Breakdown")
plt.legend()
plt.show()