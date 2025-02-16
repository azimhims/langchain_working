#from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_vertexai import VertexAIEmbeddings
#from langchain_embedding import EmbeddingModel
from dotenv import load_dotenv

load_dotenv()
#llm = EmbeddingModel(model = "gemini-2.0-flash",)
#GoogleGenerativeAI(llm=llm,)

embeddings_model = VertexAIEmbeddings(model= "text-embedding-004")
#result = embedding.embed_query("Delhi is capital of India")

#print(str(result))

embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
embedded_query[:5]