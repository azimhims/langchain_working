from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile')


prompt = PromptTemplate.from_template("give me joke about {contents}")
out_put_parser = StrOutputParser()
chain = prompt|chatmodel|out_put_parser
result = chain.invoke({'contents':'Generative AI'})
print(result)