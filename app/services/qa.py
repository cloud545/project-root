
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from app.services.vectorstore import get_vectorstore
from app.services.prompt import build_prompt

# Initialize LLM
def get_qa_chain(system_message: str):
    retriever = get_vectorstore().as_retriever()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm = ChatOpenAI(model_name="gpt-4", temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

    prompt = build_prompt(system_message)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )
    return chain

def ask_question(system_message: str, question: str):
    chain = get_qa_chain(system_message)
    result = chain({"question": question})
    return result["answer"]
