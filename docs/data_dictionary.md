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
