#=========================================================================================================================
# new working with history message
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


model = ChatGroq(model= 'llama-3.3-70b-versatile')

message_record = [SystemMessage(content="You act like Cricket Expert"),HumanMessage(content="tell me latest news on Cricket")]

result = model.invoke(message_record)

# after passes the list in message, now there is no need to pass list in invoke method, only pass variable message
message_record.append(HumanMessage(content="who is the best cricketer in the world?"))

result_record = model.invoke(message_record)
print(result.content)
print(result_record.content)