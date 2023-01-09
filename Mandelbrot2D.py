import matplotlib.pyplot as plt

X = []
Y = []

x_result = []
y_result = []

#Lower bound of x and y axes
u = -2

def quadratic(l):
    w = l
    for i in range(10):
        w = w*w + l
    return w

#Creating axes, intervals = 0.04
for i in range(100):
    X.append(u)
    Y.append(u)
    u = u + 0.04

#Make combinations of lists
for m in range(0, 100):
    r = X[m]
    for n in range(0, 100):
        c = Y[n]
        z = complex(r, c)
        # Checks if iterating makes the number spiral out to infinity; uses standard test for this (checks if consecutive iterations yield a number that exceeds 2).
        if abs(quadratic(z)) <= 2:
            plt.scatter(r, c)

plt.xlim(-1.6, 1.6)
plt.ylim(-0.9, 0.9)
plt.show()
