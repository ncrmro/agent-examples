from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


model = init_chat_model("gpt-4o", model_provider="openai")


prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me a joke about {topic}")
])

prompt_template.invoke({"topic": "cats"})
r = model.invoke([HumanMessage(content="Hi! I'm Bob")])
print(r)
