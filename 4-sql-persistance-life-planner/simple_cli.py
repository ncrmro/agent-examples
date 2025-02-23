from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage

model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}

print(
    "Bot: Hello! I am a chatbot. I can help you with anything you want to talk about."
)
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    input_messages = [HumanMessage(user_input)]
    output = app.invoke({"messages": input_messages}, config)
    print(f"Agent: {output['messages'][-1].content}")
