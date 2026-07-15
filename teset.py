import os
import sys
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Ensure standard output forces text to print immediately
sys.stdout.reconfigure(line_buffering=True)
load_dotenv()


def main():
    print("Hello from langchain-course!")

    information = """Sachin Ramesh Tendulkar born 24 April 1973) is an Indian former international cricketer..."""

    summary_template = """Given the information: {information}, about a person I want you to create:
    1. A short Summary
    2. Two interesting facts about him.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    print("DEBUG: Connecting to Local Ollama Instance...")

    # FORCED TIMEOUTS: Prevents the script from hanging forever if blocked
    llm_ollama = ChatOllama(
        model="gemma3:270m",
        temperature=0,
        timeout=10,  # Fails after 10 seconds if Ollama doesn't answer
        max_retries=0,  # Stops infinite retry loops
    )

    chain = summary_prompt_template | llm_ollama

    print("DEBUG: Triggering chain.invoke()...")
    try:
        result = chain.invoke(input={"information": information})
        print("\n--- Final Output From Model ---")
        print(result.content)
    except Exception as e:
        print(f"\n[CRASH DETECTED] Script failed with error: {e}")


if __name__ == "__main__":
    main()