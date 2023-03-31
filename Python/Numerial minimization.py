# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:15:14 2023

@author: g361a609
"""

import numpy as np
import matplotlib.pyplot as plt


def my_func(x, y):
    """Define your own 2-dimensional function here"""
    return 5*x**2 + 2*y**2

# Define the x and y ranges
x_range = np.linspace(-3, 3, 65)
y_range = np.linspace(-4, 4, 80)

# Create a meshgrid of the x and y ranges
X, Y = np.meshgrid(x_range, y_range)

# Evaluate the function at each point on the meshgrid
Z = my_func(X, Y)

# Plot the function as a 3D surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# Use the minimize function from scipy to find the minimum of the function
from scipy.optimize import minimize

# Define the starting point
x0 = np.array([1.0, 1.0])

# Use the minimize function from scipy to find the minimum of the function
res = minimize(lambda x: my_func(x[0], x[1]), x0, method='nelder-mead', options={'xatol': 1e-8, 'disp': True})

# Print the results
print(res.x)

# Plot the minimum point on the surface plot
ax.scatter(res.x[0], res.x[1], my_func(res.x[0], res.x[1]), c='r', marker='o')
plt.show()