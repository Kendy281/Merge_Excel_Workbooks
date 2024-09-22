# extract.py

import os
import pandas as pd

def extract_data(path):
    """
    Extract data from Excel files in the stated directory and return a concatenated DataFrame.
    """
    files = os.listdir(path)
    dataframe = []

    for file in files:
        file_path = os.path.join(path, file)
        try:
            df = pd.read_excel(file_path)
            dataframe.append(df)
        except Exception as e:
            print(f"Error reading file {file}: {e}")

    # Concatenate all the dataframes
    return pd.concat(dataframe, ignore_index=True)
