from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.prompts import HumanMessagePromptTemplate


load_dotenv()
chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile')
general_message = ChatPromptTemplate.from_messages([
    ("system","You act like a news anchor and economist  "),
    ("human","tell me latest news of  {userinput} economy ")
    
]

)
input_prompted = general_message.format_messages(userinput="Pakistan")
result = chatmodel.invoke(input_prompted)
print(result.content)
