import pandas as pd
import pytest

from source.transform import drop_columns
from source.transform import rename_columns

test_df = pd.read_csv('data/strong.csv')


#  Test successful column removal
def test_drop_columns():
    # Arrange
    test_input = test_df.copy()
    test_columns = ['Duration', 'Distance', 'Seconds', 'Notes', 'Workout Notes', 'RPE']
    expected_columns = [col for col in test_input.columns if col not in test_columns]
    expected_outcome = test_input[expected_columns].copy()
    # Act
    actual_outcome = drop_columns(test_input, test_columns)
    # Assert
    pd.testing.assert_frame_equal(actual_outcome, expected_outcome)


#  Test KeyError for column removal
def test_drop_column_keyerror():
    # Arrange
    test_input = test_df.copy()
    test_columns = ['Duration', 'Does not Exist']
    expected_outcome = 'Check that all columns are in the dataframe'
    # Act
    with pytest.raises(KeyError) as message:
        drop_columns(test_input, test_columns)
    # Assert
    assert expected_outcome in str(message.value)


#  Test for not entering a list
def test_drop_column_valueerror():
    # Arrange
    test_input = test_df.copy()
    test_columns = 1
    expected_outcome = 'The column-list has to be a list.'
    # Act
    with pytest.raises(TypeError) as message:
        rename_columns(test_input, test_columns)
    # Assert
    assert expected_outcome in str(message.value)


column_rename_df = drop_columns(test_df, ['Duration', 'Distance', 'Seconds', 'Notes', 'Workout Notes', 'RPE'])


# Test successful column name change
def test_rename_columns():
    # Arrange
    test_input = column_rename_df.copy()
    test_columns = ['1', '2', '3', '4', '5', '6']
    expected_outcome = test_input.copy()
    expected_outcome.columns = test_columns
    print(expected_outcome.columns)
    # Act
    actual_outcome = rename_columns(test_input, test_columns)
    print(actual_outcome)
    # Assert
    pd.testing.assert_frame_equal(actual_outcome, expected_outcome)


# Test for entering more column names than allowed
def test_rename_too_many_columns():
    # Arrange
    test_input = column_rename_df.copy()
    test_columns = ['1', '2', '3', '4', '5', '6', '7', '8']
    expected_outcome = 'Check that correct number of column names have been entered'
    # Act
    with pytest.raises(ValueError) as message:
        rename_columns(test_input, test_columns)
    # Assert
    assert expected_outcome in str(message.value)


# Test for entering less column names than allowed
def test_rename_too_few_columns():
    # Arrange
    test_input = column_rename_df.copy()
    test_columns = ['1', '2']
    expected_outcome = "Check that correct number of column names have been entered"
    # Act
    with pytest.raises(ValueError) as message:
        rename_columns(test_input, test_columns)
    # Assert
    assert expected_outcome in str(message.value)


#  Test for not entering a list
def test_rename_column_valueerror():
    # Arrange
    test_input = column_rename_df.copy()
    test_columns = 1
    expected_outcome = 'The column-list has to be a list.'
    # Act
    with pytest.raises(TypeError) as message:
        rename_columns(test_input, test_columns)
    # Assert
    assert expected_outcome in str(message.value)


# Turn the index into an id column
# Successful execution
# KeyError
# TypeError
# Exception

# Remove rows where reps = 0
# Successful execution
# KeyError
# TypeError
# Exception


# Creating the workout and exercise tables
# Successful execution
# KeyError
# TypeError
# Exception
# What if i enter a column name that doesn't exist
