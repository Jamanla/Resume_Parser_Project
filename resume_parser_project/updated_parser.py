import os
import re
import pandas as pd
import pdfplumber
import docx

# Predefined keywords
KNOWN_SKILLS = ["Python", "Java", "SQL", "Excel", "Power BI", "Tableau", "HTML", "CSS", "JavaScript", "C++"]
KNOWN_DEGREES = ["B.Tech", "M.Tech", "B.E", "M.E", "B.Sc", "M.Sc", "BCA", "MCA", "MBA", "PhD"]

# Extract text from PDF
def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

# Extract text from DOCX
def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

# General text extractor
def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    return ""

# Field extractors
def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else ""

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[\s-]?)?(\(?\d{2,4}\)?[\s-]?)?[\d\s-]{7,}', text)
    return match.group(0) if match else ""

def extract_name(text):
    return text.strip().split("\n")[0] if text else "Unknown"

def extract_linkedin(text):
    match = re.search(r'https?://(www\.)?linkedin\.com/in/[\w\-]+', text)
    return match.group(0) if match else ""

def extract_education(text):
    degrees_found = [degree for degree in KNOWN_DEGREES if degree.lower() in text.lower()]
    return ", ".join(set(degrees_found))

def extract_skills(text):
    return ", ".join([skill for skill in KNOWN_SKILLS if skill.lower() in text.lower()])

def extract_experience(text):
    match = re.search(r'(\d+)[\s-]+years?', text, re.IGNORECASE)
    return match.group(0) if match else ""

# Parse single resume
def parse_resume(file_path):
    text = extract_text(file_path)
    return {
        "File": os.path.basename(file_path),
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_linkedin(text),
        "Education": extract_education(text),
        "Skills": extract_skills(text),
        "Experience": extract_experience(text)
    }

# Parse all resumes in the folder
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

# Main logic
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
