import openpyxl
import re

# Function for performing a keyword search in an Excel file
def keyword_search():
    file_name = "study_tool.xlsx"  # Define the Excel file name

    keyword = input("Enter the keyword to search for: ")  # Get user input for the search keyword
    print()  # Add a blank line here
    pattern = r'\b' + re.escape(keyword) + r'\b'  # Prepare a regular expression pattern for the whole word match

    try:
        workbook = openpyxl.load_workbook(file_name)  # Open the Excel file
        sheet = workbook.active
        matching_rows = []  # Initialize a list to store rows with matching data
        headers = None  # Initialize variable to store column headers

        for row in sheet.iter_rows(values_only=True):
            if not headers:
                headers = row  # Store the first row as headers
                continue

            if any(cell is not None for cell in row):
                for cell in row:
                    if cell is not None and re.search(pattern, str(cell), re.I):
                        matching_rows.append(row)  # Add the row to matching rows if it contains the keyword
                        break

        if matching_rows:
            # Display matching rows with column headers
            for row in matching_rows:
                if any(cell is not None for cell in row):
                    for header, cell in zip(headers, row):
                        if cell is not None:
                            print(f"{header}: {cell}")
                    print()
            print()  # Add a blank line here
        else:
            print("No matching rows found for the keyword.")

        workbook.close()  # Close the Excel file

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main menu loop
while True:
    print("\nSelect an Option:")
    print("  1. Keyword Search")
    print("  2. Additional Feature (Not implemented yet)")
    print("  3. Exit")
    print()  # Add a blank line
    choice = input("Select an option (1/2/3): ")  # Get the user's choice
    print()  # Add a blank line here

    if choice == '1':
        keyword_search()  # Call the keyword_search function for option 1
    elif choice == '2':
        print("This feature is not implemented yet.")  # Display a message for option 2
    elif choice == '3':
        print("Exiting the script. Goodbye!")  # Display a goodbye message
        print()  # Add a blank line here
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")  # Display an error message for invalid choices
