import pandas as pd
import pytest

from source.extract import extract_dataframe_from_CVS


#  Test successful data extraction
def test_data_extraction():
    # Arrange
    test_input = 'data/strong.csv'
    expected_output = pd.read_csv('data/strong.csv')
    # Act
    actual_output = extract_dataframe_from_CVS(test_input)
    # Assert
    pd.testing.assert_frame_equal(actual_output, expected_output)


#  Test FileNotFound
def test_file_not_found():
    # Arrange
    test_input = 'tests/test_data/no_file.csv'
    expected_output = 'File not found at filepath: tests/test_data/no_file.csv'
    # Act & Assert: Checking if the error was raised
    with pytest.raises(FileNotFoundError) as excinfo: 
        extract_dataframe_from_CVS(test_input)
    # Assert :Check if message is in the output
    assert expected_output in str(excinfo.value)


#  Test EmptyFile
def test_empty_file():
    # Arrange
    test_input = 'tests/test_data/empty.csv'
    expected_output = 'There is not data in the file: tests/test_data/empty.csv'
    # Act & Assert: Checking if the error was raised
    with pytest.raises(pd.errors.EmptyDataError) as excinfo: 
        extract_dataframe_from_CVS(test_input)
    # Assert :Check if message is in the output
    assert expected_output in str(excinfo.value)


#  Test Invalid CSV format 
def test_incorrect_file_format():
    # Arrange
    test_input = 'tests/test_data/not_csv.txt'
    expected_output = 'This file is not a CSV file'
    # Act & Assert: Checking if the error was raised
    with pytest.raises(Exception) as excinfo: 
        extract_dataframe_from_CVS(test_input)
    # Assert :Check if message is in the output
    assert expected_output in str(excinfo.value)


# Need to do parsing error
def test_parsing_error():
    # Arrange
    test_input = 'tests/test_data/parse_error.csv'
    expected_output = 'The file could not be parsed, check file content'
    # Act & Assert: Checking if the error was raised
    with pytest.raises(pd.errors.ParserError) as excinfo: 
        extract_dataframe_from_CVS(test_input)
    # Assert :Check if message is in the output
    assert expected_output in str(excinfo.value)
