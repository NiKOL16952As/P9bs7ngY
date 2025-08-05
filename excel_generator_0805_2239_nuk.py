# 代码生成时间: 2025-08-05 22:39:49
import openpyxl
def create_excel(title, data, sheet_name='Sheet1', file_name='generated_excel.xlsx'):
    """This function generates an Excel file with the given title, data, and sheet name.

    Args:
        title (str): The title of the Excel file.
        data (list of list): A list of lists containing the data to be written into the Excel file.
        sheet_name (str): The name of the sheet in the Excel file.
        file_name (str): The name of the Excel file to be generated.

    Returns:
        None

    Raises:
        Exception: If there is an error while writing to the Excel file.
    """
    try:
        # Create a new Excel workbook
        wb = openpyxl.Workbook()
        # Get the active sheet
        ws = wb.active
        # Set the sheet name
        ws.title = sheet_name
        # Write the title in the first row
        ws.append([title])
        # Write the data into the Excel sheet
        for row in data:
            ws.append(row)
        # Save the Excel workbook
        wb.save(file_name)
        print(f'Excel file {file_name} created successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')
def main():
    # Example usage of the create_excel function
    title = 'Sample Excel Data'
    data = [
        ['Column 1', 'Column 2', 'Column 3'],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    create_excel(title, data)
if __name__ == '__main__':
    main()