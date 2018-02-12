import numpy as np
import matplotlib.pyplot as plt

N=5
A=np.array((3,9,22,2,6))
B=np.array((9,6,4,0.5,2))
C=np.array((12,17,1,19,6))
D=np.array((14,4,5,12,6))
E=np.array((1,12,2,18,8))

ind = np.arange(N)    # the x locations for the groups
width = 0.5       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, A, width,color = 'blue')
p2 = plt.bar(ind, B, width,bottom=A,color = 'green')
p3 = plt.bar(ind, C, width,bottom=A+B,color = 'yellow')
p4 = plt.bar(ind, D, width,bottom=A+B+C,color = 'orange')
p5 = plt.bar(ind, E, width,bottom=A+B+C+D,color = 'red')

plt.title('user activity')
plt.xticks(ind, ('M', 'T', 'W', 'Th', 'F'))
plt.yticks(np.arange(0, 61, 10))
plt.legend((p1[0], p2[0],p3[0],p4[0],p5[0]), ('A', 'B','C','D','E'))

plt.show()

