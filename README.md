## PDF Resume Section Extractor
This Python script extracts and organizes content from a resume PDF file into defined sections such as Name, Contact, Education, Skills, and more. It leverages the pdfplumber library for precise text extraction and uses regular expressions to detect section headers.

## 📌 Features
Parses text content from each page of a PDF resume.

Recognizes and segments the resume into structured sections based on predefined headers.

Cleans and organizes section content line by line.

Outputs a summarized view with primary entries for each section.

## 📁 Project Structure
bash
Copy
Edit
.
├── resume_extractor.py  # Main script file
└── README.md            # This file

## ⚙️ Requirements

Python 3.7+

Libraries:

pdfplumber

re (built-in)

Install Requirements
bash
Copy
Edit

pip install pdfplumber

🚀 How It Works
1. PDF Parsing
The script opens a PDF file using pdfplumber:

python
Copy
Edit
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        lines += text.split("\n")
This reads each page of the PDF and splits the extracted text into individual lines for further processing.

2. Section Header Detection
It defines a list of common resume section headers:

python
Copy
Edit
SECTION_HEADERS = [
    "Name", "Contact", "Education", "Skills",
    "Certificates", "Experience", "Projects"
]
These are compiled into a case-insensitive regex pattern:

python
Copy
Edit
header_pattern = re.compile(rf"^({'|'.join(SECTION_HEADERS)})\s*$", re.IGNORECASE)
3. Section Segmentation
The script processes each line of the resume:

If a line matches a section header, a new section is started.

Otherwise, the line is appended to the current section.

python
Copy
Edit
for line in lines:
    m = header_pattern.match(line.strip())
    if m:
        current_header = m.group(1).title()
        sections[current_header] = []
    else:
        if current_header and line.strip():
            sections[current_header].append(line.strip())
4. Summary Output
The script prints the first (primary) entry of each detected section, which is often the most important detail:

python
Copy
Edit
for sec, content_lines in sections.items():
    print(f"=== {sec} ===")
    if content_lines:
        print(f"Primary entry: {content_lines[0]}")
    else:
        print("<no content found>")
    print()

📄 Example Output
text
Copy
Edit
=== Name ===
Primary entry: John Doe

=== Contact ===
Primary entry: +91 9876543210 | john.doe@example.com

=== Education ===
Primary entry: B.Tech in Computer Science, XYZ University

=== Skills ===
Primary entry: Python, Java, SQL

...
📌 Use Cases
Resume parsing for HRTech applications.

Automated document classification and summarization.

Data extraction pipelines for job matching systems.

🔒 Notes
Assumes that headers in the PDF are written on their own lines and match predefined keywords.

Works best with cleanly formatted PDFs (non-scanned).

📬 Future Improvements
Use natural language processing to auto-detect section headers.

Add support for scanned/image-based PDFs using OCR (e.g., pytesseract).

Export extracted data to structured formats like JSON or CSV.

🧑‍💻 Author
Dhruv (replace with your full name and/or link to your GitHub/LinkedIn)

📝 License
This project is licensed under the MIT License — see the LICENSE file for details.
