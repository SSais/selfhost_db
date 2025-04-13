import pandas as pd


# Transform using pandas
# Removing columns that I don't need. 
df = df.drop(columns=["Duration", "Distance", "Seconds", "Notes", "Workout Notes", "RPE"])

# Renaming columns
df.columns = ['date', 'workout_name', 'exercise_name', 'set_order', 'weight', 'reps']

# Turn the index into an id column
df['set_id'] = df.index + 1

# Remove rows where reps = 0 
df = df[df['reps'] != 0]


# Normalising data
# Creating the workout table
workouts = df[['date', 'workout_name']].drop_duplicates().reset_index(drop=True)
workouts['workout_id'] = workouts.index + 1  # Add index
workouts = workouts[['workout_id', 'date', 'workout_name']]  # Re-order columns

# Creating the exercise table
exercises = df[['exercise_name']].drop_duplicates().reset_index(drop=True)
exercises['exercise_id'] = exercises.index + 1  # Add index
exercises = exercises[['exercise_id', 'exercise_name']]  # Re-order columns

# Creating the sets table 
sets = pd.merge(df, workouts, on=['date', 'workout_name'], how='left')
sets = pd.merge(sets, exercises, on='exercise_name', how='left')
sets = sets.drop(columns=['date', 'workout_name', 'exercise_name'])  # Drop columns
sets = sets[['set_id', 'workout_id', 'exercise_id', 'set_order', 'weight', 'reps']]  # Re-order columns
