import spacy
from PyPDF2 import PdfReader
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 200000

def extract_questions(text):
    doc = nlp(text)

    questions = []

    for sent in doc.sents:
        if sent.text.strip().endswith("?"):
            questions.append(sent.text.strip())

    return questions

pdf_file_path = "FileOrganization_Book_22.pdf"
pdf_text = ""

with open(pdf_file_path, "rb") as file:
    reader = PdfReader(file)
    num_pages = len(reader.pages)

    for page_num in range(num_pages):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()

book_questions = extract_questions(pdf_text)

for question in book_questions:
    print(question)
