from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate #PromptTemplate

load_dotenv()
chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile')
#ChatPromptTemplate list of message means use [] brackets to pass the list of message

prompted = ChatPromptTemplate([("system","You act like a news anchor of film industry"),
                               ("human","tell me latest news of Actor {userinput}"),
                               ("ai","thanks for contact us"),
                               ("human","Thanks for help")
                               ])
input_prompted = prompted.format_messages(userinput="Salman Khan")
result = chatmodel.invoke(input_prompted)
print(result.content)