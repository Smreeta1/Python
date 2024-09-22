import camelot
import pandas as pd
import re

def extract_tables(pdf_file, output_csv):
 
    tables = camelot.read_pdf(pdf_file, flavor='stream', pages='all', row_tol=10, edge_tol=500)
    print(f"Number of tables extracted: {len(tables)}")
    
    with open(output_csv, 'w', newline='') as csvfile:
        for i, table in enumerate(tables):
            df = table.df  
            
            if len(df.columns) >= 3 and len(df) > 2:
               
                table_name = None
                lines = table.df.to_string().splitlines()
                
               # find the table name above the header
                table_name = "Table Name Not Found"
                for line in lines:
                    if re.search(r'Table\s+\d+\.\d+\s*:', line):
                        table_name = line.strip()  # current table name
                        break
                if table_name != "Table Name Not Found":
                    print(f"Valid table added: {table_name}")
                    csvfile.write(f"{table_name}\n")  # Write the table name
                    df.to_csv(csvfile, index=False) 
                    csvfile.write('\n\n') 
           
    print(f"Valid tables saved as '{output_csv}'.")

pdf_path = 'cr.pdf'
output_csv_path = 'refined.csv'  
extract_tables(pdf_path, output_csv_path)
print("Processing completed.")