import os
import re
import pandas as pd
import pdfplumber
import docx

# Simple skill set for matching
KNOWN_SKILLS = ["Python", "Java", "SQL", "Excel", "Power BI", "Tableau", "HTML", "CSS", "JavaScript", "C++"]

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    return ""

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else ""

def extract_phone(text):
    match = re.search(r'(\+\d{1,3}[\s-]?)?(\(?\d{2,4}\)?[\s-]?)?[\d\s-]{7,}', text)
    return match.group(0) if match else ""

def extract_name(text):
    return text.strip().split("\n")[0] if text else "Unknown"

def extract_skills(text):
    return ", ".join([skill for skill in KNOWN_SKILLS if skill.lower() in text.lower()])

def extract_experience(text):
    match = re.search(r'(\d+)[\s-]+years?', text, re.IGNORECASE)
    return match.group(0) if match else ""

def parse_resume(file_path):
    text = extract_text(file_path)
    return {
        "File": os.path.basename(file_path),
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
        "Experience": extract_experience(text)
    }

def parse_all_resumes(folder):
    results = []
    for file in os.listdir(folder):
        if file.endswith((".pdf", ".docx")):
            full_path = os.path.join(folder, file)
            try:
                print(f"Parsing: {file}")
                results.append(parse_resume(full_path))
            except Exception as e:
                print(f"Failed to parse {file}: {e}")
    return results

if __name__ == "__main__":
    os.makedirs("resumes", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    data = parse_all_resumes("resumes")
    if data:
        df = pd.DataFrame(data)
        df.to_excel("output/parsed_data.xlsx", index=False)
        print("✅ Exported to output/parsed_data.xlsx")
    else:
        print("⚠️ No resumes parsed.")
