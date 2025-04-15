import pandas as pd
import pytest

from source.transform import drop_columns
from source.transform import rename_columns
from source.transform import set_index_as_id
from source.transform import remove_rows_with_no_reps
from source.transform import create_table
from source.transform import left_merge_dataframes

# Setting up testing dataframes
test_df = pd.read_csv('data/strong.csv')
column_rename_test_df = drop_columns(test_df, ['Duration', 'Distance', 'Seconds', 'Notes', 'Workout Notes', 'RPE'])
remove_rows_test_df = column_rename_test_df.copy()
remove_rows_test_df.columns = ['date', 'workout_name', 'exercise_name', 'set_order', 'weight', 'reps']


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


#  Test TypeError for drop column
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


# Test successful column name change
def test_rename_columns():
    # Arrange
    test_input = column_rename_test_df.copy()
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
    test_input = column_rename_test_df.copy()
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
    test_input = column_rename_test_df.copy()
    test_columns = ['1', '2']
    expected_outcome = "Check that correct number of column names have been entered"
    # Act
    with pytest.raises(ValueError) as message:
        rename_columns(test_input, test_columns)
    # Assert
    assert expected_outcome in str(message.value)


#  Test TypeError for rename_column
def test_rename_column_valueerror():
    # Arrange
    test_input = column_rename_test_df.copy()
    test_columns = 1
    expected_outcome = 'The column-list has to be a list.'
    # Act
    with pytest.raises(TypeError) as message:
        rename_columns(test_input, test_columns)
    # Assert
    assert expected_outcome in str(message.value)


# Test that index turns into an id column
def test_set_index_as_id():
    # Arrange
    test_input = test_df.copy()
    test_column_name = 'test'
    expected_outcome = test_df.copy()
    expected_outcome[test_column_name] = expected_outcome.index + 1
    # Act
    actual_outcome = set_index_as_id(test_input, test_column_name)
    # Assert
    pd.testing.assert_frame_equal(actual_outcome, expected_outcome)


# Test TypeError for set index
def test_set_index_as_id_typeerror():
    # Arrange
    test_input = test_df.copy()
    test_column_name = 1
    expected_outcome = 'The column name has to be a string.'
    # Act
    with pytest.raises(TypeError) as message:
        set_index_as_id(test_input, test_column_name)
    # Assert
    assert expected_outcome in str(message.value)


# Test remove rows where reps = 0
def test_remove_rows_with_no_reps():
    # Arrange
    test_input = remove_rows_test_df.copy()
    expected_outcome = test_input[test_input['reps'] != 0]
    # Act
    actual_outcome = remove_rows_with_no_reps(test_input)
    # Assert
    pd.testing.assert_frame_equal(actual_outcome, expected_outcome)


# Test dataframe creation
def test_create_table():
    # Arrange
    test_input = remove_rows_test_df.copy()
    test_column_list = ['date', 'workout_name']
    expected_outcome = test_input[test_column_list].drop_duplicates().reset_index(drop=True)
    # Act
    actual_outcome = create_table(test_input, test_column_list)
    # Assert
    pd.testing.assert_frame_equal(actual_outcome, expected_outcome)


# Test left merge
def test_left_merge_dataframes():
    # Arrange
    test_input_1 = remove_rows_test_df.copy()
    test_input_2 = remove_rows_test_df.copy()
    test_columns_to_merge_on = ['date']
    expected_outcome = test_input_1.merge(test_input_2, on=test_columns_to_merge_on, how='left')
    # Act
    actual_outcome = left_merge_dataframes(test_input_1, test_input_2, test_columns_to_merge_on)
    # Assert
    pd.testing.assert_frame_equal(actual_outcome, expected_outcome)
