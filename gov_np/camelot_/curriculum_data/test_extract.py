import camelot
import pandas as pd
tables = camelot.read_pdf('1592456510Ni Ma Vi. Science_3-3 - Rev 1.pdf', pages='all', flavor='lattice')

# clean header
def clean_header(df):
    header = df.iloc[0, 0] 
    if '\n' in header:
        new_header = header.split('\n')
        
        # replace first row of the dataframe with the new header
        df.columns = new_header + df.columns[len(new_header):].tolist()
    
    return df[1:].reset_index(drop=True) 

# Save tables to CSV
with open('test_extract.csv', 'w', newline='') as csvfile:
    for i, table in enumerate(tables):
        print(f"Table {i + 1}:")
        
        # Access the DataFrame of the table
        df = table.df
        print(df)
        df = clean_header(df)
        df = df.dropna(how='all')
    
        df.to_csv(csvfile, index=False, header=True)
        
        print(f"Data from Table {i + 1} saved to 'test_extract.csv'")

print('Processing completed.')
