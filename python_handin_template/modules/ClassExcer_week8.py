import matplotlib.pyplot as plt
import csv
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class ClassEcxer:

    def makeplot():
        data = []
        with open('myNotebooks/weight-height.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter = ',')
            next(lines, None)
            for row in lines:
                if(row[0] == 'Female'):
                    row[0] = 1
                else:
                 row[0] = 2
                if ((row[0]) and (row[1]) and (row[2])):
                    data.append({row[0], float(row[1]), float(row[2])})
                else:
                    break

        x, y, z = zip(*data)
        z = list(map(float, z))
        grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]
        grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        Axes3D.plot_surface(grid_x, grid_y, grid_z, cmap=plt.cm.Spectral, 2)
        print(z)
        plt.show()