import random
import time
import requests

# Route 2 waypoints
route2_waypoints = [
    (36.341631, -94.198761),  # Walton Blvd Walmart (Start)
    (36.489012, -94.321098),  # Center Township
    (36.218765, -94.012345),  # Decatur School District
    (36.412345, -93.890123),  # Bentonvilleville
    (36.154321, -93.765432),  # Sugar Creek Township
    (36.341631, -94.198761)   # Walton Blvd Walmart (End)
]

def simulate_drone_flight(drone_id):
    waypoint_index = 0
    current_waypoint = route2_waypoints[waypoint_index]

    # Initialize latitude and longitude 
    latitude = 36.341631  # Start at Walton Blvd Walmart
    longitude = -94.198761

    while True:
        # Calculate distance to the next waypoint
        lat_diff = current_waypoint[0] - latitude
        lon_diff = current_waypoint[1] - longitude
        distance = (lat_diff**2 + lon_diff**2)**0.5

        # If close enough to the waypoint, move to the next one
        if distance < 0.01:  # Adjust this threshold as needed
            waypoint_index = (waypoint_index + 1) % len(route2_waypoints)
            current_waypoint = route2_waypoints[waypoint_index]
            print(f"Reached waypoint {waypoint_index + 1}: {current_waypoint}")

        # Move towards the current waypoint (simplified simulation)
        latitude += lat_diff * 0.005  # Increased step size for faster movement
        longitude += lon_diff * 0.005

        # Generate altitude within a specific range
        altitude = round(random.uniform(100, 500), 2)  # Simulate flying altitude

        drone_data = {
            "BUNO_ID": drone_id,
            "Drone_Model": "Model X",
            "Manufacturer": "DroneCorp",
            "Purchase_Date": "2023-01-01",
            "Serial": "SN123456",
            "Status": "Active",
            "Status_Code": "A1",
            "Altitude": altitude,
            "Latitude": latitude,
            "Longitude": longitude
        }

        response = requests.put(f"http://localhost:5000/api/drones/{drone_id}", json=drone_data)
        if response.status_code == 200:
            print(f"Updated drone {drone_id} data: {drone_data}")
        else:
            print(f"Failed to update drone {drone_id}: {response.json()}")

        time.sleep(0.9)

if __name__ == "__main__":
    drone_id = input("Enter Drone ID: ")
    simulate_drone_flight(drone_id)
