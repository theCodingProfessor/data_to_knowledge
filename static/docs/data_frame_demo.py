"""
CLinton Garwood
Data Demonstration using
SCV data via data.naperville.il.us
"""

import os

import pandas as pd
import matplotlib.pyplot as plt


def main():
    handle_dataframe()
    return


def list_files():
    # list files in directory
    files = os.listdir()

    # Print only CSV files from the directory
    csv_files = [file for file in files if file.endswith('.csv')]
    if not csv_files:
        print("\nNo CSV files found in the current directory.")
    else:
        # Display the list of CSV files
        print(f"\nAvailable CSV Files:")
        for idx, file in enumerate(csv_files):
            print(f"\t{idx + 1}: {file}")
    return


def load_file():
    list_files()  # Display list of files
    file_name = input(f"\n\tFrom the list select a file: ")
    if os.path.exists(file_name):
        data = pd.read_csv(file_name)
        print("\tSuccess. {file_name} loaded.")
    else:
        print(f"\t{file_name} does not exist.")
        data = pd.DataFrame()
    return data


def data_frame_overview(this_frame):
    # Step 2: Preview and Statistical Summary
    print(f"\nData Preview (first five rows):")
    print(this_frame.head())

    # Counting Collection Items
    df_rows, df_cols = this_frame.shape
    print(f'\n\tCollection Counting:')
    print(f'\t\tTotal Elements: {this_frame.size}')
    print(f'\t\tRow Count: {df_rows}')
    print(f'\t\tColumn Count: {df_cols}')

    # Display Column names
    column_names = this_frame.columns
    print(f"\n\t\t{len(column_names)} Column Names:")
    for each in column_names:
        print(f'\t\t\t{each}')


def filter_columns(data):
    print(f"\n\t\tUnique Values in Columns:")
    # Unique (filter keys)
    column_name = input("\t\tColumn Name to Filter, exit with 0: ")
    unique_filter = data[column_name].unique()
    print(f'\n\tUnique Terms from {column_name} Column:')
    print(f'\t\tUnique Terms: {unique_filter}')
    data_label = input(f"\n\t\tFilter a terms (from above): ")
    while column_name != "0":
        # # Filter for 'term' in column
        try:
            filtered_df = data[data[column_name].str.contains(data_label)]
            f_row, f_column = filtered_df.shape
            print(f'\nData Report: {f_row} rows at size {filtered_df.size}.')
            print(filtered_df[['date_rept', column_name, 'street']])

            # Optional: Generate Chart on feature
            yes_no = input("To Run Report enter 1: ")
            if yes_no == "1":
                filter_feature_name(filtered_df, data_label)
        except ValueError as ve:
            print(f'Found {ve}')
        data_label = input("\n\t\tNew Filter... or exit=0: ")
        if data_label == '0':
            column_name = '0'


def user_menu():
    print(f'\n\t1) Load a CSV File: ')
    print(f'\t2) DataFrame Summary Data: ')
    print(f'\t3) Filter Column by Phrase: ')
    print(f'\t0) Exit ')
    choice = input(f'\tPlease select: ')
    return choice


def handle_dataframe():
    # Data Frame Options
    data, user_choice = None, '7'
    while user_choice != '0':
        user_choice = user_menu()
        if user_choice == "1":
            # 1 Load CSV File
            # list_files()  # displays list of csv files
            data = load_file()  # calls list_files()
        elif user_choice == "2":
            try:
                # Display data frame overview:
                data_frame_overview(data)
            except ValueError as ve:
                print(f'\tPlease select a file first.')
        elif user_choice == "3":
            # Display data frame overview:
            filter_columns(data)
        else:
            print(f'\tPlease select a file first.')

    return


def filter_feature_name(filtered_df, feature_name):
    filtered_df['date_rept'] = pd.to_datetime(filtered_df['date_rept'])
    # Extract the day of the week from 'date_rept'
    filtered_df['day_of_week'] = filtered_df['date_rept'].dt.day_name()

    # Group by the day of the week and count the number of incidents
    day_counts = filtered_df['day_of_week'].value_counts().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )

    # Plot the data using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(day_counts.index, day_counts.values, color='orange')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Incidents')
    plt.title(f'{feature_name}-related Incidents by Day of the Week')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return


main()
