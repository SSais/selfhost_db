from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Set up dictionary
df_dictionary = {
    'workouts': [df_workouts, 'workout_id'],
    'exercises': [df_exercises, 'exercise_id'],
    'sets': [df_sets, 'set_id']
    }

# Load in environment variables
load_dotenv()
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')

# Create engine
db_url = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"
engine = create_engine(db_url)

# Load new data to DB
with engine.connect() as connection:
    for key, value in df_dictionary.items():
        # Define variables
        df = value[0]
        id_column = value[1]
        table_name = key

        # Get ID count from DB
        count_query = text(f"SELECT COUNT({id_column}) FROM {table_name}")
        result = connection.execute(count_query)
        id_count_from_db = result.scalar_one()

        # Get ID count from dataframe
        id_count_from_df = df[id_column].count()

        if id_count_from_db < id_count_from_df:
            select_rows_from_df = df[id_count_from_db:]

            # Add rows to DB
            select_rows_from_df.to_sql(table_name, engine, if_exists='append', index=False)
            print(f"Successfully added {id_count_from_df - id_count_from_db} new records to {table_name}.")
        else:
            print(f"No new records added to {table_name}.")
engine.dispose()
