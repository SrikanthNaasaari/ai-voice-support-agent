# # Folder: app/faq_parser.py
# import PyPDF2
# from sentence_transformers import SentenceTransformer
# import pickle

# model = SentenceTransformer("all-MiniLM-L6-v2")

# FAQ_PATH = "data/faq.pdf"
# EMBEDDING_PATH = "data/embeddings.pkl"


# def parse_faq():
#     text = ""
#     with open(FAQ_PATH, 'rb') as f:
#         pdf = PyPDF2.PdfReader(f)
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     return [chunk.strip() for chunk in text.split("\n") if chunk.strip() != ""]


# def generate_embeddings():
#     chunks = parse_faq()
#     embeddings = model.encode(chunks)
#     with open(EMBEDDING_PATH, "wb") as f:
#         pickle.dump((chunks, embeddings), f)


import PyPDF2
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

FAQ_PATH = "data/faq.pdf"
EMBEDDING_PATH = "data/embeddings.pkl"

# Parsing the FAQ PDF, grouping multi-line answers into single chunks
def parse_faq():
    text = ""
    with open(FAQ_PATH, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    # Split the text into chunks based on line breaks, but now we want to group multiple lines as answers
    lines = [line.strip() for line in text.split("\n") if line.strip() != ""]
    
    faq_entries = []
    current_entry = ""
    
    for line in lines:
        # Assuming questions are distinct, you can tweak this based on your FAQ's format
        if line.endswith('?'):  # Indicates a new question (this could be adjusted to match your format)
            if current_entry:  # Add the previous entry to the faq_entries
                faq_entries.append(current_entry.strip())
            current_entry = line  # Start a new entry with the question
        else:
            current_entry += " " + line  # Add the line to the current entry (answer lines)
    
    # Add the last entry
    if current_entry:
        faq_entries.append(current_entry.strip())
    
    return faq_entries

# Generate embeddings for the FAQ content
def generate_embeddings():
    faq_entries = parse_faq()  # Get all FAQ entries
    embeddings = model.encode(faq_entries)  # Generate embeddings for each FAQ entry
    
    # Save both the FAQ text and embeddings to a file for future reference
    with open(EMBEDDING_PATH, "wb") as f:
        pickle.dump((faq_entries, embeddings), f)
