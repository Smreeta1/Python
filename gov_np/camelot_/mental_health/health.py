import camelot
import pandas as pd

tables = camelot.read_pdf(
    "National-Mental-Health-Survey-Report2020.pdf", pages="all", flavor="lattice"
)
print(f"Number of tables extracted: {len(tables)}")

# clean header
def clean_header(df):
    header = df.iloc[0, 0]

    if "\n" in header:
        # Split the first cell by line breaks and create new headers
        new_header = header.split("\n")
        num_columns = len(df.columns)
        if len(new_header) > num_columns:
            new_header = new_header[
                :num_columns
            ]  # Truncate if there are too many headers
        else:
            new_header = new_header + df.columns[len(new_header) :].tolist()
        # Assign new headers
        df.columns = new_header
    return df


def clean_cell(cell):
    if isinstance(cell, str):
        return cell.replace("\n", " ")
    return cell


# Save tables to CSV
with open("health.csv", "w", newline="") as csvfile:
    for i, table in enumerate(tables):
        print(f"Table {i + 1}:")

        df = table.df
        print(df)
        print(f"Table Extracted from page: {table.page}")

        # Clean the headers
        df = clean_header(df)

        df = df.applymap(clean_cell)

        df = df.dropna(how="all")

        df.to_csv(csvfile, index=False, header=True)

        print(f"Data from Table {i + 1} saved to 'health.csv'")
        csvfile.write("\n")

print("Processing completed.")
