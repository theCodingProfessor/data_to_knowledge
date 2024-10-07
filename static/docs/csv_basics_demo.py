"""
Using Python to parse csv files with comma, separated, values)
Using Pandas to get url_csv
"""
import os
from statistics import median

import pandas as pd
import matplotlib.pyplot as plt


def pd_examine_file():
    # list files in directory
    # select filename
    # extract csv data from filepath

    data = {'Product': ['Apple', 'Samsung', 'Apple', 'Google', 'Samsung'],
            'Region': ['North', 'East', 'West', 'North', 'West'],
            'Sales': [100, 150, 200, 90, 110]}
    lf_df = pd.DataFrame(data)
    sample_data = {'Product': ['Apple iPhone', 'Samsung Galaxy', 'Apple Macbook', 'Google Pixel'], 'Price': [999, 799, 1299, 899]}
    df = pd.DataFrame(sample_data)

    # Access Metadata about the dataset
    summary = df.describe()
    print(f'\nSummary data from df.describe() length {len(summary)}')
    print(f'{summary}')

    # Full Printout
    print(f'\nThe sample_data collection in full: '
          f'\n{df}')

    # Full Printout
    print(f'\nThe data collection in full: \n\t{lf_df}')

    # Filter for 'term' in column
    print(f'\nFilter Product Column by `Apple` Keyword: ')
    filtered_df = df[df['Product'].str.contains('Apple')]
    print(filtered_df)

    # Filter where 'term': value is >=, <, == etc
    print(f'\nFilter Price Column for > 900: ')
    filtered_df = df[df['Price'] > 900]
    print(filtered_df)

    # Sort the records by column
    print(f'\nSort Price Column Ascending by Price: ')
    sorted_df = df.sort_values(by='Price', ascending=True)
    print(sorted_df)

    # Create a pivot table to see total sales by Product and Region
    print(f'\nPivot Table as `Sales`, `Product`, `Region`, sum: ')
    pivot_df = lf_df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum')
    print(pivot_df)

    # Grouping
    print(f'\nGroup By `Product` .sum(): ')
    grouped_df = df.groupby('Product').sum()
    print(grouped_df)

    # Lambda Compute: High or Low
    print(f'\nCompute by `lambda` high:low')
    df['Price_Category'] = df['Price'].apply(lambda x: 'High' if x > 1000 else 'Low')
    print(df)

    # Statistical Compute
    print(f'\nStatistical Operations: ')
    # Totals as .sum()
    total_sales = lf_df['Sales'].sum()
    # print(f'\tTotal Sales \n\t\t{total_sales}')
    # mean average as .mean()
    average_price = lf_df['Sales'].mean()
    mid_value = lf_df['Sales'].median()
    mode_value = lf_df['Sales'].mode()
    print(f'\n\tAverages:')
    print(f'\t\tMean: {average_price}')
    print(f'\t\tMedian: {mid_value}')
    print(f'\t\tMode: {mode_value}')

    # # Max and Min as .max(), .min()
    max_price = lf_df['Sales'].max()
    min_price = lf_df['Sales'].min()
    print(f'\n\tMin and Max:')
    print(f"\t\tMax: {max_price}")
    print(f'\t\tMin: {min_price}')

    # Counting of collection as .count()
    print(f'\n\tCollection Counting:')
    # # count number of rows/records

    print(f'\t\tTotal Elements: {df.size}')
    df_rows, df_cols = df.shape
    print(f'\t\tRow Count: {df_rows}')
    print(f'\t\tColumn Count: {df_cols}')

    # Display Column names
    column_names = df.columns
    print(f"\n\t\tColumn Names:")
    for each in column_names:
        print(f'\t\t\t{each}')

    count_products = df['Product'].count()
    print(f'\n\t\tCount in `Product`: {count_products}')

    # Unique (filter keys)
    unique_filter = df['Product'].unique()
    print(f'\n\tUnique Terms from Column:')
    print(f'\t\tUnique Terms: {unique_filter}')

    # # get/display column names

    # # report on na values (row number)
    # # column filter


def local_csv_file():
    # Step 1: Check if the file exists and load it
    # file_name = 'weather_data_with_header.csv'
    # new_file_name = 'wi_weather_data_processed.csv'

    file_name = 'weather_data_without_header.csv'
    new_file_name = 'wo_weather_data_processed.csv'

    if os.path.exists(file_name):
        data = pd.read_csv(file_name)
        print("File loaded successfully!")
    else:
        print(f"The file '{file_name}' does not exist.")
        exit()

    # Step 2: Preview and Statistical Summary
    print("Preview of the data:")
    print(data.head())

    print("\nStatistical Summary:")
    # create column names if needed.
    data.columns = ['day', 'high_max', 'low_min', 'diff_range']
    print(data[['high_max', 'low_min', 'diff_range']].describe())

    # Step 3: Process each row individually
    for i, row in data.iterrows():
        print(f"Day {i + 1}:")
        print(f"High Max: {row['high_max']}, Low Min: {row['low_min']}, Range: {row['diff_range']}")

    # Step 4: Modify the data by adding a new column (mean temperature)
    data['mean_temp'] = (data['high_max'] + data['low_min']) / 2

    # Save the new data to a new CSV file
    data.to_csv(new_file_name, index=False)
    print(f"Modified data saved as '{new_file_name}'")

    # Step 5: Plot data and save image
    plt.figure(figsize=(10, 6))
    plt.plot(data['high_max'], label='High Max Temperatures', color='red')
    plt.plot(data['low_min'], label='Low Min Temperatures', color='blue')
    plt.title("Daily High and Low Temperatures")
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.legend()

    # Save the plot
    plot_file = 'temperature_analysis.png'
    plt.savefig(plot_file)
    print(f"Plot saved as '{plot_file}'")

    # Display the plot
    plt.show()
    return


def online_csv_file(csv_url):

    # Use `requests` to expose raw content
    headers = {'Authorization': 'Bearer your_token_here'}
    response = requests.get(csv_url, headers=headers)
    text_data = response.text  # string, number, text
    # byte_data = response.content  # byte stream, img

    # Use `pandas` when columns and separators are known
    data_sep = pd.read_csv(csv_url, sep=';', header=None)
    print(data_sep.head())  # This prints the first few rows of the structured data

    # Also Non Values
    # data_nan = pd.read_csv(csv_url, na_values=["", "NA", "null"])

    return


def main():

    print(f'Now in csv_basics_demo')
    pd_examine_file()

    return


main()
