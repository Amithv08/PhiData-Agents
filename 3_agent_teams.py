from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import  Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from streamlit import markdown

load_dotenv()


web_agent = Agent(
    name = "Web Agent",
    role = 'Searching the web',
    model = OpenAIChat(id="gpt-4o"),
    #model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ['Always include sources'],
    show_tool_calls = True,
    markdown = True
)

finance_agent = Agent(
    name = "Finanace Agent",
    role = "Get Financial data",
    model = OpenAIChat(id = "gpt-4o"),
    #model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=['use tables to display the data'],

)

agent_team = Agent(
    team = [web_agent, finance_agent],
    model = OpenAIChat(id = "gpt-4o"),
    instructions = ['Always include sources', 'use tables to display data'],
    show_tool_calls = True,
    markdown=True
)



agent_team.print_response("Summarize the analyst recommendations and share the latest news for NVDA", stream=True)