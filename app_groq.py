from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
#from langchain.core.prompts.prompt import PromptTamplate
from dotenv import load_dotenv
load_dotenv()

chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile')

message = HumanMessage(content="latest news on Artificial Intelligence")
result = chatmodel.invoke([message])
print(result.content)


#message = PromptTamplate.set_prompt("What is the capital of Pakistan?")
#result = chatmodel.invoke("What is the capital of PakistAN?")
#print(result)