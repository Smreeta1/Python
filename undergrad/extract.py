import pdfplumber
import pandas as pd

#replacing line breaks with space for multiple lines text
def clean_cell(cell):
    if isinstance(cell, str):
        return cell.replace('\n', ' ')
    return cell

def extract_table_name(page):

    text = page.extract_text() #Extract all text from the page
    if text:
        
        lines = text.split('\n')
        for line in lines:
            if line.strip(): 
                return line.strip()
    return "Table Name Not Found"

with pdfplumber.open('Undergraduate_Training_Tables.pdf') as pdf:

    with open('combined_tables.csv', 'w', newline='') as csvfile:
        first_table = True  #to check if it's the first table

        for page_number, page in enumerate(pdf.pages):
            print(f"Processing page {page_number + 1}")  # Print page no.

            table_name = extract_table_name(page)
            table = page.extract_table()

        
            if table:
                # multi-line text for both headers and data
                headers = [clean_cell(cell) for cell in table[0]]  # Headers
                rows = [[clean_cell(cell) for cell in row] for row in table[1:]]  # Rows
                csvfile.write(f"{table_name}\n")

                # Convert to DataFrame and write to CSV
                df = pd.DataFrame(rows, columns=headers)
                df.to_csv(csvfile, index=False, header=first_table, mode='a')
                csvfile.write('\n\n')

                print(f"Table from page {page_number + 1} appended to combined_tables.csv")
            else:
                print(f"No table found on page {page_number + 1}")

print("Processing is complete.")

