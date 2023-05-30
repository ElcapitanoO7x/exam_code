import spacy
from PyPDF2 import PdfReader
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 200000

def extract_questions_and_definitions(text):
    doc = nlp(text)

    questions = []
    definitions = []

    for sent in doc.sents:
        if sent.text.strip().endswith("?"):
            questions.append(sent.text.strip())
        elif ":" in sent.text:
            definitions.append(sent.text.strip())

    return questions, definitions

pdf_file_path = "FileOrganization_Book_22.pdf"
pdf_text = ""

with open(pdf_file_path, "rb") as file:
    reader = PdfReader(file)
    num_pages = len(reader.pages)

    for page_num in range(num_pages):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()

book_questions, book_definitions = extract_questions_and_definitions(pdf_text)

# Save questions to a file
with open("questions.txt", "w", encoding="utf-8") as questions_file:
    for question in book_questions:
        questions_file.write(question + "\n")

# Save definitions to a file
with open("definitions.txt", "w", encoding="utf-8") as definitions_file:
    for definition in book_definitions:
        definitions_file.write(definition + "\n")
