import os
from pathlib import Path
import json
from langchain.tools import tool
from datetime import datetime


parent_workspace=Path("/Users/apple/Documents/lead_agents")
leads_folder=parent_workspace/"leads-generated"

if not leads_folder.exists():
    leads_folder.mkdir(parents=True,exist_ok=True)
    print(f"leads folder generated for the first time")
elif leads_folder.exists():
    print(f"Path: {leads_folder} already exists")


@tool
def create_file(query:str,content:str)->str:
    """
    create a generated leads leads file to check after generation.
    ARGS:
    query: query asked by user to generate leads.
    content: generated leads from places_search_tool to be written to the file. 
    """
    if not query:
        return f"query is important to identify what the requirement was for generated leads." 
    elif not content:
        return f"content is important to populate in the file."
    else: 
        print("great we have received Leads to generate a file")

    date_time=datetime.isoformat(datetime.now())
    new_folder=leads_folder/f"leads-{date_time}"
    file_name=f"leads-file-{date_time}"
    new_file=new_folder/f"{file_name}.txt"

    new_folder.mkdir(parents=True,exist_ok=True)    
    with open(new_file,"w") as f:
        contents=(
            f"User Query: {query}\n"
            f"LEADS GENERATED - \n"
            f"{content}\n"
            f"----- Fin -----"
        )
        output=f.write(contents)
    return f"file has been created in path: '{new_file}' with the writing output code: {output}"

@tool
def read_file(path:str)->str:
    """
    Read the file and return its content.
    ARGS:
    path: path to the file where it exists so the tool can read.
    """
    if not path.startswith("/leads-generated"):
        return f"file not matching path: /{path}"
    full_path=f"{parent_workspace}{path}"
    print(f"FULL PATH: {full_path}")
    file=Path(full_path)
    if not file.exists():
        return f"file path: {file} doesn't exist. Please send a path that exists."
    else:
        with open(file,"r") as f:
            content=f.read()

    return (
        f"Content Read from File in path: '{file}'\n\n\n"
        f"{content}"
        )








# print(create_file.invoke({"query":"find schools near me?\n\n\n\n","content": "Avinashi School:\n\nPrincipal: Sadayandi M.BA\nAddress: Avinashi Road, coimbatore.\nwebsite: www.avschool.com\ncontact: +91-9952132604\n"}))

# print(read_file.invoke({"path": "/leads-generated/leads-2026-06-24T13:35:55.602863/leads-file-2026-06-24T13:35:55.602863.txt"}))