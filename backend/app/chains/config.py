import requests

from langchain_core.documents import Document
import os
# pretty print
from pprint import pprint
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

def environtmental_variables():
    # os already imported at top
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    print("My Api keys loading...")
    # print(GOOGLE_API_KEY, OPENAI_API_KEY, GROQ_API_KEY)

# load google llm
def load_google_llm():
    from langchain_google_genai import GoogleGenerativeAI
    # loading our keys
    environtmental_variables()
    google_llm=GoogleGenerativeAI(
        # pass our configurations here
        model="gemini-2.5-flash",
        temperature=0.9
    )
    return google_llm

def load_google_chat_model():

    from langchain_google_genai import ChatGoogleGenerativeAI
    environtmental_variables()
    google_chat_model=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )
    return google_chat_model


# LOAD WEATHER DATA VIA AN API


# Add this to your existing config.py file
def load_google_multimodal_chat():
    """Load Google chat model with image support"""
    from langchain_google_genai import ChatGoogleGenerativeAI
    environtmental_variables()
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.9
    )
# class WeatherAPILoader:
#     def __init__(self, city: str, api_key: str):
#         self.city = city
#         self.api_key = api_key
    
#     def load(self):
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
#         response = requests.get(url).json()
#         print("DATA PRINTED IN A WELL FORMATTED WAY - > ")
#         pprint(response)
        
#         # Extract relevant info
#         content = (
           
#             f"Weather in {self.city}: {response['weather'][0]['description']}. "
#             f"Temperature: {response['main']['temp']}°C, "
#             f"Humidity: {response['main']['humidity']}%."
#         )
        
#         # Wrap into LangChain Document
#         return [Document(page_content=content, metadata={"source": "OpenWeatherAPI"})]

# # Usage

# if __name__ == "__main__":
#     environtmental_variables()
#     loader = WeatherAPILoader(city="bamenda", api_key=os.getenv("WEATHER_API_KEY"))
#     docs = loader.load()
#     print(docs[0].page_content)
#     print(docs[0].metadata)





# CONFIGURE OUR WEATHER API ENDPOINT HERE
# OR WE GOING TO MAKE A REQUEST TO THE WEATHER API HERE

class WeatherAPILoader:
    # create a constructor function
    def __init__(self, city, api_key):
        # initialize our properties
        self.city=city
        self.api_key=api_key
    # CREATE A METHOD THAT LOADS THE DATA (LIVE)
    def load(self):
        # we need pass information to our url, like the city and the 
        # api key
        url=f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metrics"
        
        # make a request and store it to ou response 
        # json==dictionary in python
        response=requests.get(url).json()
        return response


# Write a function that can be used any where in our app
def weatherContext(city):
    # initialize or create an instant of our class
    environtmental_variables()
    weatherData=WeatherAPILoader(city=city, api_key=os.getenv("WEATHER_API_KEY"))

    response=weatherData.load()
    return response
    
# print(f"fetched data: {fechedData}")

def load_embeddings():
    environtmental_variables()
    embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    # print("embeddings", embeddings)
        # Test with some sample text
        # Embeddings work by converting text into numerical vectors that capture meaning
    sample_texts = [
            "The weather is beautiful today.",
            "It's a sunny and pleasant day outside.",
            "I love programming in Python.",
            "Machine learning is fascinating."
        ]
        
    print("Generating embeddings for sample texts...")
    print("-" * 50)
        
        
    embedded_docs = embeddings.embed_documents(sample_texts)
    print(embedded_docs)
    return embeddings
    

# load_embeddings()