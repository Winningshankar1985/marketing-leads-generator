import os
import json
import time
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
    max_retries=5
    for attempt in range(1, max_retries + 1):
        try:
            return prospect_finder.run(query)
        except (ConnectionError, ConnectionResetError, ConnectionAbortedError) as e:
            if attempt == max_retries:
                return f"Failed after {max_retries} retries: {str(e)}"
            wait = 2 ** attempt
            print(f"Connection error on attempt {attempt}/{max_retries}. Retrying in {wait}s...")
            time.sleep(wait)
        except Exception as e:
            if "Connection" in str(e) and attempt < max_retries:
                wait = 2 ** attempt
                print(f"Connection error on attempt {attempt}/{max_retries}. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                return f"Error finding prospects: {str(e)}"


# result= find_prospects.invoke("find career coaches in San Fransisco")

# print(f"Result: {result}")