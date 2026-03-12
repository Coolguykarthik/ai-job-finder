from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

# connect to local Llama3 via Ollama
llm = Ollama(model="llama3")

template = """
Given these skills:

{skills}

Generate 3 job search queries.
Return one query per line only.
"""

prompt = PromptTemplate.from_template(template)

# NEW LangChain pipeline (replaces LLMChain)
chain = prompt | llm


def generate_queries(skills):

    result = chain.invoke({"skills": skills})

    # split output into list
    queries = [q.strip() for q in result.split("\n") if q.strip()]

    return queries