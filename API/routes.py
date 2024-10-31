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


@api_bp.route(
    "/drones/<buno_id>", methods=["DELETE"])  # Changed drone_id to buno_id
def delete_drone(buno_id):  # Changed drone_id to buno_id
    """
    Delete a specific drone by its ID.
    """
    try:
        result = services.delete_drone(
            buno_id)  # Call the function from services.py and pass buno_id
        if result:
            return jsonify({'message': 'Drone deleted successfully'}), 200
        else:
            return jsonify({'error': 'Drone not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to delete drone: {str(e)}'}), 500