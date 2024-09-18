from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Set the environment variables
os.environ['SCRAPER_API_KEY'] = os.getenv('SCRAPER_API_KEY')

# Create a search tool
search_tool = SerperDevTool()
