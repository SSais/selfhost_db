import pandas as pd


class NotCSVError(Exception):
    """Custom exception raised when the file is not in CSV format."""
    pass


def extract_dataframe_from_CVS(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file, return data as a df.
    Input:
        file_path (str): The path to the CSV file.
    Output:
        Pandas dataframe: A dataFrame containing the data, or an error if it occurs.
    Raise: 
        NotCSVError if file is in the wrong format.
        FileNotFoundError if file does not exist.
        EmptyDataError if there is no data in the file.
        ParserError if the file cannot be parsed.
        Exception for unexpected errors.
    """
    try:
        is_csv_file(file_path)

        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Error: {e}\nFile not found at filepath: {file_path}.')
    except pd.errors.EmptyDataError as e:
        raise pd.errors.EmptyDataError(f'Error: {e}\nThere is not data in the file: {file_path}.')
    # Raise error if file is not in the correct format
    # During testing determined that ParseError is not reliable
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f'Error: {e}\nThe file could not be parsed, check file content.')
    except Exception as e:
        raise Exception(f'Error: {e}\nAn unexpected error has occurred.')


def is_csv_file(file_path: str):
    if '.csv' not in file_path:
        raise NotCSVError('This file is not a CSV file.')
