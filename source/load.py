from dotenv import load_dotenv
import os
from sqlalchemy import create_engine


load_dotenv()

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')

db_url = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

# Create engine
engine = create_engine(db_url)

df_dictionary = {
    'workouts': [workouts, 'workout_id'],
    'exercises': [exercises, 'exercise_id'],
    'sets': [sets, 'set_id']
    }

with engine.connect() as connection:
    for key, value in df_dictionary.items():
    
    df = value[0]
    id_column = value[1]
    table_name = key  
    
    # Get the number from the DB
    id_count_from_db = text(f"SELECT COUNT({id_column}) FROM {table_name}")
    id_count_from_db = connection.execute(id_count_from_db)
    id_count_from_db = id_count_from_db.scalar_one()

    # Get total id from the dataframe
    id_count_from_df = df[id_column].count()

    # Check if the number from the dataframe is higher than db
    if id_count_from_db < id_count_from_df:
    # Get the number at which I need to start from and what number I need to go to
        selected = df[id_count_from_db:]
        # Add those to the databse
        selected.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Successfully added {id_count_from_df - id_count_from_db} new records to {table_name}.")
    else:
        print(f"No new records found for {table_name}.")
# Close connection
engine.dispose()
