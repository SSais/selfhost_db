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
        TypeError if column list is not a list.
        KeyError if columns outside of the dataframe have been added.
        Exception for unexpected errors.
    """
    try:
        return dataframe.drop(columns=columns_list)
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
        TypeError if column list is not a list.
        KeyError if too few or too many columns has been entered.
        Exception for unexpected errors.
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
        TypeError if the column name is not a string.
        Exception for unexpected errors.
    """
    if not isinstance(id_column_name, str):
        raise TypeError('The column name has to be a string.')
    try:
        dataframe[id_column_name] = dataframe.index + 1
        return dataframe
    except Exception as e:
        raise Exception(f'Error: {e}\n An unexpected error has occurred.')


# Remove rows where reps = 0
def remove_rows_with_no_reps(dataframe: pd.DataFrame) -> pd.DataFrame :
    """
    Remove any rows where the number of reps is 0.
    Input:
        Pandas dataframe: The dataframe to be edited.
    Output:
        Pandas dataframe: A dataFrame where there are no reps with the 0 value.
    Raise:
        KeyError if reps is not in the dataframe
        Exception for unexpected errors.
    """
    try:
        dataframe = dataframe[dataframe['reps'] != 0]
        return dataframe
    except KeyError as e:
        raise KeyError(f'Error: {e}\nCheck that "reps" columns is in the dataframe.')
    except Exception as e:
        raise Exception(f"Error: An unexpected error occurred while removing rows: {e}")


# Creating the workout and exercise tables
def create_table(dataframe: pd.DataFrame, new_dataframe_column_list: list) -> pd.DataFrame:
    """
    Used to create a normalised dataframe from an existing dataframe.
    The new dataframe will not have any duplicates.
    Input:
        Pandas dataframe: The dataframe to be normalised.
        new_dataframe_column_list (list): List of columns that will be kept.
    Output:
        Pandas dataframe: A dataFrame where there are no reps with the 0 value.
    Raise:
    """
    return dataframe[new_dataframe_column_list].drop_duplicates().reset_index(drop=True)


# Merge dataframe
def left_merge_dataframes(left_dataframe: pd.DataFrame,
                          right_dataframe: pd.DataFrame,
                          columns_to_merge_on: list
                          ) -> pd.DataFrame:
    """
    Left merge two dataframes.
    Input:
        left_dataframe: The left dataframe to be merged.
        right_dataframe: The right dataframe to be merged.
        columns_to_merge_on: List of columns that will be used to merge.
    Output:
        Pandas dataframe: A dataframe that has been merged.
    Raise:
    """
    return left_dataframe.merge(right_dataframe, on=columns_to_merge_on, how='left')
