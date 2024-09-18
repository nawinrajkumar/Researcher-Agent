from crewai import Crew, Process
from agent import Research_Agent, writer
from tools import search_tool
from tasks import Researcher_task, Writer_task


# Create a Crew
crew = Crew(agents=[Research_Agent, writer], 
            tools=[search_tool],
            memory=True,
            cache=True,
            verbose=True,
            max_rpm=100,
            share_crew=True)

# Create a Process
result = crew.kickoff(inputs={"topic": "What is Machine Learning and what is it's relevance in IT industry?"})
print(result)


