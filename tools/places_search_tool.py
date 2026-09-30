import os
import json
from dotenv import load_dotenv, find_dotenv
from langchain_google_community import GooglePlacesAPIWrapper, GooglePlacesTool
from langchain.tools import tool

load_dotenv(find_dotenv())

api=os.environ.get("map_demo_key")
wrapper=GooglePlacesAPIWrapper(gplaces_api_key=api)
prospect_finder=GooglePlacesTool(api_wrapper=wrapper)

@tool
def find_prospects(query:str)->dict[list]:
    """
    get the search results of user query from GooglePlacesTool

    ARGS:
    query: a small description on what to find...

    """
 
    
    return prospect_finder.run(query)


# result= find_prospects.invoke("find career coaches in San Fransisco")

# print(f"Result: {result}")