import os
import pandas as pd

from dotenv import load_dotenv

from source.extract import extract_dataframe_from_CVS
from source.transform import drop_columns
from source.transform import rename_columns
from source.transform import set_index_as_id
from source.transform import remove_rows_with_no_reps
from source.transform import create_table
from source.transform import left_merge_dataframes


# Extract data into a dataframe
# File path
url = 'data/strong.csv'
df = extract_dataframe_from_CVS(url)


try: 
# Before transforming do a check to make sure that there is an index that is numbered from 0 and going up by 1. no duplicates.
# check that the dataframe contains the columns that I'm expecting
except Exception as e:
    raise Exception(f'Error: {e}\nAn unexpected error has occurred.')


# Transform data
# Drop columns
df = drop_columns(df, ["Duration", "Distance", "Seconds", "Notes", "Workout Notes", "RPE"])

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


# Load transformed data into DB
# Load in environment variables
load_dotenv()

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')


# I want to check if the ID already exists in the db. 
# If it exists - dont add to databse
# If it does not exist - do add to database