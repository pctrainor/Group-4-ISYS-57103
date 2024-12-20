# Grade this one for Phil!
import sqlite3
import os

# Construct the correct path to the database file
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'drone_data.db')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# --- Query Functions ---

# Query 1: Pilot Stats
def get_pilot_stats():
    """
    Retrieves the total number of unique pilots and the average pilot hours in a single query.
    """
    cursor.execute("""
        SELECT 
            COUNT(DISTINCT Pilot_ID) AS Total_Pilots, 
            AVG(Pilot_Hours) AS Average_Pilot_Hours
        FROM pilots;
    """)
    return cursor.fetchone()  # Returns tuple with both values

# Query 2 to get Lat/Long for flight plans with IsPlanned = 'TRUE'
# Query 2: Latitude/Longitude of Planned Routes (Modified)
def get_planned_route_coordinates():
    """
    Retrieves the Route_ID, a generated waypoint ID, latitude, and longitude 
    of planned routes by joining the 'routes' and 'flight_plans' tables.
    """
    cursor.execute("""
        SELECT 
            r.Route_ID,
            'WP-' || ROW_NUMBER() OVER (PARTITION BY r.Route_ID ORDER BY r.Latitude) AS Waypoint_ID,  -- Generate Waypoint ID
            r.Latitude, 
            r.Longitude
        FROM 
            routes r
        JOIN 
            flight_plans fp ON r.Route_ID = fp.Route_ID
        WHERE 
            fp.IsPlanned = 1;
    """)
    return cursor.fetchall()

# ... (other query functions) ...

# Query 3: Unique Drone Model Inventory
def get_unique_drone_model_inventory():
    """
    Retrieves the count of each unique drone model.
    """
    cursor.execute("""
        SELECT 
            Drone_Model, 
            COUNT(*) AS Count
        FROM 
            drones
        GROUP BY 
            Drone_Model;
    """)
    return cursor.fetchall()

# --- Stats ---

# Get pilot statistics (combined query)
total_pilots, avg_hours = get_pilot_stats()  # Unpack the tuple into two variables

print("-" * 30)
print("Pilot Statistics:")
print("-" * 30)
print(f"  Total Unique Pilots: {total_pilots}")
print(f"  Average Pilot Hours: {avg_hours:.2f}")

# Get planned route coordinates (modified)
route_coordinates = get_planned_route_coordinates()
print("\n" + "-" * 30)
print("Planned Route Coordinates:")
print("-" * 30)
if route_coordinates:
    for route_id, waypoint_id, lat, lon in route_coordinates:
        print(f"  Route ID: {route_id}, Waypoint ID: {waypoint_id}, Lat/Long: {lat}/{lon}")
else:
    print("  No coordinates found for planned flights.")

# ... (rest of the code) ... 
# Get drone model inventory
drone_model_inventory = get_unique_drone_model_inventory()
print("\n" + "-" * 30)
print("Unique Drone Model Inventory:")
print("-" * 30)
if drone_model_inventory:
    for model, count in drone_model_inventory:
        print(f"  Drone Model: {model}, Count: {count}")
else:
    print("  No drone inventory data found.")

# Close the connection
conn.close()