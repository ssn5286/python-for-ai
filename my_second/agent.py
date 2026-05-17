from google.adk.agents import Agent
from google.adk.tools import google_search

def morning_greet(name: str) -> str:
    return f"Good morning, {name}! how can I assist you today?"

def evening_greet(name: str) -> str:
    return f"Good evening, {name}! how can I assist you today?"

root_agent = Agent(
    name="my_first_agent",
    model="gemini-2.5-flash",
    description="An example agent that will answer questions user queries based on google search",
    instruction="""
    First Ask User a Name & Start conversation by greeting based on users Greet.
    If user says good morning, use morning_greet tool to greet user.
    If user says good evening, use evening_greet tool to greet user.
    """,
    tools=[morning_greet,evening_greet] ,  # ✅ pass the function, not string
)