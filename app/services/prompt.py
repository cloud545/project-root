
from langchain.prompts import ChatPromptTemplate

def build_prompt(system_message: str):
    template = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "{question}")
    ])
    return template
