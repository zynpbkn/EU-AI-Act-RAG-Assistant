from ingest import vector_store
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv

load_dotenv()

retriever = vector_store.as_retriever(search_kwargs={'k': 6})

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# --- Oturum (session) geçmişi ---
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# --- Soru bağlamını düzenleyen prompt ---
contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", "Given a chat history and the latest user question that may refer to previous context, rewrite it as a standalone question. Do not answer it."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# --- Geçmişi dikkate alan retriever oluştur ---
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

# --- Soru-cevap promptu (EU AI Act odaklı) ---
qa_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert assistant on the European Union Artificial Intelligence Act (EU AI Act). "
     "Use the provided context from official EU documents to answer questions accurately and clearly. "
     "If the context doesn’t include enough information, say that clearly. Be formal and informative.\n\nContext: {context}"
    ),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# --- QA zinciri ---
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

# --- Retrieval chain oluştur ---
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# --- Mesaj geçmişi ile zincir ---
qa_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

# --- Uygulamayı çalıştır ---
if __name__ == '__main__':
    session_id = "user123"
    print("💬 Welcome to the EU AI Act Assistant! (type 'quit' to exit)\n")

    while True:
        question = input("Your question: ")

        if question.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break

        try:
            response = qa_chain.invoke(
                {"input": question},
                config={"configurable": {"session_id": session_id}}
            )
            print(f"\nAnswer: {response['answer']}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}")
