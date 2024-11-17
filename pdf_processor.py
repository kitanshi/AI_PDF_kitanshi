from pypdf import PdfReader
import PyPDF2
import re

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def extract_skills_from_pdf(pdf_path):
    """
    Extracts and displays skills from a PDF file.

    Parameters:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: Extracted skills.
    """
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            content = ""
            
            # Extract text from all pages
            for page in reader.pages:
                content += page.extract_text()
            
            # Define a sample list of skills to search for (you can expand this list)
            skills_keywords = [
                "Python", "JavaScript", "SQL", "Django", "Flask", "React",
                "AWS", "GCP", "Machine Learning", "Data Analysis", "NLP",
                "Pandas", "NumPy", "API Development", "Frappe", "ERPNext"
            ]
            
            # Find matches for skills in the content
            found_skills = []
            for skill in skills_keywords:
                if re.search(rf'\b{skill}\b', content, re.IGNORECASE):
                    found_skills.append(skill)
            
            return list(set(found_skills))  # Return unique skills found

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    pdf_path = "path_to_your_pdf_file.pdf"  # Replace with the actual path to your PDF
    skills = extract_skills_from_pdf(pdf_path)
    
    if skills:
        print("Skills Extracted from the PDF:")
        for skill in skills:
            print(f"- {skill}")
    else:
        print("No skills found or unable to read the PDF.")
