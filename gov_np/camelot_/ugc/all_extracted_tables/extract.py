import camelot
import pandas as pd

tables = camelot.read_pdf('kpyDIM.pdf', pages='all', flavor='lattice')
print(f"Number of tables extracted: {len(tables)}")

#clean header
def clean_header(df):
    # to check if the first row contains line breaks 
    header = df.iloc[0, 0]
    
    if '\n' in header:
        # Split the first cell by line breaks and create new headers
        new_header = header.split('\n')
        df.columns = new_header[:1] + df.columns[1:].tolist()
    
    return df

def clean_cell(cell):
    if isinstance(cell, str):
        return cell.replace('\n', ' ')
    return cell

# Save tables to CSV
with open('kpyDIM.csv', 'w', newline='') as csvfile:
    for i, table in enumerate(tables):
        print(f"Table {i + 1}:")
        
        df = table.df
        print(df)
        print(f"Table Extracted from page: {table.page}")
        
        # Clean the headers
        df = clean_header(df)
        
        # Clean each cell in the DataFrame
        df = df.applymap(clean_cell)
        
        df = df.dropna(how='all')
        
        df.to_csv(csvfile, index=False, header=True)
        
        print(f"Data from Table {i + 1} saved to 'kpyDIM.csv'")
        csvfile.write('\n')  

print('Processing completed.')
