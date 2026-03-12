from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

# connect to local Llama3 model
llm = Ollama(model="llama3")

prompt = PromptTemplate.from_template("""
Extract technical skills from this resume.

Resume:
{resume}

Return only a comma separated list of skills.
""")

# New LangChain pipeline
chain = prompt | llm


def extract_skills(resume_text):
    result = chain.invoke({"resume": resume_text})
    return result