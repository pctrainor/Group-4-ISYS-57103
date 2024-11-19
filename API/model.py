from dataclasses import dataclass

@dataclass
class Drone:
    BUNO_ID: str
    Drone_Model: str
    Manufacturer: str
    Purchase_Date: str 
    Serial: str
    Status: str
    Status_Code: str

@dataclass
class FlightPlan:
    Flight_Plan_ID: str
    BUNO_ID: str
    Pilot_ID: str
    Route_ID: str 
    IsPlanned: bool
    IsComplete: bool

@dataclass
class Route:
    Route_ID: str
    Latitude: float
    Longitude: float
    Waypoint_ID: str 

@dataclass
class Pilot:
    Pilot_ID: str
    Pilot_Current: bool
    Pilot_Hours: int