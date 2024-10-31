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
                      Longitude=route["Longitude"])
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
    routes = run_query(query, (route_id, ))
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
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO routes (Route_ID, Latitude, Longitude) VALUES (?, ?, ?)",
            (route_data['Route_ID'], route_data['Latitude'],
             route_data['Longitude']))
        conn.commit()
        conn.close()

        new_route = Route(Route_ID=route_data['Route_ID'],
                          Latitude=route_data['Latitude'],
                          Longitude=route_data['Longitude'])
        return new_route

    except sqlite3.Error as e:
        print(f"Error adding route to the database: {e}")
        return None


def update_route(route_id: str, route_data):
    """
    Updates an existing route in the database.

    Args:
        route_id (str): The Route_ID of the route to update.
        route_data (dict): A dictionary containing the updated route data.

    Returns:
        Route: The updated Route object.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE routes SET Latitude = ?, Longitude = ? WHERE Route_ID = ?",
            (route_data['Latitude'], route_data['Longitude'], route_id))
        conn.commit()
        conn.close()

        updated_route = Route(Route_ID=route_id,
                              Latitude=route_data['Latitude'],
                              Longitude=route_data['Longitude'])
        return updated_route

    except sqlite3.Error as e:
        print(f"Error updating route in the database: {e}")
        return None


def delete_route(route_id: str):
    """
    Deletes a route from the database.

    Args:
        route_id (str): The Route_ID of the route to delete.

    Returns:
        bool: True if the route was deleted successfully, False otherwise.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM routes WHERE Route_ID = ?", (route_id, ))

        if cursor.rowcount > 0:
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False

    except sqlite3.Error as e:
        print(f"Error deleting route from the database: {e}")
        return False