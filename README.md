# MySQL Chatbot with Google Gemini

### Demo Video: https://www.youtube.com/watch?v=c1TsDsRsPYA

A natural language SQL chatbot powered by Google Gemini 2.5 Flash that interprets user queries, generates SQL statements, executes them on a connected SQL database, and returns results in plain English. It leverages LangChain for query orchestration, FastAPI to expose clean REST endpoints, and a Gradio-based UI for an intuitive chat experience. This seamless integration makes querying financial data simple, interactive, and user-friendly.

## Features
- Ask questions in **natural language** and get response in natural language
- Generate **SQL queries** using LangChain + Gemini 2.5 flash model
- Execute queries on **MySQL**  
- Return **formatted answers** with SQL Query  
- REST API via **FastAPI**  
- Chat UI via **Gradio** 

## Brief Explanation of How the Chatbot Works
The chatbot works by taking a user’s finance-related natural language question and converting it into a SQL query using the Gemini 2.5 Flash model through LangChain. The generated SQL is then executed on a connected MySQL finance database, retrieving accurate results. These results are processed and converted into a natural language explanation for better clarity. The system is exposed via a FastAPI backend with REST endpoints (`/ask`, `/health`) and a Gradio chat UI that displays both the SQL query and the answer in a Hugging Face–style interface. This modular design ensures a seamless integration between the LLM, database, API, and UI while keeping the workflow transparent and user friendly.

## Installation
Ensure you have Python installed on your machine. Then clone this repository:

```bash
git clone https://github.com/AlienXc137/SQL-Chatbot.git
cd SQL-Chatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create your own .env file with the necessary variables, including your GOOGLE GEMINI API key and SQL password:

```bash
GOOGLE_API_KEY= [your-GOOGLE-GEMINI-api-key]
SQL_USER=root
SQL_PASSWORD= [your-MySQL-password]
SQL_HOST=localhost
SQL_PORT=3306
SQL_DATABASE=finance_db
```

## Usage
To launch the app and interact with the chatbot:

```bash
uvicorn src.main:app
```

## Api Endpoints
API runs at : http://127.0.0.1:8000

Gradio UI runs at : http://127.0.0.1:8000/ui

Test API at SwaggerApi : http://127.0.0.1:8000/docs
