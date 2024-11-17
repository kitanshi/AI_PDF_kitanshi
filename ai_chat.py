from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def ask_question(knowledge_base, question):
    llm = OpenAI(model="text-davinci-003")  # Replace with open-source models
    qa_chain = RetrievalQA(llm=llm, retriever=knowledge_base.as_retriever())
    return qa_chain.run(question)
