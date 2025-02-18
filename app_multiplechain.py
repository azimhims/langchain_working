from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
#from langchain_core.runnables import RunnablePassthrough


load_dotenv()
#chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile') 
chatmodel = ChatGroq(model = 'llama3-70b-8192')

class Record_format(BaseModel):
    best_bolwer: str = Field(description = 'The best bowler of the Cricket Record')
    tournament: str = Field(description = 'The tournament of the Cricket Record')
json_parser = PydanticOutputParser(pydantic_object=Record_format)
output_parser = JsonOutputParser()


#prompt = PromptTemplate.from_template("tell me the best bolwer of {tournament}?", 
 #                                     partial_variables={"format_instructions": json_parser.get_format_instructions()})

prompt = PromptTemplate.from_template(
    "The best bowler of {tournament} was Hassan Ali. Please return the output in JSON format:{{'best_bowler': 'Hassan Ali', 'tournament': '{tournament}'}}",
    partial_variables={"format_instructions": json_parser.get_format_instructions()}
)

prompt2 = PromptTemplate.from_template("winning team of the {tournament}?")

chain = (prompt|chatmodel|json_parser| prompt2|chatmodel|output_parser)
result = chain.invoke({'tournament':'World Cup 1992'})

print(result)