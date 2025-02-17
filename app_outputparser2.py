from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import pandas as pd

load_dotenv()
chatmodel = ChatGroq(model = 'llama-3.3-70b-versatile') 

class Record_format(BaseModel):
    PlayerName: str = Field(description = 'The Player Name of the Cricket Record')
    PlayerAverage: int = Field(description = 'The Player Age of the Cricket Record')
    PlayerCountry: str = Field(description = 'The Player Country of the Cricket Record')
    PlayerRecord: str = Field(description = 'The Player Record of the Cricket Record')
    
parser = PydanticOutputParser(pydantic_object=Record_format)

prompt = PromptTemplate.from_template("tell me the cricket record of {PlayerName}")

model_promp = prompt|chatmodel
result = model_promp.invoke({'PlayerName':'Inzamam-ul-Haq'})
crick_data = parser.invoke(result)
data_dict = crick_data.dict()
df = pd.DataFrame([data_dict])
print(df)