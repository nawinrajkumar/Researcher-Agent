from crewai import Task
from agent import Research_Agent, writer
from tools import search_tool

Researcher_task = Task(
    description="Find news articles, blogs or research papers based on the topic {topic} and summarize them. The articles should contain facts and data points.",
    expected_output="A summary of the news articles, blogs or research papers based on the topic {topic}. Should contain facts and data points.",
    agent=Research_Agent,
    tools=[search_tool]
)

Writer_task = Task(
    description="Write an article based on the summary provided by the Researcher on the topic {topic}. The article should be well structured and informative.",
    expected_output="An article on the topic {topic} based on the summary provided by the Researcher. The article should be well structured and informative.",
    agent=writer,
    async_execution=False,
    tools=[search_tool]
)