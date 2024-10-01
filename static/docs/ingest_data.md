
## Data Ingestion Demonstration 

This activity provides a **similar workflows** for working with data in ** Excel and Python**.
The process is designed to strengthen foundational skills in data management and visualization techniques.

Process for **ingesting data** into either an **Excel sheet** or a **Python app** includes the following:

- **Grabbing a dataset**
- **Exploring the dataset**
- **Choosing a visualization**
- **Plotting and presenting the data**

Either/both Excel and Python can be used to manage, explore, and visualize data.

---

### Activity Title: Data Ingestion and Visualization using Excel and Python

#### Objective:
- Understand how to ingest data into Excel and Python
- Explore a dataset and perform basic data cleaning
- Choose an appropriate visualization based on the data
- Generate a graph and present findings

### Step 1: Grab a Dataset

**Instructions**:
1. Go to an open data repository, such as [Kaggle Datasets](https://www.kaggle.com/datasets), [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php), or [Data.gov](https://data.gov/).
2. Download a small CSV dataset that interests you. Suggested datasets:
   - World population growth by country
   - CO2 emissions by country
   - Global temperature change data
   
3. Save the dataset to your local machine.

**Deliverable**: Submit a brief description of the dataset, including the source and an outline of the key variables (columns) in the data.

---

### Step 2: Explore the Data

#### A) **Excel Workflow**:
1. **Open Excel** and import the CSV dataset by navigating to `File > Open > Browse` and selecting the CSV file.
2. **Data Cleaning**: 
   - Identify and remove any null or missing data. (e.g., highlight the column and use `Filter` to find empty cells)
   - Format the data as a table using `Insert > Table`.
   
3. **Explore** the dataset:
   - Use basic formulas like `=AVERAGE()`, `=SUM()`, and `=COUNT()` to understand key aspects of the data.
   - Generate a **Pivot Table** to further analyze the data if necessary.
   
#### B) **Python Workflow**:
1. **Python Setup**:
   - Open a Python project in PyCharm (or any Python IDE).
   - Install any necessary packages (`pandas`, `matplotlib`, and optionally `seaborn`):
     ```bash
     pip install pandas matplotlib seaborn
     ```

2. **Ingest Data**:
   - Use `pandas` to load the CSV file:
     ```python
     import pandas as pd

     data = pd.read_csv('path_to_your_csv_file.csv')
     ```

3. **Explore the Data**:
   - Print the first few rows to inspect the structure:
     ```python
     print(data.head())
     ```
   - Check for missing values and basic statistics:
     ```python
     print(data.info())  # Check for null values
     print(data.describe())  # Summary statistics
     ```

4. **Optional Data Cleaning**:
   - Drop rows with missing values:
     ```python
     data.dropna(inplace=True)
     ```

---

### Step 3: Choose a Visualization

#### A) **Excel Workflow**:
1. **Choose a Chart Type**:
   - Based on the dataset, decide whether a **bar chart**, **line chart**, or **scatter plot** would be appropriate. For example:
     - **Line Chart**: If you're showing trends over time (e.g., temperature change).
     - **Bar Chart**: If you're comparing categories (e.g., CO2 emissions by country).
     
2. **Create a Chart**:
   - Highlight the relevant data columns and select `Insert > Charts` to create a chart.
   
3. **Customize the Chart**:
   - Add titles, labels, and adjust the design to improve readability.

#### B) **Python Workflow**:
1. **Choose a Chart Type**:
   - Use `matplotlib` or `seaborn` to create a chart. Based on the dataset, decide between:
     - **Line Plot**:
       ```python
       import matplotlib.pyplot as plt
       
       plt.plot(data['Year'], data['Temperature Change'])
       plt.title('Global Temperature Change Over Time')
       plt.xlabel('Year')
       plt.ylabel('Temperature Change')
       plt.grid(True)
       plt.show()
       ```

     - **Bar Plot**:
       ```python
       import seaborn as sns
       
       sns.barplot(x='Country', y='CO2 Emissions', data=data)
       plt.title('CO2 Emissions by Country')
       plt.xticks(rotation=90)  # Rotate labels for readability
       plt.show()
       ```

2. **Customize the Plot**:
   - Use labels, titles, and grids to enhance the visualization.

---

### Step 4: Present Your Findings

1. **Generate the Graph**:
   - For **Excel**, take a screenshot or export the chart using `File > Save As` to save as an image.
   - For **Python**, save the plot using:
     ```python
     plt.savefig('path_to_save_plot.png')
     ```

2. **Create a Brief Summary**:
   - Provide a brief summary explaining:
     - What the data represents
     - Why you chose the particular graph type
     - Key insights from the visualization

---

### Key Takeaways:

- Both **Excel** and **Python** offer powerful tools for ingesting, exploring, and visualizing data, but they cater to different needs. 
  - **Excel** is more intuitive and user-friendly for basic data manipulation and visualization.
  - **Python** offers more flexibility, scalability, and power for complex data analysis.

- This activity provides a pathway:
  - Understand how to import and clean data in both Excel and Python.
  - Explore and analyze the dataset to gain insights.
  - Select and create appropriate visualizations to represent the data.

---


Data Set Links from https://data.un.org/

CO2 Emissions
https://data.un.org/_Docs/SYB/CSV/SYB66_310_202310_Carbon%20Dioxide%20Emission%20Estimates.csv

Land Stewardship
https://data.un.org/_Docs/SYB/CSV/SYB66_310_202310_Carbon%20Dioxide%20Emission%20Estimates.csv

Water Supply and Sanitation
https://data.un.org/_Docs/SYB/CSV/SYB66_310_202310_Carbon%20Dioxide%20Emission%20Estimates.csv

Personal Health
https://data.un.org/_Docs/SYB/CSV/SYB66_310_202310_Carbon%20Dioxide%20Emission%20Estimates.csv

Energy Production
https://data.un.org/_Docs/SYB/CSV/SYB66_310_202310_Carbon%20Dioxide%20Emission%20Estimates.csv

Labor
https://data.un.org/_Docs/SYB/CSV/SYB66_329_202310_Labour%20Force%20and%20Unemployment.csv

Agriculture
https://data.un.org/_Docs/SYB/CSV/SYB66_329_202310_Labour%20Force%20and%20Unemployment.csv

Life Index
https://data.un.org/_Docs/SYB/CSV/SYB66_246_202310_Population%20Growth,%20Fertility%20and%20Mortality%20Indicators.csv

Population
https://data.un.org/_Docs/SYB/CSV/SYB66_246_202310_Population%20Growth,%20Fertility%20and%20Mortality%20Indicators.csv
