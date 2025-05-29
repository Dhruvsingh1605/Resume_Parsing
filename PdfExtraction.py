
import pdfplumber
import re

pdf_path = "/media/dhruv/Local Disk/assignment_1/Resume_Parsing/JMadhanResume.pdf"
lines = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        lines += text.split("\n")

SECTION_HEADERS = [
    "Name", "Contact", "Education", "Skills",
    "Certificates", "Experience", "Projects"
]

header_pattern = re.compile(rf"^({'|'.join(SECTION_HEADERS)})\s*$", re.IGNORECASE)


sections = {}
current_header = None

for line in lines:
    m = header_pattern.match(line.strip())
    if m:
        current_header = m.group(1).title()   
        sections[current_header] = []
    else:
        if current_header:
            if line.strip():
                sections[current_header].append(line.strip())

for sec, content_lines in sections.items():
    print(f"=== {sec} ===")
    if content_lines:
        print(f"Primary entry: {content_lines[0]}")
    else:
        print("<no content found>")
    print()

