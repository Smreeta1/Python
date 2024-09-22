import pdfplumber
import pandas as pd

def clean_cell(cell):
    if isinstance(cell, str):
        return cell.replace('\n', ' ')
    return cell

def extract_table_name(page):

    text = page.extract_text()
    if text:
        
        lines = text.split('\n')
        for line in lines:
            if line.strip(): 
                return line.strip()
    return "Table Name Not Found"

with pdfplumber.open('cr.pdf') as pdf:

    with open('extract.csv', 'w', newline='') as csvfile: 

        for page_number, page in enumerate(pdf.pages):
            print(f"Processing page {page_number + 1}") 

            table_name = extract_table_name(page)
            table = page.extract_table()

        
            if table:
                # multi-line text for headers and data
                headers = [clean_cell(cell) for cell in table[0]]  # Headers
                rows = [[clean_cell(cell) for cell in row] for row in table[1:]]  # Rows
                csvfile.write(f"{table_name}\n")
                
                df = pd.DataFrame(rows, columns=headers)
                df.to_csv(csvfile, index=False, mode='a')
                csvfile.write('\n\n')

                print(f"Table from page {page_number + 1} appended to extract.csv")
            else:
                print(f"No table found on page {page_number + 1}")

print("Processing is complete.")

