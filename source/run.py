from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

# Load functions
from source.extract import extract_dataframe_from_CVS
from source.transform import drop_columns
from source.transform import rename_columns
from source.transform import set_index_as_id
from source.transform import remove_rows_with_no_reps
from source.transform import create_table
from source.transform import left_merge_dataframes

# EXTRACT
# File path
url = 'data/strong.csv'
df = extract_dataframe_from_CVS(url)

# Dataframe check pre-transformation
try: 
    # Check that index starts at 0 and is unique
    if min(df.index) == 0 and df.index.is_unique == True and len(df.index) > 3000:
        print('Index starts at 0 and is unique')
    else:
        raise Exception('Index is incorrect') 

    # Check for expected columns
    expected_columns = ['Date', 'Workout Name', 'Duration', 'Exercise Name', 'Set Order', 'Weight', 'Reps', 'Distance', 'Seconds', 'Notes', 'Workout Notes', 'RPE']
    actual_columns = df.columns
    if expected_columns == actual_columns:
        print('Expected columns are present')
    else:
        raise Exception('Column(s) missing from the data') 
except Exception as e:
    raise Exception(f'Error: {e}\nAn unexpected error has occurred, please check extracted data is correct.')


# TRANSFORM
# Drop columns
df = drop_columns(df, ['Duration', 'Distance', 'Seconds', 'Notes', 'Workout Notes', 'RPE'])

# Rename columns
df = rename_columns(df, ['date', 'workout_name', 'exercise_name', 'set_order', 'weight', 'reps'])

# Remove rows where reps = 0
df = remove_rows_with_no_reps(df)

# Set ID
df = set_index_as_id(df, 'set_id')

# Create workout dataframe
df_workouts = create_table(df, ['date', 'workout_name'])
df_workouts = set_index_as_id(df_workouts, 'workout_id')
df_workouts = df_workouts[['workout_id', 'date', 'workout_name']]

# Create exercises dataframe
df_exercises = create_table(df, ['exercise_name'])
df_exercises = set_index_as_id(df_exercises, 'exercise_id')
df_exercises = df_exercises[['exercise_id', 'exercise_name']]

# Create sets dataframes
df_sets = left_merge_dataframes(df, df_workouts, ['date', 'workout_name'])
df_sets = left_merge_dataframes(df_sets, df_exercises, 'exercise_name' )
df_sets = drop_columns(df_sets, ['date', 'workout_name', 'exercise_name'])
df_sets= df_sets[['set_id', 'workout_id', 'exercise_id', 'set_order', 'weight', 'reps']]

try: 
# Before loading check columns of the new tables are correct
# Check there are no duplicates in id
# Should be no 0's in rep column 
except Exception as e:
    raise Exception(f'Error: {e}\nAn unexpected error has occurred.')

# LOAD
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
