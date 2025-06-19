# Resume_Parser_Project
An automated Python tool that extracts structured information from multiple .pdf and .docx resumes and exports the results into a clean Excel file — perfect for recruiters, HR teams, and data analysts.
Here's a complete and polished **GitHub project description** you can use in your repository `README.md`:

---

# 📄 Resume Parser in Python

An automated Python tool that extracts structured information from multiple `.pdf` and `.docx` resumes and exports the results into a clean Excel file — perfect for recruiters, HR teams, and data analysts.

---

## 🚀 Features

✅ Supports `.pdf` and `.docx` resumes
✅ Extracts key fields:

* Name
* Email
* Phone Number
* Education
* Skills
* Experience
* Address
* LinkedIn URL
* GitHub Profile
* Portfolio Website

✅ Outputs to `Excel (.xlsx)`
✅ Auto-opens result in Excel (Windows)
✅ Skips temp/system files (`~$...`)
✅ Requires **no manual labeling or templates**

---

## 🧰 Tech Stack

* **Python 3.7+**
* `pdfplumber` – PDF parsing
* `python-docx` – DOCX reading
* `pandas` – DataFrame + Excel export
* `openpyxl` – Excel writing
* `re` – Regex matching

---

## 📁 Folder Structure

```
resume_parser_project/
├── resumes/         # Drop your resume files here
├── output/          # Excel file will be saved here
├── cleaned_resume_parser.py
```

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/resume-parser.git
cd resume-parser

pip install -r requirements.txt
```

Or manually install:

```bash
pip install pandas pdfplumber python-docx openpyxl
```

---

## ▶️ Usage

1. Place all resumes inside the `resumes/` folder
2. Run the script:

```bash
python cleaned_resume_parser.py
```

3. Output will be saved in:

```
output/parsed_data.xlsx
```

If you're on Windows, Excel will open automatically.

---

## 🧪 Example Output

| Name           | Email            | Phone        | Skills                | Experience |
| -------------- | ---------------- | ------------ | --------------------- | ---------- |
| Jamanla Suresh | jamanlas357\@... | +91-76750... | Python, SQL, Power BI | 3 years    |

---

## 🧠 Ideas for Extension

* ✅ Streamlit web app for uploading resumes
* 📊 Resume scoring based on skills match
* ☁️ Export to Google Sheets or Airtable
* 🔍 Section-level tagging: Education, Projects, Experience

---

## 📜 License

MIT License — feel free to use and modify for personal or commercial use.

---

Let me know if you'd like a:

* `README.md` file generated
* GitHub tags, topics, or banner created
* GitHub Actions CI workflow added
