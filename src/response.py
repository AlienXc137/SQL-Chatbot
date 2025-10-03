from langchain_core.messages import AIMessage, HumanMessage
from .chains import get_sql_chain, get_response_chain
from .models import QueryRequest, QueryResponse

class SQLChatbot:
    def __init__(self, db):
        self.db = db
        self.chat_history = [
            AIMessage(content="Hello! I'm your SQL assistant. Ask me anything related to the database.")
        ]
        self.sql_chain = get_sql_chain(db)
        self.response_chain = get_response_chain(db)

    def ask(self, question: str) -> QueryResponse:
        self.chat_history.append(HumanMessage(content=question))
        vars = {
            "chat_history": self.chat_history,
            "question": question
        }
        db=self.db
        sql_query = self.sql_chain.invoke(vars)
        sql_response = db.run(sql_query)
        answer = self.response_chain.invoke({**vars, "query": sql_query, "response": sql_response})
        self.chat_history.append(AIMessage(content=answer))
        output = QueryResponse(
            SQLquery= sql_query.strip(),
            answer= answer.strip()
        )
        return output
