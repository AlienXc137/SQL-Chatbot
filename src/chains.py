from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI

# from .db import init_database
# from .config import SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_PORT, SQL_DATABASE

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

def get_response_chain(db):
    template = """
    YYou are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, question, sql query, and sql response, write a natural language response.

    <SCHEMA>{schema}</SCHEMA>
    Conversation History: {chat_history}
    SQL Query: {query}
    User Question: {question}
    SQL Response: {response}
    """

    prompt = ChatPromptTemplate.from_template(template)
    llm = GoogleGenerativeAI(model="gemini-2.5-flash")

    return (
        RunnablePassthrough.assign(schema=lambda _: db.get_table_info())
        | prompt
        | llm
        | StrOutputParser()
    )


# if __name__ == "__main__":
#     db = init_database(SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_PORT, SQL_DATABASE)
#     sql_chain=get_sql_chain(db)
#     sql_chain = get_sql_chain(db)
#     response_chain = get_response_chain(db)
#     vars = {
#         "chat_history": "",
#         "question": "how many artists?"
#     }
#     sql_query = sql_chain.invoke(vars)
#     sql_response = db.run(sql_query)
#     answer = response_chain.invoke({**vars, "query": sql_query, "response": sql_response})
#     output = {
#         "sql_query": sql_query.strip(),
#         "answer": answer.strip()
#     }
#     print(output)
