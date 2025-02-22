import requests
import base64
from typing import Optional

# Import things that are needed generically
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from pprint import pprint


# @tool
def get_repo_content(owner: str, repo: str, filepath: Optional[str] = "") -> str | list:
    """Return contents of a file or a list of files if filepath is a directory in a git directory. If no filepath is provided use /"""
    url = f"http://gitea:3000/api/v1/repos/{owner}/{repo}/contents/{filepath}"
    headers = {
        "accept": "application/json",
        "Authorization": "token 87282d54cd23a690e80f658e9043416f637ad469",
    }

    response = requests.get(url, headers=headers)
    d = response.json()
    if type(d) is list:
        return [i["name"] for i in d]
    # Decode the base64-encoded content
    decoded_bytes = base64.b64decode(d["content"])

    # Convert bytes to a string (assuming the content is UTF-8 encoded)
    decoded_string = decoded_bytes.decode("utf-8")
    return decoded_string


llm = ChatOpenAI(model="gpt-4o-mini")

tools = [get_repo_content]
prompt = (
    "You are a helpful assistant that has access to a Git repos via a Git API. "
    "You may not need to use tools for every query - the user may just want to chat!"
)

# with this prompt string before any other messages sent to the model
agent = create_react_agent(llm, tools, prompt=prompt)


res = agent.invoke(
    {"messages": [HumanMessage(content="What is the contents of admin/dotfiles")]}
)

for m in res["messages"]:
    pprint(m)

for m in res["messages"]:
    if m.content != "":
        pprint(m.content)

# Call the function with the example URL and the README.md file
# c = get_repo_content(
#     "admin",
#     "Test",
#     #    "README.md",
# )
#
# print(c)
