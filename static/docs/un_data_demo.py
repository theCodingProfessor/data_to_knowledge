"""
United Nations Data Demo
Clinton Garwood
License: MIT
October 2024
see `ingest_data.md` for workflow
"""

import pandas as pd
import os


def main():

    print(f'\nUN Data Using Python Demo')
    file_path = 'un_population.csv'

    try:
        if os.path.exists(file_path):
            data = pd.read_csv(file_path, encoding='ISO-8859-1')

            print(f"\ndata.head() Prints top 5 Rows")
            print(f'\t{data.head()}')

            print(f"\ndata.info() Checks for null values")
            print(f'\t{data.info()}')

            print(f"\ndata.describe() Show Summary Statistics")
            print(data.describe())

            # Select the xth row (replace x with the row number, remember row indexing starts at 0)
            x = 325
            row = data.iloc[x]
            print(row)  # Display all the columns for the selected row


    except FileNotFoundError as fnfe:
        print(f'File not Found')

    return


main()
