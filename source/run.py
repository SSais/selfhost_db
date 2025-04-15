import os

from dotenv import load_dotenv
from source.extract import extract_dataframe_from_CVS


# Extract data into a dataframe
# File path
url = 'data/strong.csv'
df = extract_dataframe_from_CVS(url)


# Transform data

# Drop columns
# Rename columns
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