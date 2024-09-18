from crewai import Agent
from dotenv import load_dotenv
from tools import file_tool, search_tool, youtube_tool
import os

# Load the environment variables
load_dotenv()

os.environ['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')

# Create an agent
Research_Agent = Agent(
    role="Researcher",
    goal="To research the given document or YT video and provide a summary of the same.",
    backstory="A Top AI Research scientist specialized in providing accurate data driven insights on AI/ML through blogs, articles, and research papers.",
    tools=[file_tool, search_tool, youtube_tool],
    memory=True,
    verbose=True,
    allow_delegation=True
)

writer = Agent( 
    role="Writer",
    goal="To write articles, blogs, and research papers.",
    backstory="Specialized in writing articles, blogs, and research papers.",
    tools=[file_tool],
    verbose=True
)
