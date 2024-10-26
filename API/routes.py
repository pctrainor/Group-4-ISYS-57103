from flask import Blueprint, jsonify  # Import Blueprint
from . import model

# Create the blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/drones')
def get_drones():
    # ... your code to fetch and return drone data ...
    # 1. Connect to your database (using SQLAlchemy or similar)
    # 2. Fetch drone data from the database
    # 3. Create a list of Drone objects from the fetched data 

    drones = [
        model.Drone(BUNO_ID="123", Drone_Model="...", Manufacturer="...", Purchase_Date="...", Serial="...", Status="...", Status_Code="..."),  # Example data with keyword arguments
        model.Drone(BUNO_ID="456", Drone_Model="...", Manufacturer="...", Purchase_Date="...", Serial="...", Status="...", Status_Code="..."),  # Example data with keyword arguments
    ]

    # Convert Drone objects to dictionaries for JSON serialization
    drone_list = [drone.__dict__ for drone in drones] 
    return jsonify(drone_list)