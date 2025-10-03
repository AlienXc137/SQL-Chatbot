import gradio as gr
from fastapi import FastAPI, HTTPException
from .config import SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_PORT, SQL_DATABASE
from .database import init_database
from .response import SQLChatbot
from .models import QueryRequest, QueryResponse

app = FastAPI(title="SQLGenie - Finance SQL Assistant")


db = init_database(SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_PORT, SQL_DATABASE)
chatbot = SQLChatbot(db)


#Endpoints
@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/ask", response_model=QueryResponse)
async def ask_question(req: QueryRequest):
    try:
        result = chatbot.ask(req.question)
        return QueryResponse(SQLquery=result.SQLquery, answer=result.answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#Gradio UI
def chat_with_sqlgenie(message, history):
    result = chatbot.ask(message)
    return f"### SQL Query:\n```sql\n{result.SQLquery}\n```\n### Answer:\n{result.answer}"


# theme
theme = gr.themes.Soft(
    primary_hue="indigo",
    secondary_hue="blue"
).set(
    body_background_fill="linear-gradient(135deg, #f9fafb, #e0f2fe)",
    block_title_text_color="#4f46e5",  # Indigo title
    button_primary_background_fill="linear-gradient(90deg, #4f46e5, #3b82f6)",
    button_primary_text_color="white",
)

# Custom CSS for Hugging Face–like chat bubbles
custom_css = """
#component-0 {color: #4f46e5 !important;} /* Title color override */
.svelte-1ipelgc.user {background-color: #e0f2fe !important; color: #1e40af !important; border-radius: 12px; padding: 8px;}
.svelte-1ipelgc.assistant {background-color: #ede9fe !important; color: #4f46e5 !important; border-radius: 12px; padding: 8px;}
"""

demo = gr.ChatInterface(
    fn=chat_with_sqlgenie,
    title="SQLGenie - Finance SQL Assistant",
    description="Ask finance-related questions in plain English. Get SQL + answers.",
    theme= theme,#'NoCrypt/miku'
    css=custom_css,
)

# Mount Gradio on FastAPI at /ui
app = gr.mount_gradio_app(app, demo, path="/ui")


