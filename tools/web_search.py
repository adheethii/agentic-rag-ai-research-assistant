from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query):

    response = client.search(query=query)

    return response["results"]