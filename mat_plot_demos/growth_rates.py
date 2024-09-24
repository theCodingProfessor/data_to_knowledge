import matplotlib.pyplot as plt
import os
import numpy as np
import math


def slower_rates():
    return


def faster_rates():
    return


def select_rates():
    # Define data range (e.g., size of input)
    n = np.arange(1, 10)  # X-axis values, from 1 to 20

    # Complexity functions
    complexities = {
        'Factorial O(n!)': np.array([math.factorial(i) for i in n]),  # O(n!)
        'Exponential O(2^n)': 2 ** n,  # O(2^n)
        'Quadratic O(n^2)': n ** 2,  # O(n^2)
        # 'Linearithmic O(n log n)': n * np.log(n),  # O(n log n)
        # 'Linear O(n)': n,  # O(n)
        # 'Logarithmic O(log n)': np.log(n),  # O(log n)
        # 'Constant O(1)': np.ones_like(n),  # O(1)
        # 'Cubic O(n^3)': n ** 3,  # O(n^3)
    }

    # Plotting each growth rate
    plt.figure(figsize=(10, 6))

    for label, complexity in complexities.items():
        plt.plot(n, complexity, label=label)

    # Labeling the chart
    plt.title("Growth Rates of Common Algorithms", fontsize=16)
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Operations", fontsize=12)
    plt.yscale('log')  # Logarithmic scale to better visualize exponential growth
    plt.grid(True)

    # Adding a legend
    plt.legend()

    # Save the plot to a static file

    # File path/name for the image
    image_path = os.path.join('../static/img', 'grow_fastest.png')

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()


def growth_rates():
    # Define data range (e.g., size of input)
    n = np.arange(1, 21)  # X-axis values, from 1 to 20

    # Complexity functions
    complexities = {
        'Constant O(1)': np.ones_like(n),  # O(1)
        'Logarithmic O(log n)': np.log(n),  # O(log n)
        'Linear O(n)': n,  # O(n)
        'Linearithmic O(n log n)': n * np.log(n),  # O(n log n)
        'Quadratic O(n^2)': n ** 2,  # O(n^2)
        'Cubic O(n^3)': n ** 3,  # O(n^3)
        'Exponential O(2^n)': 2 ** n,  # O(2^n)
        'Factorial O(n!)': np.array([math.factorial(i) for i in n]),  # O(n!)
    }

    # Plotting each growth rate
    plt.figure(figsize=(10, 6))

    for label, complexity in complexities.items():
        plt.plot(n, complexity, label=label)

    # Labeling the chart
    plt.title("Growth Rates of Common Algorithms", fontsize=16)
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Operations", fontsize=12)
    plt.yscale('log')  # Logarithmic scale to better visualize exponential growth
    plt.grid(True)

    # Adding a legend
    plt.legend()

    # Save the plot to a static file

    # File path/name for the image
    image_path = os.path.join('../static/img', 'growth_rates.png')

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()
    return


def test_suite():
    # slower_rates()
    # faster_rates()
    select_rates()
    # growth_rates()
    return


test_suite()
