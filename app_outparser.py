from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator 
#from langchain_core.messages import HumanMessage, SystemMessage  


load_dotenv()

chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile')

class Record(BaseModel):
    setup: str = Field(description = 'The setup of the Cricket Record')
    PlayerName: str = Field(description = 'The Player Name of the Cricket Record')
    Records: str = Field(description = 'The Records of the Cricket Record')

parser = PydanticOutputParser(pydantic_object=Record)

prompt = PromptTemplate.from_template("tell me the cricket record of {PlayerName}")

prompt_model = prompt|chatmodel
output = prompt_model.invoke({'PlayerName':'Imran Khan'})
parser.invoke(output)
