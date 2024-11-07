from flask import Flask, Blueprint, jsonify, send_from_directory, request
import API.services as services  # Import your services module

api_bp = Blueprint('api', __name__)


@api_bp.route('/connection')
def test_connection():
    """
    Test the database connection.
    """
    try:
        services.get_db_connection()  # Call the function from services.py
        return jsonify({'message': 'Successfully connected to the API'}), 200
    except Exception as e:
        return jsonify({'error': f'Database connection failed: {str(e)}'}), 500


@api_bp.route("/drones", methods=["GET"])
def get_drones():
    """
    Retrieve a list of all drones.
    """
    try:
        drones = services.get_all_drones()  # Call the function from services.py
        drone_list = [drone.__dict__ for drone in drones]
        return jsonify(drone_list), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch drones: {str(e)}'}), 500


@api_bp.route('/drone-api.yaml')
def serve_openapi_spec():
    """Serve the OpenAPI specification file."""
    return send_from_directory('.', 'drone-api.yaml')


@api_bp.route('/')  # Route for index.html
def serve_index():
    """Serve the index.html file."""
    return send_from_directory('.', 'index.html')


@api_bp.route("/drones/<buno_id>", methods=["GET"])  # Changed drone_id to buno_id
def get_drone(buno_id):  # Changed drone_id to buno_id
    """
    Retrieve a specific drone by its ID.
    """
    try:
        drone = services.get_drone_by_id(
            buno_id
        )  # Call the function from services.py and pass buno_id
        if drone:
            return jsonify(drone.__dict__), 200
        else:
            return jsonify({'error': 'Drone not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to fetch drone: {str(e)}'}), 500


@api_bp.route("/drones", methods=["POST"])
def add_drone():
    """
    Add a new drone.
    """
    try:
        drone_data = request.get_json()
        new_drone = services.add_drone(
            drone_data)  # Call the function from services.py
        return jsonify(new_drone.__dict__), 201
    except Exception as e:
        return jsonify({'error': f'Failed to add drone: {str(e)}'}), 500


@api_bp.route("/drones/<buno_id>", methods=["PUT"])  # Changed drone_id to buno_id
def update_drone(buno_id):  # Changed drone_id to buno_id
    """
    Update an existing drone by its ID.
    """
    try:
        drone_data = request.get_json()
        updated_drone = services.update_drone(
            buno_id, drone_data
        )  # Call the function from services.py and pass buno_id
        if updated_drone:
            return jsonify(updated_drone.__dict__), 200
        else:
            return jsonify({'error': 'Drone not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to update drone: {str(e)}'}), 500


@api_bp.route("/drones/<buno_id>", methods=["DELETE"])  # Changed drone_id to buno_id
def delete_drone(buno_id):  # Changed drone_id to buno_id
    """
    Delete a specific drone by its ID.
    """
    try:
        result = services.delete_drone(buno_id)  # Call the function from services.py and pass buno_id
        if result:
            return jsonify({'message': 'Drone deleted successfully'}), 200
        else:
            return jsonify({'error': 'Drone not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to delete drone: {str(e)}'}), 500


@api_bp.route("/routes", methods=["GET"])
def get_routes():
    routes = services.get_all_routes()
    return jsonify([route.__dict__ for route in routes])

@api_bp.route("/routes/<route_id>", methods=["GET"])
def get_route_by_id_handler(route_id):
    routes = services.get_route_by_id(route_id)
    if routes:
        return jsonify([route.__dict__ for route in routes])
    else:
        return jsonify({"error": "Route not found"}), 404


@api_bp.route("/routes/<route_id>/<waypoint_id>", methods=["GET"])
def get_route_waypoint(route_id, waypoint_id):
    try:
        waypoint = services.get_route_waypoint(route_id, waypoint_id)
        if waypoint:
            return jsonify(waypoint.__dict__), 200
        else:
            return jsonify({'error': 'Waypoint not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to fetch waypoint: {str(e)}'}), 500


@api_bp.route("/routes/<route_id>/<waypoint_id>", methods=["POST"])
def add_route_waypoint(route_id, waypoint_id):
    """
    Add a new waypoint to a route.
    """
    try:
        waypoint_data = request.get_json()
        new_waypoint = services.add_route_waypoint(route_id, waypoint_id, waypoint_data)
        return jsonify(new_waypoint.__dict__), 201
    except Exception as e:
        return jsonify({'error': f'Failed to add waypoint: {str(e)}'}), 500
    

@api_bp.route("/routes/<route_id>/<waypoint_id>", methods=["DELETE"])
def delete_route_waypoint(route_id, waypoint_id):
    try:
        if services.delete_route_waypoint(route_id, waypoint_id):
            return jsonify({"message": "Waypoint deleted"}), 200
        else:
            return jsonify({"error": "Waypoint not found"}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to delete waypoint: {str(e)}'}), 500


@api_bp.route("/routes/<route_id>/<waypoint_id>", methods=["PUT"])
def update_route_waypoint(route_id, waypoint_id):
    """
    Update an existing waypoint in a route.
    """
    try:
        waypoint_data = request.get_json()
        updated_waypoint = services.update_route_waypoint(route_id, waypoint_id, waypoint_data)
        if updated_waypoint:
            return jsonify(updated_waypoint.__dict__), 200
        else:
            return jsonify({"error": "Waypoint not found"}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to update waypoint: {str(e)}'}), 500


@api_bp.route("/routes/<route_id>", methods=["DELETE"])
def delete_route(route_id):
    try:
        if services.delete_route(route_id):
            return jsonify({"message": "Route deleted"}), 200
        else:
            return jsonify({"error": "Route not found"}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to delete route: {str(e)}'}), 500
    
    
@api_bp.route("/flight_plans", methods=["GET"])
def get_flight_plans():
    """
    Retrieve a list of all flight plans.
    """
    try:
        flight_plans = services.get_all_flight_plans()
        flight_plan_list = [flight_plan.__dict__ for flight_plan in flight_plans]
        return jsonify(flight_plan_list), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch flight plans: {str(e)}'}), 500


@api_bp.route("/flight_plans/<flight_plan_id>", methods=["GET"])
def get_flight_plan(flight_plan_id):
    """
    Retrieve a specific flight plan by its ID.
    """
    try:
        flight_plan = services.get_flight_plan_by_id(flight_plan_id)
        if flight_plan:
            return jsonify(flight_plan.__dict__), 200
        else:
            return jsonify({'error': 'Flight plan not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to fetch flight plan: {str(e)}'}), 500


@api_bp.route("/flight_plans", methods=["POST"])
def add_flight_plan():
    """
    Add a new flight plan.
    """
    try:
        flight_plan_data = request.get_json()
        new_flight_plan = services.add_flight_plan(flight_plan_data)
        return jsonify(new_flight_plan.__dict__), 201
    except Exception as e:
        return jsonify({'error': f'Failed to add flight plan: {str(e)}'}), 500


@api_bp.route("/flight_plans/<flight_plan_id>", methods=["PUT"])
def update_flight_plan(flight_plan_id):
    """
    Update an existing flight plan by its ID.
    """
    try:
        flight_plan_data = request.get_json()
        updated_flight_plan = services.update_flight_plan(flight_plan_id, flight_plan_data)
        if updated_flight_plan:
            return jsonify(updated_flight_plan.__dict__), 200
        else:
            return jsonify({'error': 'Flight plan not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to update flight plan: {str(e)}'}), 500


@api_bp.route("/flight_plans/<flight_plan_id>", methods=["DELETE"])
def delete_flight_plan(flight_plan_id):
    """
    Delete a specific flight plan by its ID.
    """
    try:
        result = services.delete_flight_plan(flight_plan_id)
        if result:
            return jsonify({'message': 'Flight plan deleted successfully'}), 200
        else:
            return jsonify({'error': 'Flight plan not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to delete flight plan: {str(e)}'}), 500
    
@api_bp.route("/pilots", methods=["GET"])
def get_pilots():
    """
    Retrieve a list of all pilots.
    """
    try:
        pilots = services.get_all_pilots()
        pilot_list = [pilot.__dict__ for pilot in pilots]
        return jsonify(pilot_list), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch pilots: {str(e)}'}), 500


@api_bp.route("/pilots/<pilot_id>", methods=["GET"])
def get_pilot(pilot_id):
    """
    Retrieve a specific pilot by their ID.
    """
    try:
        pilot = services.get_pilot_by_id(pilot_id)
        if pilot:
            return jsonify(pilot.__dict__), 200
        else:
            return jsonify({'error': 'Pilot not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to fetch pilot: {str(e)}'}), 500


@api_bp.route("/pilots", methods=["POST"])
def add_pilot():
    """
    Add a new pilot.
    """
    try:
        pilot_data = request.get_json()
        new_pilot = services.add_pilot(pilot_data)
        return jsonify(new_pilot.__dict__), 201
    except Exception as e:
        return jsonify({'error': f'Failed to add pilot: {str(e)}'}), 500


@api_bp.route("/pilots/<pilot_id>", methods=["PUT"])
def update_pilot(pilot_id):
    """
    Update an existing pilot by their ID.
    """
    try:
        pilot_data = request.get_json()
        updated_pilot = services.update_pilot(pilot_id, pilot_data)
        if updated_pilot:
            return jsonify(updated_pilot.__dict__), 200
        else:
            return jsonify({'error': 'Pilot not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to update pilot: {str(e)}'}), 500


@api_bp.route("/pilots/<pilot_id>", methods=["DELETE"])
def delete_pilot(pilot_id):
    """
    Delete a specific pilot by their ID.
    """
    try:
        result = services.delete_pilot(pilot_id)
        if result:
            return jsonify({'message': 'Pilot deleted successfully'}), 200
        else:
            return jsonify({'error': 'Pilot not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to delete pilot: {str(e)}'}), 500