import sqlite3
from . import model  # Import your Drone model

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect('data/drone_data.db')  
    print(conn)
    return conn

def get_all_drones():
    """Fetches all drone records from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drones")  
    drone_data = cursor.fetchall()
    conn.close()

    drones = []
    for row in drone_data:
        drone = model.Drone(BUNO_ID=row[0], Drone_Model=row[1], 
                            Manufacturer=row[2], Purchase_Date=row[3], 
                            Serial=row[4], Status=row[5], Status_Code=row[6])
        drones.append(drone)

    return drones