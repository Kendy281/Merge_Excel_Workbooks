# load.py
import mysql.connector

def load_data_to_db(incidents, conn_params):
    """
    Load the transformed data into a MySQL database.
    """
    conn = mysql.connector.connect(**conn_params)

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
        Restoration_Action TEXT,
        I2G_Count INT,
        I3G_Count INT,
        I4G_Count INT,
        Vendor VARCHAR(50),
        Affected_Sites TEXT,
        New_Column TEXT
    );
    """

    sql_insert_data_script = """
    INSERT INTO NEW_INCIDENTS (
        Ticket, Region, Problem_Fault, Category, Impact, Occurrence_Time, Resolution_Time,
        Restoration_Action, I2G_Count, I3G_Count, I4G_Count, Vendor, Affected_Sites, New_Column
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        new_cursor = conn.cursor()

        # Execute the table creation script
        for result in new_cursor.execute(CREATE_TABLE_SCRIPT, multi=True):
            pass

        # Batch insert
        batch_size = 100
        for i in range(0, len(incidents), batch_size):
            batch = incidents.iloc[i:i + batch_size].values.tolist()
            new_cursor.executemany(sql_insert_data_script, batch)

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()

    finally:
        new_cursor.close()
        conn.close()
