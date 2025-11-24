from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq


load_dotenv()


# seleccionar modelo gratis
llm = ChatGroq(model="llama-3.1-8b-instant")  # rápido, gratis y bueno

response = llm.invoke("Cual es el sentido de la vida?")
print(response)