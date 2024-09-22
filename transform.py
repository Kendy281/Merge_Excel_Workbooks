# transform.py
import pandas as pd

def transform_data(incidents):
    """
    Clean and transform the data before loading into the database.
    """
    # Rename the last column to 'New_Column'
    incidents.rename(columns={incidents.columns[-1]: 'New_Column'}, inplace=True)

    # Convert relevant columns to correct data types
    incidents['Resolution Time'] = pd.to_datetime(incidents['Resolution Time'], errors='coerce')

    # Convert counts to integers
    incidents['2G Count'] = incidents['2G Count'].astype('Int64')
    incidents['3G Count'] = incidents['3G Count'].astype('Int64')
    incidents['4G Count'] = incidents['4G Count'].astype('Int64')

    # Convert object columns to numeric, handle non-numeric values
    incidents['MTTR(Hrs)'] = incidents['MTTR(Hrs)'].astype('float')
    incidents['2G Outage Hours'] = incidents['2G Outage Hours'].astype('float')
    incidents['3G Outage Hours'] = incidents['3G Outage Hours'].astype('float')
    incidents['4G Outage Hours'] = incidents['4G Outage Hours'].astype('float')

    # Handle missing values
    incidents.fillna('', inplace=True)

    # Drop duplicate records
    incidents = incidents.drop_duplicates(subset='Tickets')

    # Drop unnecessary columns
    incidents = incidents.drop(columns=['MTTR', 'MTTR(Hrs)', '2G Outage Hours', '3G Outage Hours', '4G Outage Hours'])

    return incidents
