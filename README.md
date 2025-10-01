# MySQL Chatbot with Google Gemini

A natural language SQL chatbot using Google Gemini that can interpret natural language queries, generate SQL queries, and fetch results from a SQL database, all in an intuitive and user-friendly way. It utilizes the power of Gemini 2.5 flash model, integrated with a Streamlit GUI for an enhanced interaction experience.

## Features
- **Natural Language Processing**: Uses Gemini 2.5 flash model to interpret and respond to user queries in natural language.
- **SQL Query Generation**: Dynamically generates SQL queries based on the user's natural language input.
- **Database Interaction**: Connects to a SQL database to retrieve query results, demonstrating practical database interaction.
- **Streamlit GUI**: Features a user-friendly interface built with Streamlit, making it easy for users of all skill levels.

## Brief Explanation of How the Chatbot Works
The chatbot works by taking a user's natural language query, converting it into a SQL query using Gemini 2.5 flash model, executing the query on a SQL database, and then presenting the results back to the user in natural language. This process involves several steps of data processing and interaction with the Google Gemini API and a SQL database, all seamlessly integrated into a Streamlit application.

## Installation
Ensure you have Python installed on your machine. Then clone this repository:

```bash
git clone [repository-link]
cd [repository-directory]
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create your own .env file with the necessary variables, including your GOOGLE GEMINI API key and SQL password:

```bash
GOOGLE_API_KEY= [your-GOOGLE-GEMINI-api-key]
SQL_PASSWORD = [SQL-Password]
```

## Usage
To launch the Streamlit app and interact with the chatbot:

```bash
streamlit run app.py
```