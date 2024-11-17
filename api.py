from fastapi import FastAPI, UploadFile, File
from pdf_processor import extract_text_from_pdf
from knowledge_base import build_knowledge_base
from ai_chat import ask_question

app = FastAPI()
knowledge_base = None

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.get("/query/")
async def query(question: str):
    if not knowledge_base:
        return {"error": "No knowledge base found. Please upload files first."}
    response = ask_question(knowledge_base, question)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
