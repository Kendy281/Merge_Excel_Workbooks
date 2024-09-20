import os
import pandas as pd

path = r"C:\Users\k50037877\Desktop\Reports\prim\Major Failures\NWMF\Single_raw_data\WK32\new"
output_path = r"C:\Users\k50037877\Desktop\week_incidents.xlsx"
files = os.listdir(path)

dataframe = []

for file in files:
    file_path = os.path.join(path, file)
    df = pd.read_excel(file_path)
    dataframe.append(df)

incidents = pd.concat(dataframe, ignore_index=True)

#incidents.to_excel(output_path,index=False)


#PART 2
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '######',
    database = 'failures_db',
    port = 3306,
)

#CREATE TABLE SCRIPT
CREATE_TABLE_SCRIPT = """
DROP TABLE IF EXISTS NEW_INCIDENTS;
CREATE TABLE IF NOT EXISTS NEW_INCIDENTS (
    Ticket VARCHAR(24) PRIMARY KEY,
    Region VARCHAR(50),
    Problem_Fault TEXT,
    Category VARCHAR(50),
    Impact VARCHAR(100),
    Occurrence_Time DATETIME,
    Resolution_Time DATETIME,
    MTTR TIME,
    Restoration_Action TEXT,
    I2G_Count INT,
    I3G_Count INT,
    I4G_Count INT,
    I2G_Outage_Hours DECIMAL(10, 3),
    I3G_Outage_Hours DECIMAL(10, 3),
    I4G_Outage_Hours DECIMAL(10, 3),
    Vendor VARCHAR(50),
    Affected_Sites TEXT
);
""" 

#Insert data into table script
sql_insert_data_script = """
INSERT INTO NEW_INCIDENTS (
    Ticket, Region, Problem_Fault, Category, Impact, Occurrence_Time, Resolution_Time,
    MTTR, Restoration_Action, I2G_Count, I3G_Count, I4G_Count, I2G_Outage_Hours,
    I3G_Outage_Hours, I4G_Outage_Hours, Vendor, Affected_Sites
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

new_cursor = conn.cursor()

new_cursor.execute(CREATE_TABLE_SCRIPT, multi=True)



new_cursor.close()
conn.close()