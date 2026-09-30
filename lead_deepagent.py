import os
import json
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from langchain_deepseek import ChatDeepSeek
from deepagents import create_deep_agent
from sub_agents.lead_generation_sub_agent import find_prospect_agent 

load_dotenv(find_dotenv())

prompt=str(input("Please mention a location and the domain to look Leads for: "))

messages={"messages":[{"role":"user","content": prompt}]}

model=os.environ.get("model_pro")
api_key=os.environ.get("DEEPSEEK_API_KEY")
sys_prompt="""You are a senior it consulting lead gen expert.
Context: I run a IT Consulting business and need help with lead generation.
Task: Generate a high-converting lead gen output tailored to my audience.
Output: convert the response to a file and store it.
"""

llm=ChatDeepSeek(
model=model,
api_key=api_key,
temperature=0.3,
max_retries=5,
)

_agent=create_deep_agent(
    model=llm,
    subagents=[find_prospect_agent],
    system_prompt=sys_prompt
)

try:
    print(f"Agent has started looking for leads:\n")
    output=_agent.invoke(messages)
   
 
    print(f"Done\n")
      
except Exception as e:

    print(f"The agent failed to execute,\n\n Message:\n {str(e)}")