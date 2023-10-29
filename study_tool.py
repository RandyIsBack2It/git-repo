import openpyxl
import re

def keyword_search():
    # Define the filename of the Excel file
    file_name = "study_tool.xlsx"

    # Get user input for the keyword
    print()  # Blank line added
    keyword = input("Enter the keyword to search for: ")
    print()  # Blank line added

    # Prepare a regular expression pattern for the keyword as a whole word
    pattern = r'\b' + re.escape(keyword) + r'\b'

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

            # Check if the keyword (case-insensitive, whole word) is in any of the cells in the row
            if any(cell is not None for cell in row):
                for cell in row:
                    if cell is not None and re.search(pattern, str(cell), re.I):
                        matching_rows.append(row)
                        break

        # Display the matching rows with values in separate rows
        if matching_rows:
            print()  # Blank line added
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

# Menu loop
while True:
    print("\nSelect an Option:")
    print("  1. Keyword Search")  # Added blank space
    print("  2. Additional Feature (Not implemented yet)")
    print("  3. Exit")  # Added blank space
    print()  # Blank line added
    choice = input("Select an option (1/2/3): ")
    print()  # Blank line added

    if choice == '1':
        keyword_search()
    elif choice == '2':
        print("This feature is not implemented yet.")
    elif choice == '3':
        print("Exiting the script. Goodbye!\n")  # Blank line added
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")
