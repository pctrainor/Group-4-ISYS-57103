# Grade this one for Jess!
import sqlite3
import os
 
# Construct the correct path to the database file
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'drone_data.db')
 
# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
 
# --- Query Functions ---

# Connect to the database
conn = sqlite3.connect('drone_data.db')
cursor = conn.cursor()

# --- Query Functions ---

# Query 1: Total Flights Logged by Pilots
def get_total_flights_logged_by_pilots():
    cursor.execute("""
    SELECT Pilot_ID, COUNT(Flight_Plan_ID) AS total_flights
    FROM flight_plans
    GROUP BY Pilot_ID;
    """)
    return cursor.fetchall()

# Query: Checking BUNO_ID against Status_Code
def check_buno_status(status_code):
    cursor.execute("""
    SELECT BUNO_ID, Status_Code
    FROM Drones
    WHERE Status_Code = ?;
    """, (status_code,))
    return cursor.fetchall()

# Query 3: Unique Drones Used in Each Flight
def get_unique_drones_used_in_each_flight():
    cursor.execute("""
    SELECT Flight_Plan_ID, COUNT(DISTINCT Drones.BUNO_ID) AS unique_drones
    FROM flight_plans
    JOIN Drones ON flight_plans.BUNO_ID = Drones.BUNO_ID  -- Corrected join condition
    GROUP BY Flight_Plan_ID;  -- Corrected GROUP BY clause
    """)
    return cursor.fetchall()

# --- Stats ---

# Get total flights logged by pilots
flights_logged_by_pilots = get_total_flights_logged_by_pilots()

# Get BUNO_ID status
buno_status = check_buno_status('OK')

# Get unique drones used in each flight
unique_drones_in_flight = get_unique_drones_used_in_each_flight()

# Print Flight Statistics
print("-" * 30)
print("Total Flights Logged by Pilots:")
print("-" * 30)
for pilot_id, total_flights in flights_logged_by_pilots:
    print(f"  Pilot ID: {pilot_id}, Total Flights: {total_flights}")

# Print Status of Drones
print("-" * 30)
print("BUNO_ID to Status_Code Check:")
print("-" * 30)
if buno_status:
    for buno_id, status_code in buno_status:
        print(f"  BUNO_ID: {buno_id}, Status: {status_code}")
else:
    print("  No drones found with the specified status.")

# Print Unique Drones Used in Each Flight
print("\n" + "-" * 30)
print("Unique Drones Used in Each Flight:")
print("-" * 30)
for flight_id, unique_drones in unique_drones_in_flight:
    print(f"  Flight ID: {flight_id}, Unique Drones Used: {unique_drones}")

# Close the connection
conn.close()
