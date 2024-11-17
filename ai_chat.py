from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import pdfplumber

# Function to load the T5 model and tokenizer
def load_t5_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    return tokenizer, model

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# Function to ask a question using the T5 model
def ask_question_from_pdf(pdf_path, question):
    # Extract text from the PDF
    knowledge_base = extract_text_from_pdf(pdf_path)
    
    # Load the model and tokenizer
    tokenizer, model = load_t5_model()

    # Format the input text for the model
    input_text = f"Answer the following question based on the text from the document: {question} Context: {knowledge_base}"

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

    # Generate the response with more controlled output
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=512,  # Limit the response length
            num_beams=5,     # Beam search for better answers
            temperature=0.7, # Set temperature for randomness
            top_p=0.9,       # Set nucleus sampling to control randomness
            no_repeat_ngram_size=2 # Avoid repetitive responses
        )

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
