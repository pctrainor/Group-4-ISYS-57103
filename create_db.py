import sqlalchemy as sa
import pandas as pd

# Create database engine
engine = sa.create_engine('sqlite:///drone_data.db')

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

# Load data from CSV files and insert into tables
for table, filename in [(drones, 'drone.csv'), (flight_plans, 'flight_plan.csv'), 
                         (routes, 'flight_route.csv'), (pilots, 'pilot_currency.csv')]:
    df = pd.read_csv(filename)
    df.to_sql(table.name, engine, index=False, if_exists='replace')  # Change to 'append'

# Create the database
metadata.create_all(engine)