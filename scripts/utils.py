import pandas as pd


def extract_names_from_csv(csv_path, column_name='Nom'):
    """
    Extract names from a specified column in a CSV file.

    Parameters:
    csv_path (str): The path to the CSV file.
    column_name (str): The name of the column containing the names. Default is 'Nom'.

    Returns:
    list: A list of names extracted from the specified column.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        return f"Error: Column '{column_name}' not found in the CSV file."

    # Extract names from the specified column and convert it to a list
    names_list = df[column_name].dropna().tolist()

    return names_list
