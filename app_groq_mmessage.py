from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


model = ChatGroq(model= 'llama-3.3-70b-versatile')

message = [SystemMessage(content="You act like Cricket Expert"),HumanMessage(content="tell me latest news on Cricket")]

# after passes the list in message, now there is no need to pass list in invoke method, only pass variable message


result = model.invoke(message)
print(result.content)
