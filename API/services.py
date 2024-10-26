import sqlalchemy as sa  # Or your preferred database library

def get_drone_data():
    # 1. Connect to the database
    engine = sa.create_engine(...)
    # 2. Fetch drone data 
    # 3. Return the data
    return "it worked"