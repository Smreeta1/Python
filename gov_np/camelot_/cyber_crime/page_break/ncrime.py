import camelot
import pandas as pd
import csv

def clean_cell(cell):
    if isinstance(cell, str):
        return cell.replace('\n', ' ')
    return cell

# Function to combine tables on multiple pages
def get_continued_tables(tables, threshold=15):
    continued_tables = {}
    previous_table = None
    group_counter = 0
    page_height = 792  # Usual PDF page height
    
    for i, table in enumerate(tables):
        if previous_table and table.page == previous_table.page + 1 and len(table.df.columns) == len(previous_table.df.columns):
            prev_table_bottom = previous_table._bbox[1]
            current_table_top = table._bbox[3]
            
            # Check if tables continue across pages based on their positions
            if prev_table_bottom < 0.15 * page_height and current_table_top > 0.85 * page_height:
                if group_counter not in continued_tables:
                    continued_tables[group_counter] = [previous_table]
                continued_tables[group_counter].append(table)
            else:
                group_counter += 1
        else:
            group_counter += 1
        
        previous_table = table

    return [value for value in continued_tables.values()]

# save tables to CSV
def save_tables_to_csv(tables, continued_tables, output_csv='ncrime.csv'):
    written = []
    batch_size = 1000
    
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for table in tables:
            if table in written:
                continue
            df = table.df
            # Clean cells
            df = df.applymap(clean_cell)
            df = df.dropna(how='all')

            df.to_csv(csvfile, index=False, header=True)
            
            # if table continues over pages, add the remaining parts
            for group in continued_tables:
                if table in group:
                    for continued_table in group:
                        if continued_table != table and continued_table not in written:
                            
                            df = df.applymap(clean_cell)
                            df = df.dropna(how='all')
                            df.to_csv(csvfile, index=False, header=False)
                            written.append(continued_table)
            written.append(table)
            csvfile.write('\n')

# extract tables from the PDF
tables = camelot.read_pdf('cybercrime.pdf', pages='all', flavor='lattice')
print(f"Number of tables extracted: {len(tables)}")

# Detect tables that continue across pages
continued_tables = get_continued_tables(tables)

# Save tables to CSV
save_tables_to_csv(tables, continued_tables)

print('Processing completed.')
