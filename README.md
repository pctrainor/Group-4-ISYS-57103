# Group-4-ISYS-57103
Public Repository for Group 4 Project
- Swagger UI: https://pctrainor.github.io/Group-4-ISYS-57103/

# Entity Diagram 

![Screenshot 2024-10-07 164940](https://github.com/user-attachments/assets/347e76b8-3946-4f64-a76e-2da7a0c25b0a)


# Jessalyn Heckel's Queries
This Python script connects to a SQLite database (`drone_data.db`) to retrieve and display key statistics related to flight plans, pilot logs, and drone usage. The script executes three SQL queries to perform the following:

1. **Total Flights Logged by Pilots**:
   - Retrieves the total number of flights logged by each pilot from the `flight_plans` table, grouped by `Pilot_ID`.

2. **Drone Status Check (BUNO_ID to Status_Code)**:
   - Filters drones from the `Drones` table based on their `Status_Code` (e.g., 'active'), showing their corresponding `BUNO_ID` and current status.

3. **Unique Drones Used in Each Flight**:
   - Queries the number of unique drones used in each flight by joining the `flight_plans` and `Drones` tables, grouped by `Flight_Plan_ID`.

After fetching the results, the script prints them in a neatly formatted manner for review. Finally, it closes the database connection to ensure resources are released properly.

 # Phillip Trainor's Queries
 
This script connects to an SQLite database (`drone_data.db`) and retrieves various statistics related to drone flight operations. It performs the following key queries:
 
1. **Pilot Statistics**:
 
   - Retrieves the total number of unique pilots and the average hours logged by pilots from the `pilots` table.
 
2. **Planned Route Coordinates**:
 
   - Fetches route IDs, dynamically generated waypoint IDs, and the latitude/longitude of flight routes from the `routes` and `flight_plans` tables where `IsPlanned` is true.
 
3. **Unique Drone Model Inventory**:
   - Retrieves a count of each unique drone model from the `drones` table.
 
The results are printed in a formatted output, and the database connection is closed after querying.
