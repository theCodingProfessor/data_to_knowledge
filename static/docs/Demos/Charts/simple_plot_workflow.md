
## Simple Plotting Workflow

Description: 

This workflow is designed to help explain the fundamentals of plotting in Python with Matplotlib, and covers simple graph types and styles.

The step-by-step workflow will help you gain skills with Python and Matplotlib for graphing data.

### **Step-by-Step Workflow for a Simple Python and Matplotlib Graphing Project**

1. Install Python and Set Up Environment
2. Install Required Libraries
3. Introduction to Plotting in Matplotlib
4. Adding Styles and Labels
5. Creating Subplots
6. Plotting Multiple Types of Graphs
7. Adding Math Functions
8. Save the Plot as an Image
9. Combine Everything into a Final Project
10. Encourage Exploration
11. Polish and Present Results

---

### **1. Install Python and Set Up Environment**
**Goal:** Ensure that the Python environment is ready for use with `matplotlib`.

- **Install Python**: Download and install the latest version of Python from [python.org](https://www.python.org/downloads/).
- **Install PyCharm or VSCode**: Select an IDE like [PyCharm](https://www.jetbrains.com/pycharm/) or [VSCode](https://code.visualstudio.com/) for coding.
- **Set up Virtual Environment (Optional)**:
    ```bash
    python -m venv graphing_env
    ```
    Activate the virtual environment (in the terminal):
    - **Windows**:
        ```bash
        graphing_env\Scripts\activate
        ```
    - **Mac/Linux**:
        ```bash
        source graphing_env/bin/activate
        ```

### **2. Install Required Libraries**
**Goal:** Install `matplotlib` and any other necessary libraries.

- **Install Matplotlib using `pip`**:
    ```bash
    pip install matplotlib
    ```

- Verify the installation by importing it in Python:
```python
import matplotlib.pyplot as plt
print("Matplotlib is ready!")
```

### **3. Introduction to Plotting in Matplotlib**
**Goal:** Create a basic plot.

- Create a simple Python script (e.g., `basic_plot.py`):

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a basic line plot
plt.plot(x, y)

# Add title and labels
plt.title('Basic Line Plot: y = x^2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
```

- **Explanation**:
  - The `x` list contains the x-values.
  - The `y` list contains the y-values (square of x in this case).
  - `plt.plot(x, y)` creates the graph.
  - `plt.show()` displays it.

### **4. Adding Styles and Labels**
**Goal:** Enhance the plot by adding styles, labels, and other visual elements.

- **Customize the plot**:
```python
plt.plot(x, y, 'bo-', label="y = x^2")  # blue circles and lines
plt.title('Customized Line Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)
plt.legend()  # Add a legend
plt.show()
```

- **Explanation**:
  - `'bo-'` changes the style to blue circles connected by lines.
  - `plt.grid(True)` adds a grid.
  - `plt.legend()` shows the line's label in a legend.

### **5. Creating Subplots**
**Goal:** Display multiple plots in one figure.

- **Example:**
```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

# Create a figure with subplots
plt.subplot(3, 1, 1)  # (rows, columns, panel number)
plt.plot(x, y1, 'r-', label="y = x")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(x, y2, 'g-', label="y = x^2")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(x, y3, 'b-', label="y = x^3")
plt.legend()

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
```

- **Explanation**:
  - `plt.subplot(3, 1, 1)` creates a 3-row, 1-column grid of subplots.
  - Each subplot displays a different mathematical function.

### **6. Plotting Multiple Types of Graphs**
**Goal:** Discover different types of graphs (line, bar, scatter, etc.).

- **Example of Bar and Scatter Plots**:
```python
import matplotlib.pyplot as plt

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

# Scatter plot
plt.scatter(x, y, color='red', label='Scatter Plot')
plt.title('Scatter Plot Example')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.show()
```

- **Explanation**:
  - `plt.bar()` generates a bar chart.
  - `plt.scatter()` generates a scatter plot.

### **7. Adding Math Functions**
**Goal:** Visualize mathematical functions (like growth rates).

- **Example: Exponential, Logarithmic, etc.**:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11, 1)
plt.plot(x, x, label="Linear: O(n)")
plt.plot(x, np.log(x), label="Logarithmic: O(log n)")
plt.plot(x, x**2, label="Quadratic: O(n^2)")
plt.plot(x, np.exp(x/3), label="Exponential: O(2^n)")

plt.title('Algorithm Growth Rates')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.grid(True)
plt.legend()
plt.show()
```

### **8. Save the Plot as an Image**
**Goal:** Save the plot to a file.

- **Saving the plot**:
```python
plt.savefig('growth_rates.png')
```

- **Explanation**:
  - `plt.savefig('filename.png')` saves the plot as an image.

### **9. Combine Everything into a Final Project**
**Goal:** Bring all the knowledge together in a presentation.

- **Example Task**:
  - Create multiple subplots for different types of functions.
  - Add titles, labels, and legends.
  - Save the final graph as an image file.

### **10. Explore More**
**Goal:** Explore advanced options and different data.

- **Try out different matplotlib styles**: 
```python
plt.style.use('ggplot')  # Use ggplot style
```

- **Explore 3D plotting**:
```python
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, zs=0, zdir='z')
```

### **11. Polish and Present Results**
**Goal:** Review your code and tell the story.

Key Deliverables:
- A Python script (e.g., `final_graph.py`) that generates a graph.
- A saved plot (e.g., `final_plot.png`).

### **Key Learning Outcomes**
- Basic Python and Matplotlib skills.
- Understanding data visualization using different plot types.
- Hands-on practice creating, customizing, and saving graphs.

---
