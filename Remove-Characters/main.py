import pandas as pd

# Replace the path with the actual path to your Excel file
file_path = '/home/husnain/Desktop/record_with_names.xlsx'

# Load the Excel file into a pandas DataFrame using openpyxl as the engine
df = pd.read_excel(file_path, engine='openpyxl')


# Function to remove a specific character (e.g., comma) from a cell
def remove_character(cell_value, character):
    # Handle empty cells correctly
    if pd.isna(cell_value):
        return cell_value

    # Convert the cell value to a string and remove the specified character
    cell_str = str(cell_value)
    cell_str = cell_str.replace(character, '')

    # Convert back to the original data type if it was an integer
    try:
        return int(cell_str)
    except ValueError:
        return cell_str


# Input character to remove from the file
character_to_remove = str(input("Input character to remove from the file: "))

# Apply the function to remove the character from the whole DataFrame
df = df.applymap(lambda cell: remove_character(cell, character_to_remove))

# Save the modified DataFrame back to a new Excel file using openpyxl as the engine
output_file_path = '/home/husnain/Desktop/filtered-unwanted-characters.xlsx'
df.to_excel(output_file_path, index=False, engine='openpyxl')

print(f"All instances of '{character_to_remove}' have been removed from the Excel file.")
