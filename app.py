import PyPDF2
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# Function to load the T5 model and tokenizer
def load_t5_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    return tokenizer, model

# Function to ask a question using the T5 model
def ask_question_from_pdf(pdf_path, question):
    # Step 1: Extract text from PDF
    knowledge_base = extract_text_from_pdf(pdf_path)
    
    # Step 2: Tokenize and prepare the question with the knowledge base
    tokenizer, model = load_t5_model()
    
    # Format the input for the T5 model
    input_text = f"question: {question} context: {knowledge_base}"
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    # Step 3: Generate the answer from the model
    with torch.no_grad():
        outputs = model.generate(inputs['input_ids'], max_length=150)

    # Decode the model's response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

