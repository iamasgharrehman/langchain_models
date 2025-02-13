from langchain_openai import openai
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result= llm.invoke('What is the capital of Pakistan')

print(result)