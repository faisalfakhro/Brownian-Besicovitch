import numpy as np
import matplotlib.pyplot as plt

k = 1000
printcoords = False

# store x and y coordinates of random walk, starting at origin
x = [0]
y = [0]

bes = [0] # coordinates for besocovitch set contruction
ymax = 0 # max y value reached so far
triangles = [] #triangles making up besicovitch set

#simulate random walk
direc = [[1, 0], [-1,0], [0,1], [0,-1]]
i = 0
while y[i] < k-1:
    i += 1
    delta = direc[np.random.randint(0,4)]
    
    x.append(x[-1] + delta[0])
    y.append(y[-1] + delta[1])

    if y[-1] > ymax:
        ymax = y[-1]
        bes.append(x[-1])


if printcoords:
    #print coordinates of entire random walk
    for a,b in zip(x,y):
        print("%d, %d" % (a, b))

    #print coordinates of new y-maxima
    for (i,v) in enumerate(bes):
        print("%d, %d" % (v, i))

#draw walk
plt.figure(0)
plt.plot(x,y)
plt.scatter(bes, range(k), color='red')
plt.show()
plt.figure(1)

#build besicovitch set
u = np.random.randint(0, k)
for (i, z) in enumerate(bes):
    triangles.append([])
    zm = (u + z) % k

    #bottom point of triangle z_m / n
    triangles[-1].append([zm/k, 0])

    #point (z_m - m) / n of triangle
    triangles[-1].append([(zm - i)/k, 1])

    #point (z_m - m - 1) / n of triangle
    triangles[-1].append([(zm - i - 1)/k, 1])

#plot besicovitch set
for (i, t) in enumerate(triangles):
    tri = plt.Polygon(t, edgecolor='black')
    plt.gca().add_patch(tri)

print("at end")
plt.xlim([-1,1])
plt.show()