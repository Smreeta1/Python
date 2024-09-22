import camelot
import pandas as pd


tables = camelot.read_pdf('cr.pdf', pages='all', flavor='stream', row_tol=5, edge_tol=500)

print(f"Number of tables extracted: {len(tables)}")

# Save extracted tables to CSV
with open('camtab.csv', 'w', newline='') as csvfile:
    for i, table in enumerate(tables):
        print(f"Table {i + 1}:")
        
        df = table.df  
        print(df)
        csvfile.write('\n\n') 
        
        df.to_csv(csvfile, index=False, mode='a')  #append all tables in the file
        print(f"Data from Table {i + 1} saved to 'camtab.csv'")


