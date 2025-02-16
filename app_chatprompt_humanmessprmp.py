from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import HumanMessagePromptTemplate , ChatPromptTemplate

from langchain_core.messages import SystemMessage

load_dotenv()
chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile')


message_tampletes = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are content creater"),
        HumanMessagePromptTemplate.from_template("please create a content for facebook for {userinput} Fashions apeal to the youth" )
    ]
    )
#message = message_tampletes.format_messages(userinput='ZOBAS')
#result = chatmodel.invoke(message)
#print(result.content)



result = message_tampletes.invoke({'userinput':'ZOBAS'})
#print(result.to_messages())
print(result.to_string())

