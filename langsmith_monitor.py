
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API keys and LangSmith settings
load_dotenv()

# Create the language model
llm = ChatOpenAI(model="gpt-4o-mini")

# Three prompts for the assignment
prompts = [
    "Explain LangChain in two sentences.",
    "Explain LangSmith tracing in three bullet points.",
    "Explain how a RAG application retrieves information and generates an answer, using a simple example."
]

# Send all three prompts and print the answers
for i, prompt in enumerate(prompts, start=1):
    print(f"\n--- Run {i} ---")
    print(f"Prompt: {prompt}")

    response = llm.invoke(prompt)

    print(f"Answer: {response.content}")
