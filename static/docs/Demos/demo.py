# Clinton Garwood
# Live Demonstration 9/26/2024
# NCC INFS 110 Live Demo File

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, 'bx--')
plt.bar(x, y, color="orange")
plt.title("This is the title")
plt.xlabel("This is the X axis label")
plt.ylabel("These are the doubled values")
plt.grid(True)

plt.savefig('demo_chart.png')
