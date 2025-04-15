import os

from dotenv import load_dotenv

load_dotenv()

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')

# Using SQL alchemy to connect to database
from sqlalchemy import create_engine

db_url = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

# Create engine
engine = create_engine(db_url)


# enter data into db
exercises.to_sql('exercises', engine, if_exists='append', index=False)
workouts.to_sql('workouts', engine, if_exists='append', index=False)
sets.to_sql('sets', engine, if_exists='append', index=False)

# Close connection
engine.dispose()