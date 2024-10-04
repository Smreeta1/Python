import pdfplumber
import json

universities_data = []

def clean_text(text):
    if text is None: 
        return ""
    return text.replace('\n', ' ') if isinstance(text, str) else text

with pdfplumber.open('2017-18.pdf') as pdf:
    current_university_name = None 
    last_university_name = None
    
    for i in range(58, 156): 
        print(f"Processing Page {i + 1}...")
        page = pdf.pages[i]
        tables = page.extract_tables()
    
        current_campus_type = None
        
        # Extract text to identify university and campus type
        page_text = page.extract_text()
        if page_text:
            for line in page_text.split('\n'):
            
                if "University" in line or "B.P. Koiral Institute of Health Sciences" in line or "National Academy of Medical Sciences" in line and len(line.split()) <= 6:
                    current_university_name = line.strip()
                    print(f"Found University: {current_university_name}")
                
                    if any(campus_type in line for campus_type in ["Constituent", "Private", "Community"]) and len(line.split()) <= 5:
                        current_campus_type = line.strip()
                        print(f"Found Campus Type: {current_campus_type}")

        # Process each table on the page
        for j, table in enumerate(tables):
            print(f"Processing Table {j + 1} on Page {i + 1}...")
            
            if not table: 
                continue
            
            headers = table[0]
            
            for row in table[1:]:
                CampusName = clean_text(row[0]) if len(row) > 0 else None
                District = clean_text(row[1]) if len(row) > 1 else None
                Program = clean_text(row[2]) if len(row) > 2 else None
                Level = clean_text(row[3]) if len(row) > 3 else None
                Faculty = clean_text(row[4]) if len(row) > 4 else None
                Ecological = clean_text(row[5]) if len(row) > 5 else None
                Province = clean_text(row[6]) if len(row) > 6 else None
            
             
                
                Male = row[7] if len(row) > 7 else '0'  # Set default to '0'
                Female = row[8] if len(row) > 8 else '0'  
                
                Total = row[9] if len(row) > 9 else 'N/A'

                #Total calculation if it's not available or not a valid number
                if Total is None or not str(Total).isdigit():
                   
                    Total = (int(Male) if str(Male).isdigit() else 0) + (int(Female) if str(Female).isdigit() else 0)
                else:
                    Total = int(Total)
                
                          
                campus_data = {
                    "Campus_Name": CampusName,
                    "District": District,
                    "Program": Program,
                    "Level": Level,
                    "Faculty": Faculty,
                    "Ecological": Ecological,
                    "Province": Province,
                    "Male": Male,
                    "Female": Female,
                    "Total": Total
                }

               
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

# Save to JSON
with open('extract.json', 'w') as jsonfile:
    json.dump(universities_data, jsonfile, indent=4)

print("Data has been saved to 'extract.json' ")
