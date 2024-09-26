"""
Python/Flask Demo using MatPlotLib
Clinton Garwood, 2024
License: MIT
"""

# This demonstration file follows simple_plot_workflow
import matplotlib.pyplot as plt
print("\nWelcome to MatPlotLib using Python.")

# Step 2: Verify matplotlib success
print("\nMatplotlib is ready.")


def step_3():
    # Step 3: Create a basic plot and plt.show()
    x_list = [1, 2, 3, 4, 5, 6, 7, 8]
    y_list = [1, 4, 9, 16, 25, 36, 49, 64]

    # Create a basic line plot
    plt.plot(x_list, y_list)
    plt.title("Basic Plot of x_list and y_list")
    plt.xlabel("Simple Ascending for x_list")
    plt.ylabel("X Values Doubled for y_list")

    # Show the plot using plt.show()
    plt.show()
    return


def step_4():
    # Step 4: Add style to the chart
    x_list = [1, 2, 3, 4, 5, 6, 7, 8]
    y_list = [1, 4, 9, 16, 25, 36, 49, 64]
    # Change the line style and marker in the chart
    plt.plot(x_list, y_list, 'rx--', label="y = x^2")
    plt.title("Updated Close Plot with Red Line and Legend")
    plt.xlabel("Simple Ascending for x_list")
    plt.ylabel("X Values Doubled for y_list")
    plt.grid(True)  # Add a checkerboard grid behind line
    plt.legend()  # Add a legend to the chart
    plt.show()
    plt.clf()  # Manage Memory (clear figure)
    plt.close()  # Manage Memory (close plot)
    return


def step_5():
    # Step 5: Multiple Charts
    # Generate Data list and list comprehensions
    my_x = [1, 2, 3, 4, 5]
    my_y1 = [i for i in my_x]
    my_y2 = [i**2 for i in my_x]
    my_y3 = [i**3 for i in my_x]

    # Create a figure with subplots
    plt.subplot(3, 1, 1)  # (rows, columns, panel number)
    plt.plot(my_x, my_y1, 'r-', label="y = x")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(my_x, my_y2, 'g-', label="y = x^2")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(my_x, my_y3, 'b-', label="y = x^3")
    plt.legend()

    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.show()  # Render the graph

    # Manage Memory (clear figure and close plot)
    plt.clf()
    plt.close()
    return


def step_6():
    # Step 6: Work with Different Chart Types
    # Data
    x = [1, 2, 3, 4, 5]
    y = [10, 24, 36, 40, 56]

    # Bar chart
    plt.bar(x, y, color='purple', label='Bar Chart')
    plt.xlabel('X Values')
    plt.title('Bar Chart Example')
    plt.ylabel('Y Values')
    plt.legend()
    plt.show()
    # Manage Memory (clear figure and close plot)
    plt.clf()
    plt.close()

    # Scatter plot
    plt.scatter(x, y, color='red', label='Scatter Plot')
    plt.title('Scatter Plot Example')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.legend()
    plt.show()

    # Manage Memory (clear figure and close plot)
    plt.clf()
    plt.close()
    return


def step_7():
    # Step 7: Import numpy and do math plots
    import numpy as np

    x = np.arange(1, 11, 1)
    plt.plot(x, x, label="Linear: O(n)")
    plt.plot(x, np.log(x), label="Logarithmic: O(log n)")
    plt.plot(x, x ** 2, label="Quadratic: O(n^2)")
    plt.plot(x, np.exp(x / 3), label="Exponential: O(2^n)")

    plt.title('Algorithm Growth Rates')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Manage Memory (clear figure and close plot)
    plt.clf()
    plt.close()


def step_8():
    # Step 8: Save the Plot as an image
    import numpy as np

    x = np.arange(1, 11, 1)
    plt.plot(x, x, label="Linear: O(n)")
    plt.plot(x, np.log(x), label="Logarithmic: O(log n)")
    plt.plot(x, x ** 2, label="Quadratic: O(n^2)")
    plt.plot(x, np.exp(x / 3), label="Exponential: O(2^n)")

    plt.title('Algorithm Growth Rates')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.grid(True)
    plt.legend()
    # plt.show()

    # Manage Memory (clear figure and close plot)
    # plt.clf()
    plt.close()

    plt.savefig('growth_rates.png')
    return


def main():
    # Driver for Step Functions
    # step_3()
    # step_4()
    # step_5()
    # step_6()
    # step_7()
    # step_8()
    return


main()
