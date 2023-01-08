import matplotlib.pyplot as plt

X = []
Y = []

#Lower bound of x and y axes
u = -5


#Creating axes, intervals = 0.1
for i in range(20):
	X.append(u)
	Y.append(u)
	u = u + 0.5

#Make combinations of lists
for m in range(0, 20):
	r = X[m]
	for n in range(0, 20):
		c = Y[n]
		z = complex(r, c)
		s = z**2
		x_result = [s.real]
		y_result = [s.imag]


		#Graph each unique combination
		plt.scatter(x_result, y_result)

plt.show()
