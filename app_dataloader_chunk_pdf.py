#from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pypdf
load_dotenv()

loader = PyPDFLoader(file_path =f"E:\pro\salestaxact_1990.pdf")
data = loader.load()

splitted_data=  RecursiveCharacterTextSplitter(
    
    chunk_size = 1000, 
    chunk_overlap = 200,
    separators=["\n\n", "\n", " ", ""]
)
result = splitted_data.split_documents(data)
text_chunks = [doc.page_content for doc in result] 
configured_embedding = GoogleGenerativeAIEmbeddings(model = "models/embedding-001",task_type="retrieval_document")


try:
    embed_data = configured_embedding.embed_documents(text_chunks)
    print(len(embed_data))

    print(f"\nSample embedding (first 3 dimensions): {embed_data[0][:3]}")
    print(f"Embedding dimensions per chunk: {len(embed_data[0])}")
    
except Exception as e:
    print(f"Embedding Error: {str(e)}")


#print(f"Total chunks:{len(result)}")
#print(result[11:12])
#print("Hellow world with new line")
#print(result[12:13])



