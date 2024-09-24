import os

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute areas and colors
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta

fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

# Citation to MatPlotLib for the source code
plt.text(0.5, -.1, 'Text Box Style: https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_scatter.html#sphx-glr-gallery-pie-and-polar-charts-polar-scatter-py', ha='center', va='center', fontsize=5, transform=plt.gca().transAxes)

# Show the plot
plt.grid(True)

# File path/name for the image
image_path = os.path.join('../static/img', 'scatter_polar_demo.png')

# Save image to the static/images directory
plt.savefig(image_path)
plt.close()
