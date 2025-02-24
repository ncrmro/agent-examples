import os
import sqlite3

from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langgraph.prebuilt import create_react_agent

DATA_DIR = "data"
DB_FILE = os.path.join(DATA_DIR, "sqlite3.db")


def get_engine_for_db():
    """Pull sql file, populate in-memory database, and create engine."""
    """Create or load SQLite database from the data directory."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if os.path.exists(DB_FILE):
        # Load existing database
        connection = sqlite3.connect(DB_FILE, check_same_thread=False)
    else:
        # Create new database and define the user_notes table
        connection = sqlite3.connect(DB_FILE, check_same_thread=False)
        create_table_sql = """
        CREATE TABLE user_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category STRING NOT NULL,
            key STRING,
            value STRING NOT NULL,
            created INT,
            updated INT
        );
        """
        connection.execute(create_table_sql)

    return create_engine(
        f"sqlite:///{DB_FILE}",
        creator=lambda: connection,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )


engine = get_engine_for_db()

db = SQLDatabase(engine)

llm = init_chat_model("gpt-4o-mini", model_provider="openai")

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

prompt_template = PromptTemplate.from_template("""You are an agent designed to collect imformation about a user and store it in the user_notes table inside of a SQL database.
Store any information the user provides.
The category column should use the following values only (profile, relationship, goal), not all rows will have a key.
A row with a category of profile may have a key birthday and value would be the users birthday, one with relationship might have a key of mother, sister, partner etc.
Never store more than one value in the values column use multiple rows.
Store and retreive data using syntactically correct {dialect} query to run and return.
You have access to tools for interacting with the database.
Only use the below tools. Only use the information returned by the below tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any of the following statements (DELETE, DROP) to the database.
""")

system_message = prompt_template.format(dialect="SQLite")

memory = MemorySaver()
agent_executor = create_react_agent(
    llm, toolkit.get_tools(), prompt=system_message, checkpointer=memory
)
config = {"configurable": {"thread_id": "abc123"}}
print(
    "Bot: Hello! I am a chatbot. I can help you with anything you want to talk about."
)
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    for step in agent_executor.stream(
        {"messages": [HumanMessage(content=user_input)]},
        config,
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()
    #     m = step["messages"][-1]
    #     if m.type == "ai":
    #         if m.content == "":
    #             print("...")
    #         else:
    #             print(f"Agent: {step['messages'][-1].content}")
    # # print(f"Agent: {step['messages'][-1]}")
