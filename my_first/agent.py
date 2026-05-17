from google.adk.agents import Agent
from google.adk.tools import google_search

def morning_greet(name: str) -> str:
    return f"Good morning, {name}! how can I assist you today?"

def evening_greet(name: str) -> str:
    return f"Good evening, {name}! how can I assist you today?"

root_agent = Agent(
    name="my_first_agent",
    model="gemini-2.0-flash-lite",
    description="An example agent that will answer questions user queries related to google cloud",
    instruction="""
    You are AI assistant that helps users with google cloud related queries.
    """,
    tools=[google_search]   # ✅ pass the function, not string
)