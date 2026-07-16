from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """ Schema for the source used by the agent"""
    url: str =Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """ Schema for the  response from the agent with answer"""
    answer: str = Field(description="The Agents answer to the query")
    sources: List[Source] = Field(default_factory =list,description="List of sources used to generate the answer")

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools =[TavilySearch()]
agent = create_agent(model=llm_gemini, tools=tools,response_format=AgentResponse)

def main():
    print("Hello from langchain-course!") 
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="provide top 3 job postings for AI data engineer in the Hyderabad Location"
                )
        }
    )
    print(result)


if __name__ == "__main__":
    main()