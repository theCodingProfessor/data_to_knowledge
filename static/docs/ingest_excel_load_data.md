
## Data, Load Data from Outside Source

In Excel, Using the `Data` Tab find `Load Data` and `from an outside source` 
Paste a URL into the interface.
Select either Load, Load to, or Transform Data options *explained below*.

Use the **Data tab** in Excel
to connect to an external source via a URL where several options for importing and managing the data are provided.
The main options are —**Load**, **Load To**,
and **Transform Data**—each serve different purposes
and provide various ways to manage how the data is imported into Excel.

Here’s a breakdown of these options:

### 1. **Load**
The **Load** option is the simplest and quickest way to import data directly into Excel. When a user selects **Load**:
- **Data is imported into a new worksheet** (or an existing one if applicable).
- This option doesn't allow for much customization or transformation of the data.
- It's a good choice when students just want to get the data into Excel quickly, without making any changes to its structure or content.
- The connection between the data and the source URL is preserved, meaning the data can be refreshed if the source is updated.

### 2. **Load To**
The **Load To** option offers more control over how and where the data is imported. When students choose **Load To**, they are presented with different destinations and formats for the data:
- **Existing or New Worksheet**: Allows them to decide whether the data will be placed in a new worksheet or an existing one.
- **Table**: Imports the data as a structured table, making it easier to manipulate and analyze.
- **PivotTable Report**: Loads the data directly into a PivotTable, which can be useful if they want to summarize and analyze large datasets.
- **PivotChart**: Imports the data directly into a PivotChart, useful for visualizing the data in graph form.
- **Connection Only**: This option loads the data without displaying it in the worksheet but keeps a live connection to the data source. This is useful for using the data in calculations or reporting without having it appear in the workbook.

This option gives students flexibility in how they interact with the imported data and where it goes in the workbook.

### 3. **Transform Data**
The **Transform Data** option opens the **Power Query Editor**, which is a powerful tool for cleaning, filtering, and reshaping data before it is imported. This is especially useful when working with messy or complex datasets. Using **Transform Data**, students can:
- **Filter data**: Remove unnecessary rows or columns based on certain conditions.
- **Change data types**: Correct mismatches in data types (e.g., change a column of text into numbers or dates).
- **Merge and split columns**: Combine or break apart data in columns.
- **Remove duplicates**: Eliminate duplicate entries.
- **Pivot and unpivot data**: Reshape the data to fit their needs for analysis or visualization.

Once the data is cleaned up in the Power Query Editor, students can load the transformed version into Excel for further work.

### Use Case Scenarios for Students:
- **Load**: Clean, well-structured data and want it quickly imported into Excel to perform analysis or visualization, this is the simplest approach.
  
- **Load To**: Adds controls over where the data goes in the workbook or if they want to import the data as a PivotTable for immediate summary analysis, this is the best option. It also works well for larger datasets they might not want to display immediately but want to use in calculations.

- **Transform Data**: Provides visual look at real data. This is useful when students need to clean or reshape the data before working with it. It’s ideal for situations where they are importing data from an external source (e.g., the web or a database) that might not be formatted correctly for their needs.

---

### Summary:
- **Load**: Quick and easy import into a worksheet.
- **Load To**: Flexible options for where and how data is loaded (Table, PivotTable, etc.).
- **Transform Data**: Allows for data cleansing and transformation before loading it into Excel.

## Initial Prompt
In Excel, I can create the scatter plot, but I would like to do so for a few countries. Once a chart is created, can I freeze it somehow, so the data is preserved, but if I adjust/filter the underlying table the chart is not updated? 
