import numpy as np

numbers = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(numbers)


xint= np.arange(1, 7)
yint= np.arange(5, 11)
print(xint)
print(yint)


import matplotlib
print(matplotlib.__version__)


import matplotlib.pyplot as plt



import matplotlib.pyplot as plt
import numpy as np

plt.plot(xint, yint)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([1,2,3,4,5])
y2 = np.array([5,6,7,8,9])
y3 = np.array ([9,10,11,12,13])

plt.plot(y1)
plt.plot(y2)
plt.plot(y3)

plt.xlabel("X Label")
plt.ylabel("Y Label")

plt.show()


import matplotlib.pyplot as plt
import numpy as np

#plot 1:
xpoints = np.array([1,2,3,4])
ypoints = np.array([1,2,3,4])

plt.subplot(2,3,1)
plt.plot(xpoints, ypoints, marker = 'D', linewidth = '4')

plt.title("Simple Plot")

#plot 2:
y1 = np.array([12, 14, 17, 20])
y2 = np.array([20, 10, 15, 10])
y3 = np.array([0, 20, 17, 5])

plt.subplot(2,3,2)
plt.plot(y1, marker = 'o')
plt.plot(y2, marker = '*')
plt.plot(y3, marker = 'o')

plt.title("Complex Plot")


#plot 3:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([0, 1, 4, 9])
x2 = np.array([0, 2, 4, 6])
y2 = np.array([0, 4, 8, 12])

plt.subplot(2,3,3)
plt.plot(x1, y1, x2, y2, linewidth = '10')
plt.grid()

plt.title("Intermediate Plot")
plt.xlabel("Base Value")
plt.ylabel("Mathematical Function")


font1 = {'family': 'serif', 'color': 'red', 'size': 20}
plt.suptitle("SUBPLOTS", fontdict = font1)
plt.show()


