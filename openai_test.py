import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 1. Load your .env file containing OPENAI_API_KEY
load_dotenv()


def main():
    print("Hello from langchain-course######!")
    print(f"DEBUG: API Key Loaded -> {os.getenv('GOOGLE_API_KEY')[:10]}...")

    # 2. Put all your variables inside the main execution block
    information = """Sachin Ramesh Tendulkar  born 24 April 1973) is an Indian former international cricketer who captained the Indian national team. Tendulkar is widely regarded as one of the greatest cricketers in the history of cricket.[5] He holds several world records, including being the all-time highest run-scorer in international cricket,[6] receiving the most player of the match awards in international cricket,[7] and being the only batsman to score 100 international centuries.[8] Tendulkar was a Member of Parliament, Rajya Sabha by presidential nomination from 2012 to 2018.[9][10]

    Tendulkar took up cricket at the age of eleven, made his Test match debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for over 24 years.[11] In 2002, halfway through his career, Wisden ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards.[12] The same year, Tendulkar was a part of the team that was one of the joint-winners of the 2002 ICC Champions Trophy. Later in his career, Tendulkar was part of the Indian team that won the 2011 Cricket World Cup, his first win in six World Cup appearances for India.[13] He had previously been named "Player of the Tournament" at the 2003 World Cup.
    """

    summary_template = """Given the information: {information}, about a person I want you to create:
    1. A short Summary
    2. Two interesting facts about him.
    """

    # 3. Initialize your Prompt Template properly (Note lowercase 'input_variables')
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # 4. Set up your Chat model 
    llm_openai = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # 5. Build the LangChain Expression Language (LCEL) chain
    chain = summary_prompt_template | llm_openai

    # 6. Invoke the chain and print out the content
    print("\n--- Sending request to OpenAI ---")
    result = chain.invoke(input={"information": information})
    print(result.content)


if __name__ == "__main__":
    main()