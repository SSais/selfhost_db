import pandas as pd


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
    Raise:
        TypeError
        KeyError
        TypeError
        Exception
    """
    try:
        return dataframe.drop(columns=columns_list)
    except TypeError as e:
        raise TypeError(f'Error: {e}\nThe column-list has to be a list.')
    except KeyError as e:
        raise KeyError(f'Error: {e}\nCheck that all columns are in the dataframe.')
    except TypeError as e:
        raise TypeError(f'Error: {e}\nThe column-list has to be a list.')
    except Exception as e:
        raise Exception(f'Error: {e}\nAn unexpected error has occurred.')


# Renaming columns
def rename_columns(dataframe: pd.DataFrame, columns_list: list) -> pd.DataFrame:
    """
    Re-name columns from a dataframe, columns will be renamed in order of entry.
    Input:
        Pandas dataframe: The dataframe to be edited.
        columns_list (list): The new column names, has to match number of columns in dataframe.
    Output:
        Pandas dataframe: A dataFrame with new columns names.
    Raise:

    """
    try:
        dataframe.columns = columns_list
        return dataframe
    except TypeError as e:
        raise TypeError(f'Error: {e}\nThe column-list has to be a list.')
    except ValueError as e:
        raise ValueError(f'Error: {e}\nCheck that correct number of column names have been entered.')
    except Exception as e:
        raise Exception(f'Error: {e}\n An unexpected error has occurred.')


# Turn the index into an id column
def set_index_as_id(dataframe: pd.DataFrame, id_column_name: str) -> pd.DataFrame:
    """
    Set the index as ID, but adding 1 so that ID starts from 1.
    Input:
        Pandas dataframe: The dataframe to be edited.
        id_column_name (list): Name of the new ID column.
    Output:
        Pandas dataframe: A dataFrame with the new ID column.
    Raise:
    """
    try:
        dataframe[id_column_name] = dataframe.index + 1
        return dataframe
    except KeyError as e:
        raise KeyError(f'Error: {e}\nCheck that column exists in the dataframe.')
    except TypeError as e:  # If not a string?test
        raise TypeError(f'Error: {e}\nThe column-name has to be a string.')
    except Exception as e:
        raise Exception(f'Error: {e}\n An unexpected error has occurred.')   


# Remove rows where reps = 0
def remove_rows_with_no_reps(dataframe: pd.DataFrame, reps_column_name: str = 'reps') -> pd.DataFrame :
    """
    
    Input:
        
    Output:
        
    Raise:
    """
    try:
        dataframe = dataframe[dataframe[reps_column_name] != 0]
        return dataframe
    except KeyError as e:
        raise KeyError(f'Error: {e}\nCheck that column exists in the dataframe.')
    except TypeError as e:
        raise TypeError(f'Error: {e}\nThe column-name has to be a string.')
    except Exception as e:
        raise Exception(f"Error: An unexpected error occurred while removing rows: {e}")


# Creating the workout and exercise tables
def create_table(dataframe: pd.DataFrame, new_dataframe_column_list: list) -> pd.DataFrame:
    """
    
    Input:
        
    Output:
        
    Raise:
    """
    return dataframe[new_dataframe_column_list].drop_duplicates().reset_index(drop=True)


# Merge dataframe
def lef_merge_dataframes(left_dataframe: pd.DataFrame, 
                         right_dataframe: pd.DataFrame, 
                         columns_to_merge_on: list
                         ) -> pd.DataFrame:
    """
    
    Input:
        
    Output:
        
    Raise:
    """
    return left_dataframe.merge(right_dataframe, on=columns_to_merge_on, how='left')
