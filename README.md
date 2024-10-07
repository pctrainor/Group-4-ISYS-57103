# Group-4-ISYS-57103
Public Repository for Group 4 Project

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

 
