from crewai_tools import FileReadTool, SerperDevTool, WebsiteSearchTool

file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()