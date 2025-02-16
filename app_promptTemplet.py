# there are multiple type of chain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile')

prompt = PromptTemplate.from_template("give me joke about {contents}")
#promptTemplete is a string so there is no need to fstirng in above prompt.
formated_prompt = prompt.format(contents="dog")
print(prompt)
result = chatmodel.invoke([formated_prompt])
print(result.content)