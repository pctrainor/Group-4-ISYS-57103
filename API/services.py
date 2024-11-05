import sqlite3
from typing import List
from API.model import Drone, FlightPlan, Route, Pilot  # Only import necessary models
from pathlib import Path


def get_db_connection():
    """
    Establishes a connection to the SQLite database.

    Returns:
        sqlite3.Connection: A connection object.
    """
    DATABASE_PATH = Path(__file__).parents[1] / "data"
    connection = sqlite3.connect(DATABASE_PATH / 'drone_data.db')
    connection.row_factory = sqlite3.Row
    return connection


def run_query(query, params=None):
    """
    Runs a query on the database.

    Args:
        query (str): The SQL query.
        params (tuple, optional): Query parameters.

    Returns:
        list of dict: Query results.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    if params is not None:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# ---------------------------------------------------------
# Drones
# ---------------------------------------------------------

def convert_rows_to_drone_list(drones):
    """
    Converts database rows to Drone objects.

    Args:
        drones (list): Database rows.

    Returns:
        list: Drone objects.
    """
    all_drones = []
    if drones is None:
        return all_drones
    for drone in drones:
        drone = Drone(BUNO_ID=drone["BUNO_ID"],
                      Drone_Model=drone["Drone_Model"],
                      Manufacturer=drone["Manufacturer"],
                      Purchase_Date=drone["Purchase_Date"],
                      Serial=drone["Serial"],
                      Status=drone["Status"],
                      Status_Code=drone["Status_Code"])
        all_drones.append(drone)
    return all_drones


def get_all_drones() -> List[Drone]:
    """
    Retrieves all drones.

    Returns:
        List[Drone]: Drone objects.
    """
    query = "SELECT * FROM drones"
    drones = run_query(query)  # Use run_query()
    return convert_rows_to_drone_list(drones)


# Add other functions for drones (get_drone_by_id, etc.) as needed

def get_drone_by_id(buno_id: int) -> Drone:
    """
    Retrieves a drone by its BUNO_ID.

    Args:
        buno_id (int): The BUNO_ID of the drone.

    Returns:
        Drone: The drone object.
    """
    query = "SELECT * FROM drones WHERE BUNO_ID = ?"
    drones = run_query(query, (buno_id, ))
    drone_list = convert_rows_to_drone_list(drones)
    return drone_list[0] if drone_list else None


def get_drones_by_status(status: str) -> List[Drone]:
    """
    Retrieves drones by their status.

    Args:
        status (str): The status of the drones.

    Returns:
        List[Drone]: Drone objects.
    """
    query = "SELECT * FROM drones WHERE Status = ?"
    drones = run_query(query, (status, ))
    return convert_rows_to_drone_list(drones)


def get_drones_by_manufacturer(manufacturer: str) -> List[Drone]:
    """
    Retrieves drones by their manufacturer.

    Args:
        manufacturer (str): The manufacturer of the drones.

    Returns:
        List[Drone]: Drone objects.
    """
    query = "SELECT * FROM drones WHERE Manufacturer = ?"
    drones = run_query(query, (manufacturer, ))
    return convert_rows_to_drone_list(drones)


def get_drones_purchased_after(date: str) -> List[Drone]:
    """
    Retrieves drones purchased after a specific date.

    Args:
        date (str): The purchase date in 'YYYY-MM-DD' format.

    Returns:
        List[Drone]: Drone objects.
    """
    query = "SELECT * FROM drones WHERE Purchase_Date > ?"
    drones = run_query(query, (date, ))
    return convert_rows_to_drone_list(drones)


def add_drone(drone_data):
    """
    Adds a new drone to the database.

    Args:
        drone_data (dict): A dictionary containing the drone data.

    Returns:
        Drone: The newly added Drone object.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Assuming your 'drones' table has columns: BUNO_ID, Drone_Model, Manufacturer, Purchase_Date, Serial, Status, Status_Code
        cursor.execute(
            "INSERT INTO drones (BUNO_ID, Drone_Model, Manufacturer, Purchase_Date, Serial, Status, Status_Code) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (drone_data['BUNO_ID'], drone_data['Drone_Model'],
             drone_data['Manufacturer'], drone_data['Purchase_Date'],
             drone_data['Serial'], drone_data['Status'],
             drone_data['Status_Code']))
        conn.commit()
        conn.close()

        new_drone = Drone(BUNO_ID=drone_data['BUNO_ID'],
                          Drone_Model=drone_data['Drone_Model'],
                          Manufacturer=drone_data['Manufacturer'],
                          Purchase_Date=drone_data['Purchase_Date'],
                          Serial=drone_data['Serial'],
                          Status=drone_data['Status'],
                          Status_Code=drone_data['Status_Code'])
        return new_drone

    except sqlite3.Error as e:
        print(f"Error adding drone to the database: {e}")
        return None


def delete_drone(buno_id):
    """
    Deletes a drone from the database.

    Args:
        buno_id: The BUNO_ID of the drone to delete.

    Returns:
        bool: True if the drone was deleted successfully, False otherwise.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Execute the DELETE query
        cursor.execute("DELETE FROM drones WHERE BUNO_ID = ?", (buno_id, ))

        # Check if any rows were affected (i.e., if the drone existed)
        if cursor.rowcount > 0:
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False

    except sqlite3.Error as e:
        print(f"Error deleting drone from the database: {e}")
        return False

# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

def convert_rows_to_route_list(routes):
    """
    Converts database rows to Route objects.

    Args:
        routes (list): Database rows.

    Returns:
        list: Route objects.
    """
    all_routes = []
    if routes is None:
        return all_routes
    for route in routes:
        route = Route(Route_ID=route["Route_ID"],
                      Latitude=route["Latitude"],
                      Longitude=route["Longitude"])  # Add other attributes as needed
        all_routes.append(route)
    return all_routes

def get_all_routes() -> List[Route]:
    """
    Retrieves all routes.

    Returns:
        List[Route]: Route objects.
    """
    query = "SELECT * FROM routes"
    routes = run_query(query)
    return convert_rows_to_route_list(routes)

def get_route_by_id(route_id: str) -> Route:
    """
    Retrieves a route by its Route_ID.

    Args:
        route_id (str): The Route_ID of the route.

    Returns:
        Route: The route object.
    """
    query = "SELECT * FROM routes WHERE Route_ID = ?"
    routes = run_query(query, (route_id,))
    route_list = convert_rows_to_route_list(routes)
    return route_list[0] if route_list else None

def add_route(route_data):
    """
    Adds a new route to the database.

    Args:
        route_data (dict): A dictionary containing the route data.

    Returns:
        Route: The newly added Route object.
    """

# ---------------------------------------------------------
# Flight Plans
# ---------------------------------------------------------

def convert_rows_to_flight_plan_list(flight_plans):
    """
    Converts database rows to FlightPlan objects.

    Args:
        flight_plans (list): Database rows.

    Returns:
        list: FlightPlan objects.
    """
    all_flight_plans = []
    if flight_plans is None:
        return all_flight_plans
    for flight_plan in flight_plans:
        flight_plan = FlightPlan(Flight_Plan_ID=flight_plan["Flight_Plan_ID"],
                                  BUNO_ID=flight_plan["BUNO_ID"],
                                  Pilot_ID=flight_plan["Pilot_ID"],
                                  Route_ID=flight_plan["Route_ID"],
                                  IsPlanned=flight_plan["IsPlanned"])
        all_flight_plans.append(flight_plan)
    return all_flight_plans


def get_all_flight_plans() -> List[FlightPlan]:
    """
    Retrieves all flight plans.

    Returns:
        List[FlightPlan]: FlightPlan objects.
    """
    query = "SELECT * FROM flight_plans"
    flight_plans = run_query(query)
    return convert_rows_to_flight_plan_list(flight_plans)


def get_flight_plan_by_id(flight_plan_id: str) -> FlightPlan:
    """
    Retrieves a flight plan by its Flight_Plan_ID.

    Args:
        flight_plan_id (str): The Flight_Plan_ID of the flight plan.

    Returns:
        FlightPlan: The flight plan object.
    """
    query = "SELECT * FROM flight_plans WHERE Flight_Plan_ID = ?"
    flight_plans = run_query(query, (flight_plan_id,))
    flight_plan_list = convert_rows_to_flight_plan_list(flight_plans)
    return flight_plan_list[0] if flight_plan_list else None


def add_flight_plan(flight_plan_data):
    """
    Adds a new flight plan to the database.

    Args:
        flight_plan_data (dict): A dictionary containing the flight plan data.

    Returns:
        FlightPlan: The newly added FlightPlan object.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO flight_plans (Flight_Plan_ID, BUNO_ID, Pilot_ID, Route_ID, IsPlanned) VALUES (?, ?, ?, ?, ?)",
            (flight_plan_data['Flight_Plan_ID'], flight_plan_data['BUNO_ID'],
             flight_plan_data['Pilot_ID'], flight_plan_data['Route_ID'],
             flight_plan_data['IsPlanned']))
        conn.commit()
        conn.close()

        new_flight_plan = FlightPlan(Flight_Plan_ID=flight_plan_data['Flight_Plan_ID'],
                                      BUNO_ID=flight_plan_data['BUNO_ID'],
                                      Pilot_ID=flight_plan_data['Pilot_ID'],
                                      Route_ID=flight_plan_data['Route_ID'],
                                      IsPlanned=flight_plan_data['IsPlanned'])
        return new_flight_plan

    except sqlite3.Error as e:
        print(f"Error adding flight plan to the database: {e}")
        return None


def update_flight_plan(flight_plan_id: str, flight_plan_data):
    """
    Updates an existing flight plan in the database.

    Args:
        flight_plan_id (str): The Flight_Plan_ID of the flight plan to update.
        flight_plan_data (dict): A dictionary containing the updated flight plan data.

    Returns:
        FlightPlan: The updated FlightPlan object.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE flight_plans SET BUNO_ID = ?, Pilot_ID = ?, Route_ID = ?, IsPlanned = ? WHERE Flight_Plan_ID = ?",
            (flight_plan_data['BUNO_ID'], flight_plan_data['Pilot_ID'],
             flight_plan_data['Route_ID'], flight_plan_data['IsPlanned'],
             flight_plan_id))
        conn.commit()
        conn.close()

        updated_flight_plan = FlightPlan(Flight_Plan_ID=flight_plan_id,
                                          BUNO_ID=flight_plan_data['BUNO_ID'],
                                          Pilot_ID=flight_plan_data['Pilot_ID'],
                                          Route_ID=flight_plan_data['Route_ID'],
                                          IsPlanned=flight_plan_data['IsPlanned'])
        return updated_flight_plan

    except sqlite3.Error as e:
        print(f"Error updating flight plan in the database: {e}")
        return None


def delete_flight_plan(flight_plan_id: str):
    """
    Deletes a flight plan from the database.

    Args:
        flight_plan_id (str): The Flight_Plan_ID of the flight plan to delete.

    Returns:
        bool: True if the flight plan was deleted successfully, False otherwise.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM flight_plans WHERE Flight_Plan_ID = ?", (flight_plan_id,))

        if cursor.rowcount > 0:
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False

    except sqlite3.Error as e:
        print(f"Error deleting flight plan from the database: {e}")
        return False
    
# ---------------------------------------------------------
# Pilots
# ---------------------------------------------------------
@api_bp.route('/pilots', methods=['GET', 'POST'])
def get_or_create_pilots():
    if request.method == 'GET':
        # 1. Connect to your database (using SQLAlchemy or similar)
        # Example using SQLAlchemy (replace with your actual setup):
        # from . import db  # Assuming you have a db object initialized
        # pilots = db.session.query(model.Pilot).all()

        # --- Example using in-memory data (replace with database retrieval) ---
        pilot_data = [
            {"Pilot_ID": "PILOT-001", "Pilot_Current": True, "Pilot_Hours": 1000},
            {"Pilot_ID": "PILOT-002", "Pilot_Current": False, "Pilot_Hours": 500},
            # ... other pilot data ...
        ]
        pilots = [model.Pilot(**data) for data in pilot_data]
        # --- End of example ---

        # Apply limit if provided in the request arguments
        limit = request.args.get('limit', type=int)
        if limit:
            pilots = pilots[:limit]

        pilot_list = [pilot.__dict__ for pilot in pilots]
        return jsonify(pilot_list)

    if request.method == 'POST':
        # Get the pilot data from the request body
        data = request.get_json()

        # Create a new Pilot object
        new_pilot = model.Pilot(**data)

        # ... your code to save the new pilot to the database ...

        return jsonify(new_pilot.__dict__), 201  # 201 Created


@api_bp.route('/pilots/<pilot_id>', methods=['GET', 'PUT', 'DELETE'])
def get_update_or_delete_pilot(pilot_id):
    # --- Example using in-memory data (replace with database retrieval) ---
    pilot_data = [
        {"Pilot_ID": "PILOT-001", "Pilot_Current": True, "Pilot_Hours": 1000},
        {"Pilot_ID": "PILOT-002", "Pilot_Current": False, "Pilot_Hours": 500},
        # ... other pilot data ...
    ]
    pilots = [model.Pilot(**data) for data in pilot_data]
    # --- End of example ---

    if request.method == 'GET':
        # 1. Connect to your database (if not already connected)

        # 2. Fetch the pilot with the given pilot_id from the database
        # Example using SQLAlchemy:
        # from . import db
        # pilot = db.session.query(model.Pilot).filter_by(Pilot_ID=pilot_id).first()

        pilot = next((p for p in pilots if p.Pilot_ID == pilot_id), None)

        if pilot:
            return jsonify(pilot.__dict__)
        else:
            return jsonify({'error': 'Pilot not found'}), 404

    if request.method == 'PUT':
        # Get the updated pilot data from the request body
        data = request.get_json()

        # ... your code to update the pilot with the given pilot_id in the database ...
        pilot = next((p for p in pilots if p.Pilot_ID == pilot_id), None)
        if pilot:
            # Update the pilot object with the new data (example)
            pilot.Pilot_Current = data.get('Pilot_Current', pilot.Pilot_Current)
            pilot.Pilot_Hours = data.get('Pilot_Hours', pilot.Pilot_Hours)
            return jsonify({'message': f'Pilot {pilot_id} updated'}), 200
        else:
            return jsonify({'error': 'Pilot not found'}), 404


    if request.method == 'DELETE':
        # ... your code to delete the pilot with the given pilot_id from the database ...
        try:
            # Find the index of the pilot to delete
            index = next((i for i, p in enumerate(pilots) if p.Pilot_ID == pilot_id), None)

            if index is not None:
                # Delete the pilot from the list
                del pilots[index]
                return jsonify({'message': f'Pilot {pilot_id} deleted'}), 204  # 204 No Content
            else:
                return jsonify({'error': 'Pilot not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500