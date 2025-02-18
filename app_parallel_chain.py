from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel 


load_dotenv()
chatmodel = ChatGroq(model = 'llama3-70b-8192')

best_bowler_prompt = PromptTemplate.from_template("Who was best bowler  in {tournament}?, Respond just name")
top_score_prompt = PromptTemplate.from_template("Who was top run score  in {tournament}?, Respond just name")
winnig_team_prompt = PromptTemplate.from_template("Who was winnig team in {tournament}?, Respond just name")
host_country_prompt = PromptTemplate.from_template("What was the host country of {tournament}?, Respond just name")

parallel_chain = RunnableParallel({'best_bowler': best_bowler_prompt|chatmodel|StrOutputParser(),
    'top_score':top_score_prompt|chatmodel|StrOutputParser(),
    'winning_team':winnig_team_prompt|chatmodel|StrOutputParser(),
    'host_country':host_country_prompt|chatmodel|StrOutputParser()}
)

result = parallel_chain.invoke({'tournament':'Cricket World Cup 1996'})
print(result)