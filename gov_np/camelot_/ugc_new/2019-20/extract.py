import pdfplumber
import json

universities_data = []

def clean_text(text):
    if text is None:  
        return ""
    return text.replace('(cid:415)', 't').replace('\n', ' ').replace('(cid:425)', 'tt') if isinstance(text, str) else text

with pdfplumber.open('2019-20.pdf') as pdf:
    current_university_name = None  
    
    for i in range(54, 163):  
        print(f"Processing Page {i + 1}...")
        page = pdf.pages[i]
        tables = page.extract_tables()
    
        current_campus_type = None
        
        # Extract text to identify university and campus type
        page_text = page.extract_text()
        if page_text:
            for line in page_text.split('\n'):
                
                if "University" in line and len(line.split()) <= 5:  
                    current_university_name = line.strip()
                    print(f"Found University: {current_university_name}")
                
                if "Constituent" in line or "Private" in line or "Community" in line:
                    current_campus_type = line.strip()
                    print(f"Found Campus Type: {current_campus_type}")
        
        
        # Process each table on the page
        for j, table in enumerate(tables):
            print(f"Processing Table {j + 1} on Page {i + 1}...")
            
            if not table: 
                continue
            
            headers = table[0]
            
            for row in table[1:]:
                code = row[0] if len(row) > 0 else None
                Campus = clean_text(row[1]) if len(row) > 1 else None
                Province = clean_text(row[2]) if len(row) > 2 else None
                District = clean_text(row[3]) if len(row) > 3 else None
                Faculty = clean_text(row[4]) if len(row) > 4 else None
                Level = clean_text(row[5]) if len(row) > 5 else None
                Male = int(row[6]) if len(row) > 6 and row[6].isdigit() else 0
                Female = int(row[7]) if len(row) > 7 and row[7].isdigit() else 0
                Total = int(row[8]) if len(row) > 8 and row[8].isdigit() else 0
                
                campus_data = {
                    "Code": code,
                    "campus_name": Campus,
                    "province": Province,
                    "District": District,
                    "Faculty": Faculty,
                    "Level": Level,
                    "male": Male,
                    "Female": Female,
                    "total": Total
                }

                # Check if the university already exists in the data
                university_data = next((u for u in universities_data if u['university_name'] == current_university_name), None)
                if not university_data:
                    university_data = {
                        "university_name": current_university_name,
                        "campus_types": []
                    }
                    universities_data.append(university_data)

                
                campus_type_data = next((ct for ct in university_data['campus_types'] if ct['type'] == current_campus_type), None)
                if not campus_type_data:
                    campus_type_data = {
                        "type": current_campus_type,
                        "campuses": []
                    }
                    university_data['campus_types'].append(campus_type_data)

        
                campus_type_data['campuses'].append(campus_data)

# Save the data to JSON
with open('extract.json', 'w') as jsonfile:
    json.dump(universities_data, jsonfile, indent=4)

print("Data has been saved to 'extract.json' ")
