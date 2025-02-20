from langchain_groq import ChatGroq
from dotenv import load_dotenv
import bs4
from langchain_community.document_loaders import TextLoader #WebBaseLoader

load_dotenv()


#loader = WebBaseLoader("https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q=smart%20phone")

loader = TextLoader('E:\pro\data.txt')



data = loader.load()
print(data)