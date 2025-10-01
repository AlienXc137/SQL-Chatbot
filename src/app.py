from dotenv import load_dotenv
import streamlit as st
import os
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
  db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
  return SQLDatabase.from_uri(db_uri)

#SQL chain
def get_sql_chain(db):
    template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
    
    <SCHEMA>{schema}</SCHEMA>
    
    Conversation History: {chat_history}
    
    Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
    
    For example:
    Question: which 3 artists have the most tracks?
    SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
    Question: Name 10 artists
    SQL Query: SELECT Name FROM Artist LIMIT 10;
    
    Your turn:
    
    Question: {question}
    SQL Query:
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm = GoogleGenerativeAI(model="gemini-2.5-flash")

    def get_schema(_):
        return db.get_table_info()
    
    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
    )


if "chat_history" not in st.session_state: #initialize chat history in session state
    st.session_state.chat_history = [ 
        AIMessage(content="Hello! I'm your SQL assistant, Ask me anything related to SQL database.") #initial message
    ]


load_dotenv()

SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.set_page_config(page_title="Chat with SQL", page_icon=":robot_face:")
st.title("Chat with SQL")

with st.sidebar:
    st.subheader("Settings")
    st.write("Simple SQL Chat App, Connect your DB and start chatting!")

    st.text_input("Host", value="localhost", key="Host")  #key argument to store the input value in session state
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User",value="root", key="User")
    st.text_input("Password", type="password",value=SQL_PASSWORD, key="Password")
    st.text_input("Database", value="chinook", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            db = init_database(
                st.session_state["User"], #session state variables to hold the input values (key from above)
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
            )
            st.session_state.db = db #store the db object in session state
            st.success("Connected to database!")

for message in st.session_state.chat_history: #display chat history
    if isinstance(message, HumanMessage): #check if message is from human
        with st.chat_message("Human"): #display human message
            st.markdown(message.content) #display message content
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)

user_query=st.chat_input("Ask your SQL related questions here!")
if user_query is not None and user_query.strip() != "": #check if user input is not empty and not just spaces
    st.session_state.chat_history.append(HumanMessage(content=user_query)) #append human message to chat history

    with st.chat_message("Human"): #display human message
        st.markdown(user_query) 
    
    with st.chat_message("AI"): #display AI message
        sql_chain=get_sql_chain(st.session_state.db) #get SQL chain with db from session state
        response = sql_chain.invoke({
            "chat_history": st.session_state.chat_history,
            "question": user_query
        })
        st.markdown(response)
    
    st.session_state.chat_history.append(AIMessage(content=response)) #append AI message to chat history