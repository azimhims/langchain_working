import requests
from bs4 import BeautifulSoup
from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
# Initialize LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# --------------------------
# Scrapers for Different Sites
# --------------------------
#https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q=smart%20phone

def scrape_daraz(model_name):
    """Scrape Daraz.pk for a specific phone model."""
    url = f"https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q={model_name.replace(' ', '%20')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract data (update selectors based on Daraz's current HTML)
        product = {
            "website": "Daraz.pk",
            "price": soup.select_one(".price").text.strip() if soup.select_one(".price") else "N/A",
            "warranty": soup.select_one(".warranty-text").text.strip() if soup.select_one(".warranty-text") else "N/A",
            "Specifications": soup.select_one(".spec-list").text.strip() if soup.select_one(".spec-list") else "N/A",
            "reviews": [review.text.strip() for review in soup.select(".review-content")],
        }
        return product
    except Exception as e:
        print(f"Failed to scrape Daraz: {e}")
        return None

def scrape_priceoye(model_name):
    """Scrape PriceOye.pk for a specific phone model."""
    url = f"https://priceoye.pk/search?q={model_name.replace(' ', '+')}"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract data (update selectors for PriceOye)
        product = {
            "website": "PriceOye.pk",
            "price": soup.select_one(".price-box").text.strip() if soup.select_one(".price-box") else "N/A",
            "warranty": soup.select_one(".warranty-text").text.strip() if soup.select_one(".warranty-text") else "N/A",
            "Specifications": soup.select_one(".spec-list").text.strip() if soup.select_one(".spec-list") else "N/A",
            "reviews": [review.text.strip() for review in soup.select(".rating-reviews")],
        }
        return product
    except Exception as e:
        print(f"Failed to scrape PriceOye: {e}")
        return None

# Add more scrapers (e.g., Homeshopping.pk, Mobiles4U) here.
# --------------------------
# Comparison Logic
# --------------------------

def compare_models(model_list):
    """Compare multiple models across all websites."""
    all_data = []
    
    for model in model_list:
        model_data = {"model": model, "sites": []}
        
        # Scrape data from all websites for this model
        daraz_data = scrape_daraz(model)
        priceoye_data = scrape_priceoye(model)
        
        # Add valid results to the dataset
        if daraz_data:
            model_data["sites"].append(daraz_data)
        if priceoye_data:
            model_data["sites"].append(priceoye_data)
        
        all_data.append(model_data)
    
    return generate_comparison_table(all_data)

def generate_comparison_table(data):
    """Use LLM to create a structured comparison table."""
    prompt_template = ChatPromptTemplate.from_template(
        """
        Compare smartphones across Pakistani e-commerce sites. Use this data:
        {data}
        
        Generate a Markdown table with columns: Model, Website, Price, Warranty, Reviews Summary.
        Highlight the best price for each model.
        """
    )
    chain = prompt_template | llm
    return chain.invoke({"data": data})

# Example: Streamlit UI
import streamlit as st

st.title("🇵🇰 Pakistan Smartphone Comparison")
models = st.text_input("Enter models (comma-separated):", "Infinix Note 7, Samsung A04")

if st.button("Compare"):
    model_list = [m.strip() for m in models.split(",")]
    result = compare_models(model_list)
    st.markdown(result.content)