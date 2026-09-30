import os
from dotenv import load_dotenv, find_dotenv
from tools.places_search_tool import find_prospects
from tools.file_ops import (
    create_file,
    read_file
)
load_dotenv(find_dotenv())
model=os.environ.get("model_pro")
prompt="You are helpful 15 years experienced 'lead generation expert'. Who generates accurate and verifiable leads for the user with googleplaces api tool in 'find_prospects'. once done you have to write those leads in a file."




find_prospect_agent={
    "name": "lead-generation-agent",
    "description": "Use this to find business's, people or organization professional & contact details",
    "tools": [find_prospects,create_file,read_file],
    "model": model,
    "system_prompt": prompt
}