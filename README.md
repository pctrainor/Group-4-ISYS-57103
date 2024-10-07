# Group-4-ISYS-57103
Public Repository for Group 4 Project

# Entity Diagram 

![Screenshot 2024-10-07 164940](https://github.com/user-attachments/assets/347e76b8-3946-4f64-a76e-2da7a0c25b0a)

### Data Dictionary 
1. **Drone**:
- **BUNO_ID**: Primary key, a unique identifier for the drone.
- **Drone_Model**: The model or type of drone.
- **Manufacturer**: The company that produced the drone.
- **Purchase_Date**: The date the drone was purchased.
- **Serial**: Serial number for the drone.
- **Status**: Maintenance status of the drone (e.g., active, inactive, in repair).
- **Status_Code**: A numerical representation of the drone's maintenance status (e.g., status code ‘12345’ might represent a low battery condition for this particular model).

2. **Flight Plan**:
- **Plan_ID**: Primary key, a unique identifier for the planned flight plan.
- **BUNO**: Foreign key referencing the Drone entity, indicating the drone associated with the plan.
- **Pilot_ID**: Foreign key referencing the Pilot entity, indicating the pilot assigned to the plan.
- **Start_Time**: The scheduled start time of the flight.
- **End_Time**: The scheduled end time of the flight.
- **Route_Coordination_ID**: Foreign key referencing the Flight Route entity, indicating the route associated with the plan.
- **IsPlanned**: Boolean representing whether the flight plan is the original flight plan (1) or the actual flight plan (0).

3. **Flight Plan Actuals**:
- **Flight_Actual_ID**: Primary key, a unique identifier for the actual flight.
- **Plan_ID**: Foreign key referencing the Flight Plan entity, indicating the planned flight.
- **Start_Time**: The actual start time of the flight.
- **End_Time**: The actual end time of the flight.
- **Pilot_ID**: Foreign key referencing the Pilot entity, indicating the pilot who flew the actual flight.
- **Pilot_Currency**: Boolean indicating whether the pilot was current for the flight.
- **Pilot_Hours**: The number of hours flown by the pilot.
- **Route_ID**: Foreign key referencing the Flight Route entity, indicating the actual route flown.

4. **Pilot**:
- **Pilot_ID**: Primary key, a unique identifier for the pilot.
- **Pilot_Current**: Boolean indicating whether the pilot is currently certified.
- **Pilot_Hours**: The total number of hours flown by the pilot.

5. **Flight Route**:
- **Route_ID**: Primary key, a unique identifier for the flight route.
- **Latitude**: A unique identifier for each latitudinal fix along the route.
- **Longitude**: A unique identifier for each longitudinal fix along the route.
- **Route_Coordination_ID**: A unique identifier for the route coordination (e.g., air traffic control clearance).

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
