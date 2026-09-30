import os
import json
import time
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

max_retries=3
for attempt in range(1, max_retries + 1):
    try:
        print(f"Agent has started looking for leads:\n")
        output=_agent.invoke(messages)
        print(f"Done\n")
        break
    except Exception as e:
        error_msg=str(e)
        if ("Connection" in error_msg or "reset" in error_msg.lower()) and attempt < max_retries:
            wait = 10 * attempt
            print(f"\nConnection error on attempt {attempt}/{max_retries}. Retrying in {wait}s...\n")
            time.sleep(wait)
        else:
            print(f"The agent failed to execute,\n\n Message:\n {error_msg}")
            break