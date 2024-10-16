import os
from pathlib import Path
import sqlalchemy as sa
import pandas as pd

# --- File Path Handling ---
# Get the script's directory
script_dir = Path(__file__).parent.resolve()

# Go up one level to the main directory 
main_dir = script_dir.parent 

# Construct paths relative to the main directory
data_folder = main_dir / "data"  # For the database
database_path = data_folder / "drone_data.db"

# Create data folder if it doesn't exist
data_folder.mkdir(parents=True, exist_ok=True)

# --- Database Creation ---
# Create the engine with the absolute path
engine = sa.create_engine(f'sqlite:///{database_path}')

# Define the table structures
metadata = sa.MetaData()

drones = sa.Table(
    'drones', metadata,
    sa.Column('BUNO_ID', sa.String, primary_key=True),
    sa.Column('Drone_Model', sa.String),
    sa.Column('Manufacturer', sa.String),
    sa.Column('Purchase_Date', sa.Date),
    sa.Column('Serial', sa.String),
    sa.Column('Status', sa.String),
    sa.Column('Status_Code', sa.String)
)

flight_plans = sa.Table(
    'flight_plans', metadata,
    sa.Column('Flight_Plan_ID', sa.String, primary_key=True),
    sa.Column('BUNO_ID', sa.String, sa.ForeignKey('drones.BUNO_ID')),
    sa.Column('Pilot_ID', sa.String, sa.ForeignKey('pilots.Pilot_ID')),
    sa.Column('Route_ID', sa.String, sa.ForeignKey('routes.Route_ID')),
    sa.Column('IsPlanned', sa.Boolean),
)

routes = sa.Table(
    'routes', metadata,
    sa.Column('Route_ID', sa.String, primary_key=True),
    sa.Column('Latitude', sa.Float),
    sa.Column('Longitude', sa.Float),
)

pilots = sa.Table(
    'pilots', metadata,
    sa.Column('Pilot_ID', sa.String, primary_key=True),
    sa.Column('Pilot_Current', sa.Boolean),
    sa.Column('Pilot_Hours', sa.Integer)
)


# --- Data Loading ---
# Construct the path to the CSV files in the raw_data folder
csv_data_folder = script_dir / "raw_data"  # Path to the 'utility/raw_data' folder

# Load data from CSV files using pathlib
for table, filename in [
    (drones, csv_data_folder / 'drone.csv'),
    (flight_plans, csv_data_folder / 'flight_plan.csv'),
    (routes, csv_data_folder / 'flight_route.csv'),
    (pilots, csv_data_folder / 'pilot_currency.csv')
]:
    try:
        df = pd.read_csv(filename)
        df.to_sql(table.name, engine, index=False, if_exists='replace')
    except FileNotFoundError:
        print(f"Error: Could not find the file at {filename}")

# --- Database Creation ---
metadata.create_all(engine)
print(f"Database created at: {database_path}")