import os

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


# Before transforming do a check to make sure that there is an index that is numbered from 0 and going up by 1. no duplicates.
# check that the dataframe contains the columns that I'm expecting


# Transform data
# Drop columns
df = drop_columns(df, ["Duration", "Distance", "Seconds", "Notes", "Workout Notes", "RPE"])

# Rename columns
df = rename_columns(df, ['date', 'workout_name', 'exercise_name', 'set_order', 'weight', 'reps'])

# Remove rows where reps = 0
# Set ID

# Create sets and exercises

# Merge


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