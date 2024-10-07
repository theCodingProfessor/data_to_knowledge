"""
CLinton Garwood
Data Demonstration using
open data via data.naperville.il.us
"""
import os

import pandas as pd


def main():
    demo_examine_data()
    return


def demo_examine_data():

    # list files in directory
    file_name = 'Naper_Incidents.csv'
    # extract csv data from filepath
    if os.path.exists(file_name):
        data = pd.read_csv(file_name)
        print("File loaded successfully!")
    else:
        print(f"The file '{file_name}' does not exist.")
        data = None

    # Step 2: Preview and Statistical Summary
    print("Preview of the data:")
    print(data.head())

    # Counting of collection as .count()
    print(f'\n\tCollection Counting:')

    print(f'\t\tTotal Elements: {data.size}')
    df_rows, df_cols = data.shape
    print(f'\t\tRow Count: {df_rows}')
    print(f'\t\tColumn Count: {df_cols}')

    # Display Column names
    column_names = data.columns
    print(f"\n\t\tColumn Names:")
    for each in column_names:
        print(f'\t\t\t{each}')

    print(f"\n\t\tUnique Values in Columns:")
    # Unique (filter keys)
    column_name = input("Enter Column to Filter: ")
    unique_filter = data[column_name].unique()
    print(f'\n\tUnique Terms from {column_name} Column:')
    print(f'\t\tUnique Terms: {unique_filter}')

    # count_products = df['Product'].count()
    # print(f'\n\t\tCount in `Product`: {count_products}')
    #



    # lf_df = pd.DataFrame(data)
    # sample_data = {'Product': ['Apple iPhone', 'Samsung Galaxy', 'Apple Macbook', 'Google Pixel'], 'Price': [999, 799, 1299, 899]}
    # df = pd.DataFrame(sample_data)
    #
    # # Access Metadata about the dataset
    # summary = df.describe()
    # print(f'\nSummary data from df.describe() length {len(summary)}')
    # print(f'{summary}')
    #
    # # Full Printout
    # print(f'\nThe sample_data collection in full: '
    #       f'\n{df}')
    #
    # # Full Printout
    # print(f'\nThe data collection in full: \n\t{lf_df}')
    #
    # # Filter for 'term' in column
    # print(f'\nFilter Product Column by `Apple` Keyword: ')
    # filtered_df = df[df['Product'].str.contains('Apple')]
    # print(filtered_df)
    #
    # # Filter where 'term': value is >=, <, == etc
    # print(f'\nFilter Price Column for > 900: ')
    # filtered_df = df[df['Price'] > 900]
    # print(filtered_df)
    #
    # # Sort the records by column
    # print(f'\nSort Price Column Ascending by Price: ')
    # sorted_df = df.sort_values(by='Price', ascending=True)
    # print(sorted_df)
    #
    # # Create a pivot table to see total sales by Product and Region
    # print(f'\nPivot Table as `Sales`, `Product`, `Region`, sum: ')
    # pivot_df = lf_df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum')
    # print(pivot_df)
    #
    # # Grouping
    # print(f'\nGroup By `Product` .sum(): ')
    # grouped_df = df.groupby('Product').sum()
    # print(grouped_df)
    #
    # # Lambda Compute: High or Low
    # print(f'\nCompute by `lambda` high:low')
    # df['Price_Category'] = df['Price'].apply(lambda x: 'High' if x > 1000 else 'Low')
    # print(df)
    #
    # # Statistical Compute
    # print(f'\nStatistical Operations: ')
    # # Totals as .sum()
    # total_sales = lf_df['Sales'].sum()
    # # print(f'\tTotal Sales \n\t\t{total_sales}')
    # # mean average as .mean()
    # average_price = lf_df['Sales'].mean()
    # mid_value = lf_df['Sales'].median()
    # mode_value = lf_df['Sales'].mode()
    # print(f'\n\tAverages:')
    # print(f'\t\tMean: {average_price}')
    # print(f'\t\tMedian: {mid_value}')
    # print(f'\t\tMode: {mode_value}')
    #
    # # # Max and Min as .max(), .min()
    # max_price = lf_df['Sales'].max()
    # min_price = lf_df['Sales'].min()
    # print(f'\n\tMin and Max:')
    # print(f"\t\tMax: {max_price}")
    # print(f'\t\tMin: {min_price}')
    #

    # # report on na values (row number)
    # # column filter




main()
