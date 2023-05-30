import spacy
from PyPDF2 import PdfReader
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 200000

def extract_questions(text):
    doc = nlp(text)
    questions = []
    for sent in doc.sents:
        if is_question(sent):
            questions.append(sent.text.strip())
    return questions
def is_question(sent):
    question_keywords = ["what", "when", "where", "why", "how", "which", "who", "whom", "whose"]
    verbs = ["is", "are", "was", "were", "do", "does", "did", "can", "could", "should", "would", "will", "have", "has", "had", "may", "might", "must","Advantages","Disadvantages"]

    # Check if the sentence starts with a question keyword or contains a verb
    return sent.text.strip().split()[0].lower() in question_keywords or any(token.text.lower() in verbs for token in sent if token.pos_ == "VERB")

pdf_file_path = "FileOrganization_Book_22.pdf"
pdf_text = ""

with open(pdf_file_path, "rb") as file:
    reader = PdfReader(file)
    num_pages = len(reader.pages)

    for page_num in range(num_pages):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()

# Extract questions from the PDF text
book_questions = extract_questions(pdf_text)

for question in book_questions:
    print(question)
