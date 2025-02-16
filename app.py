# using langchain create simple chatbot with chain features avaliable
#from langchain import LangChain



from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = GoogleGenerativeAI(model= "gemini-2.0-flash")

result = chatmodel.invoke("what is squre root of 625 and then multple by 2")

print(result)
