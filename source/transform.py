import pandas as pd


["Duration", "Distance", "Seconds", "Notes", "Workout Notes", "RPE"]


# Transform using pandas
# Removing columns that I don't need.
def drop_columns(dataframe: pd.DataFrame, columns_list: list) -> pd.DataFrame:
    """
    Drop defined columns from a dataframe.
    Input:
        Pandas dataframe: The dataframe to be edited.
        columns_list (list): The names of columns to be dropped.
    Output:
        Pandas dataframe: A dataFrame with the dropped columns.
    """
    try:
        return dataframe.drop(columns=columns_list)
    except KeyError as e:
        raise KeyError(f'Error: {e}\nCheck that all columns are in the dataframe.')
    except TypeError as e:
        raise TypeError(f'Error: {e}\nThe column-list has to be a list.')
    except Exception as e:
        raise Exception(f'Error: {e}\nAn unexpected error has occurred.')


['date', 'workout_name', 'exercise_name', 'set_order', 'weight', 'reps']


# Renaming columns
def rename_columns(dataframe: pd.DataFrame, columns_list: list) -> pd.DataFrame:
    """
    Re-name columns from a dataframe, columns will be renamed in order of entry.
    Input:
        Pandas dataframe: The dataframe to be edited.
        columns_list (list): The new column names, has to match number of columns in dataframe.
    Output:
        Pandas dataframe: A dataFrame with new columns names.
    """
    try:
        dataframe.columns = columns_list
        return dataframe
    except ValueError as e:
        raise ValueError(f'Error: {e}\nCheck that correct number of column names have been entered.')
    except TypeError as e:
        raise TypeError(f'Error: {e}\nThe column-list has to be a list.')
    except Exception as e:
        raise Exception(f'Error: {e}\n An unexpected error has occurred.')

# # Turn the index into an id column
# df['set_id'] = df.index + 1

# # Remove rows where reps = 0 
# df = df[df['reps'] != 0]


# # Normalising data
# # Creating the workout table
# workouts = df[['date', 'workout_name']].drop_duplicates().reset_index(drop=True)
# workouts['workout_id'] = workouts.index + 1  # Add index
# workouts = workouts[['workout_id', 'date', 'workout_name']]  # Re-order columns

# # Creating the exercise table
# exercises = df[['exercise_name']].drop_duplicates().reset_index(drop=True)
# exercises['exercise_id'] = exercises.index + 1  # Add index
# exercises = exercises[['exercise_id', 'exercise_name']]  # Re-order columns

# # Creating the sets table 
# sets = pd.merge(df, workouts, on=['date', 'workout_name'], how='left')
# sets = pd.merge(sets, exercises, on='exercise_name', how='left')
# sets = sets.drop(columns=['date', 'workout_name', 'exercise_name'])  # Drop columns
# sets = sets[['set_id', 'workout_id', 'exercise_id', 'set_order', 'weight', 'reps']]  # Re-order columns