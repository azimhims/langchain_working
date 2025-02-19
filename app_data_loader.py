from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader



load_dotenv()

loader = CSVLoader(file_path=f"2FNofFeb202518022025.csv")
data = loader.load()
print(data)