import openpyxl

# Define the filename of the Excel file
file_name = "study_tool.xlsx"

# Get user input for the keyword
keyword = input("Enter the keyword to search for: ")

# Open the Excel file
try:
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active

    # Initialize a list to store matching rows
    matching_rows = []

    # Initialize headers
    headers = None

    # Iterate through each row in the sheet
    for row in sheet.iter_rows(values_only=True):
        if not headers:
            headers = row  # First row is assumed to be the headers
            continue

        # Check if the keyword is in any of the cells in the row
        if any(cell is not None and keyword in str(cell) for cell in row):
            matching_rows.append(row)

    # Display the matching rows with values in separate rows
    if matching_rows:
        for row in matching_rows:
            if any(cell is not None for cell in row):
                for header, cell in zip(headers, row):
                    if cell is not None:
                        print(f"{header}: {cell}")
                print()
    else:
        print("No matching rows found for the keyword.")

    # Close the Excel file
    workbook.close()

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
