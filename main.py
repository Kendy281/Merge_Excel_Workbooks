# main.py
from extract import extract_data
from transform import transform_data
from load import load_data_to_db
import config  # Import connection parameters

# Define paths
path = r"C:\Users\k50037877\Desktop\Reports\prim\Major Failures\NWMF\Single_raw_data\WK32\new"


# Step 1: Extract data
incidents = extract_data(path)

# Step 2: Transform data
incidents = transform_data(incidents)

# Step 3: Load data to the database
load_data_to_db(incidents, config.conn_params)
