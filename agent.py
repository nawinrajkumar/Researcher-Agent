from crewai import Agent
from dotenv import load_dotenv
from tools import search_tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load the environment variables
load_dotenv()

## call the gemini models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GEMINI_API_KEY"))


researcher_backstory = """A Top AI Research scientist specialized in providing 
accurate data driven insights on AI/ML through blogs, articles, and research 
papers."""

researcher_goal = """Research on web on the topic and provide a summary of
results.""" 

writer_goal = """Write an article based on the summary 
provided by the Researcher"""

writer_backstory = """Experienced writer with a background in 
writing blogs and articles. Specialized in writing on AI/ML topics.
All the articles are well known for structured data and facts."""

# Create a Researcher Agent
Research_Agent = Agent(role="Researcher",
                       goal=researcher_goal,
                       backstory=researcher_backstory,
                       tools=[search_tool],
                       memory=True,
                       verbose=True,
                       llm=llm,
                       allow_delegation=True)

# Create a Writer Agent
writer = Agent(role="Writer",
               goal=writer_goal,
               backstory=writer_backstory,
               tools=[search_tool],
               verbose=True,
               llm=llm,
               allow_delegation=False)
