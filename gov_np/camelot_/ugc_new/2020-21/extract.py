import pdfplumber
import json
universities_data = []

def clean_text(text):
    return text.replace('\n', ' ') if isinstance(text, str) else text

with pdfplumber.open('data.pdf') as pdf:
    for i in range(58, 169):  
        print(f"Processing Page {i + 1}...")
        page = pdf.pages[i]
        tables = page.extract_tables()
    
        current_university_name = None
        current_campus_type = None
        
        # extract text to identify university and campus type
        page_text = page.extract_text()
        for line in page_text.split('\n'):
            if "University" in line:
                current_university_name = line.strip()
                print(f"Found University: {current_university_name}")

            if "Constituent" in line or "Private" in line or "Community" in line:
                current_campus_type = line.strip()
                print(f"Found Campus Type: {current_campus_type}")

        for j, table in enumerate(tables):
            print(f"Processing Table {j + 1} on Page {i + 1}...")
            
            if not table: 
                continue
            
            headers = table[0]
            
            for row in table[1:]:
                code=row[0] 
                campusname = clean_text(row[1]) if len(row) > 1 else None
                province = clean_text(row[2]) if len(row) > 2 else None
                faculty = clean_text(row[3]) if len(row) > 3 else None
                district = clean_text(row[4]) if len(row) > 4 else None
                program = clean_text(row[5])if len(row) > 5 else None
                level = clean_text(row[6])if len(row) > 6 else None
                male = int(row[7]) if len(row) > 6 and row[7].isdigit() else 0
                female = int(row[8]) if len(row) > 7 and row[8].isdigit() else 0
                Total = int(row[9]) if len(row) > 8 and row[9].isdigit() else 0
                
                campus_data = {
                    "Code": code,
                    "campus_name": campusname,
                    "province": province,
                    "District": district,
                    "Faculty": faculty,
                    "program_name": program,
                    "Level":level,
                    "male": male,
                    "Female": female,
                    "total": Total
                    
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

with open('extract.json', 'w') as jsonfile:
    json.dump(universities_data, jsonfile, indent=4)

print("Data has been saved to 'extract.json' ")
