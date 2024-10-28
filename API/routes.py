from flask import Blueprint, jsonify
import api.services as services  # Import your services module

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    return 'Welcome to the Drone Delivery API!', 200

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