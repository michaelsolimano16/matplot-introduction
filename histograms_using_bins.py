import matplotlib.pyplot as plt

#Make list of ACT scores
act_scores = [15, 20, 18, 35, 36, 33, 23, 19, 10, 12, 18, 22, 27, 29, 31, 24, 19, 18, 25, 36, 32, 9, 11, 20]

#Instead of student id's, create bins to get a different look at the data
#Here, we'll use ACT scores broken into sextiles
score_buckets = [0, 6, 12, 18, 24, 30, 36]


#Plot the ACT scores in a histogram
#we assign histtype to bar histogram
plt.hist(act_scores, score_buckets, histtype='bar')

#labels / titles for our graph
plt.xlabel('ACT Score')
plt.ylabel('Students within Range')
plt.title('ACT Scores for Population of Students')

plt.show()