from dotenv import load_dotenv


load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """Search the web for current weather details about a specific city."""
    print(f"Searching for: {query}")
    return f"Vijayawada weather is Sunny"

@tool
def search_tavely(query: str) -> str:
    """Search the web for current weather details about a specific city."""
    print(f"Searching for: {query}")
    return tavily.search(query=query, search_depth="advanced")

#llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
#llm_olama = ChatOllama(model="llama3.2", temperature=0)
llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

tools =[search_tavely]
#tools =[search]
agent = create_agent(model=llm_gemini, tools=tools)

def main():
    print("Hello from langchain-course!") 
    #result = agent.invoke({"messages": [HumanMessage(content="provide the weather details for vijayawada city")]})   
    #Real world search using tavily
    result = agent.invoke({"messages": [HumanMessage(content="provide top 3 job offers for AI data engineer")]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
