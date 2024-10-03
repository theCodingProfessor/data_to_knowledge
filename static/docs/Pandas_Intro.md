
## Pandas Introduction

### What is Pandas
**Pandas** has a rich set of methods and functionalities for its core data structures: `Series` and `DataFrame`. These methods provide powerful data manipulation, transformation, and analysis capabilities.

The most common used **Pandas features** are described next with: a brief description,
use case scenario, runtime efficiency, and a short block of demo code.

Methods described are associated with `Series` and `DataFrame`.

### **Pandas Series Features:**

1. **`pd.Series()`**
   - **Description**: A one-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.), with an optional axis label (index).
   - **Use Case**: Storing data like a column from a DataFrame, time series data, or any single-variable dataset.
   - **Runtime**: Efficient in terms of access and manipulation due to NumPy’s underlying structure.
   - **Code**:
     ```python
     import pandas as pd
     s = pd.Series([1, 3, 5, np.nan, 6, 8])
     print(s)
     ```

2. **`Series.value_counts()`**
   - **Description**: Returns a Series containing counts of unique values.
   - **Use Case**: Analyzing the frequency distribution of categorical data.
   - **Runtime**: Typically O(n) for counting unique values.
   - **Code**:
     ```python
     s = pd.Series(['apple', 'orange', 'apple', 'banana'])
     print(s.value_counts())
     # Output: 
     # apple     2
     # orange    1
     # banana    1
     ```

3. **`Series.apply(func)`**
   - **Description**: Applies a function along each element of the Series.
   - **Use Case**: Apply custom transformations to data elements (e.g., normalization, scaling, text processing).
   - **Runtime**: Depends on the complexity of the function, typically O(n) for simple functions.
   - **Code**:
     ```python
     s = pd.Series([1, 2, 3, 4])
     print(s.apply(lambda x: x * 2))
     ```

4. **`Series.describe()`**
   - **Description**: Generates descriptive statistics like mean, min, max, standard deviation for numeric Series.
   - **Use Case**: Summarizing data quickly for exploratory data analysis.
   - **Runtime**: O(n) as it computes various aggregate values.
   - **Code**:
     ```python
     s = pd.Series([1, 2, 3, 4, 5])
     print(s.describe())
     ```

5. **`Series.str()`**
   - **Description**: A set of string handling functions (substring extraction, replacements, splitting, etc.).
   - **Use Case**: Perform vectorized string operations, similar to Python’s native string methods, but more efficient.
   - **Runtime**: More efficient than Python loops for large datasets due to vectorization.
   - **Code**:
     ```python
     s = pd.Series(['apple', 'banana', 'orange'])
     print(s.str.upper())  # Outputs capitalized version
     ```

---

### **Pandas DataFrame Features:**

1. **`pd.DataFrame()`**
   - **Description**: A two-dimensional labeled data structure with columns of potentially different types, similar to a table in SQL or Excel.
   - **Use Case**: Store and manipulate tabular data with mixed data types (integers, floats, strings, etc.).
   - **Runtime**: Highly efficient for row and column access/modifications due to the NumPy-based implementation.
   - **Code**:
     ```python
     df = pd.DataFrame({
         'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'Score': [85.5, 90.3, 78.9]
     })
     print(df)
     ```

2. **`DataFrame.head()`**
   - **Description**: Returns the first n rows of the DataFrame.
   - **Use Case**: Useful for inspecting the structure of large datasets.
   - **Runtime**: O(n) where n is the number of rows requested (usually a small constant like 5).
   - **Code**:
     ```python
     print(df.head(2))  # Displays the first 2 rows
     ```

3. **`DataFrame.info()`**
   - **Description**: Provides a concise summary of the DataFrame, including column data types and non-null values.
   - **Use Case**: Quick overview of dataset structure, missing values, and memory usage.
   - **Runtime**: O(1) for metadata retrieval.
   - **Code**:
     ```python
     df.info()  # Outputs summary of the DataFrame
     ```

4. **`DataFrame.groupby()`**
   - **Description**: Groups the DataFrame using a column and allows you to apply aggregate functions (mean, sum, count, etc.).
   - **Use Case**: Analyzing grouped data, e.g., calculating average sales per product category.
   - **Runtime**: O(n) where n is the size of the DataFrame.
   - **Code**:
     ```python
     grouped = df.groupby('Age').mean()
     print(grouped)
     ```

5. **`DataFrame.merge()`**
   - **Description**: SQL-like join operation to merge DataFrames on a key (column).
   - **Use Case**: Combining datasets based on shared information (e.g., joining sales and customer data).
   - **Runtime**: O(n + m) for merging two DataFrames with n and m rows.
   - **Code**:
     ```python
     df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'val1': [1, 2, 3]})
     df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'val2': [4, 5, 6]})
     merged_df = pd.merge(df1, df2, on='key', how='inner')
     print(merged_df)
     ```

6. **`DataFrame.pivot_table()`**
   - **Description**: Creates a pivot table, which is a multi-dimensional table by summarizing data (like Excel pivot tables).
   - **Use Case**: Useful for summarizing and cross-tabulating large datasets.
   - **Runtime**: Depends on the complexity of the operation, but typically O(n).
   - **Code**:
     ```python
     data = {'A': ['foo', 'foo', 'bar'], 'B': ['one', 'two', 'one'], 'C': [1, 3, 2]}
     df = pd.DataFrame(data)
     pivot = df.pivot_table(values='C', index='A', columns='B', aggfunc=np.sum)
     print(pivot)
     ```

7. **`DataFrame.isnull()` and `DataFrame.fillna()`**
   - **Description**: Detects and handles missing values in the DataFrame. `isnull()` returns a boolean DataFrame indicating missing values, and `fillna()` replaces missing data with specified values.
   - **Use Case**: Dealing with incomplete datasets.
   - **Runtime**: O(n) for filling or detecting missing values.
   - **Code**:
     ```python
     df['Score'] = [85.5, None, 78.9]  # Introduce missing data
     print(df.isnull())  # Check for missing values
     df_filled = df.fillna(0)  # Fill missing values
     ```

8. **`DataFrame.sort_values()`**
   - **Description**: Sorts the DataFrame by values of one or more columns.
   - **Use Case**: Sorting datasets based on a column (e.g., sorting employees by salary).
   - **Runtime**: O(n log n) for sorting n rows.
   - **Code**:
     ```python
     df_sorted = df.sort_values(by='Score', ascending=False)
     print(df_sorted)
     ```

9. **`DataFrame.drop()`**
   - **Description**: Removes rows or columns from the DataFrame.
   - **Use Case**: Removing unneeded or redundant data, cleaning the dataset.
   - **Runtime**: O(n) where n is the size of the DataFrame.
   - **Code**:
     ```python
     df_dropped = df.drop(columns=['Score'])
     print(df_dropped)
     ```

10. **`DataFrame.apply()`**
    - **Description**: Applies a function along the axis (rows or columns) of the DataFrame.
    - **Use Case**: Apply custom transformations to entire rows or columns, such as normalizing data or calculating complex metrics.
    - **Runtime**: O(n), depending on the complexity of the applied function.
    - **Code**:
      ```python
      df['Adjusted_Score'] = df['Score'].apply(lambda x: x * 1.1 if x else 0)
      print(df)
      ```

---

### **Summary**:
- **Pandas** enhances **NumPy** by providing powerful, user-friendly tools for data manipulation, especially with structured and heterogeneous datasets.
- **Series** offers many single-dimensional data operations, and **DataFrame** extends this to multi-dimensional data (e.g., tables).
These methods allow efficient data loading, transformation, and analysis in a scalable way.

---

Prompt Inputs:
In the NumPy overview provided earlier a list of features (np.sort, np.unique, np.transpose...) were iterated and each feature was explained with a short description, a use case scenario, an runtime description and a short block of demo code. Does Pandas have a pd.features type of base object too. If Series or DataFrame are the base objects, could you summarize a set of features of those like you did for NumPy?

