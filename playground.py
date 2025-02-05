from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.agent import Agent
from dotenv import load_dotenv
from streamlit import markdown

load_dotenv()


web_search_agent = Agent(
    name = "Web search agent",
    role = "search web for information",
    model = OpenAIChat(id="gpt-4o"),
    tools = [DuckDuckGo()],
    instructions = ['Always include sources'],
    show_tool_calls = True,
    markdown = True,
)

finance_agent = Agent(
    name = "Finance AI Agent",
    model = OpenAIChat(id="gpt-4o"),
    tools = [YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        company_news=True,
        key_financial_ratios=True
    )],
    instructions = ['Use tables to display the data'],
    show_tool_calls = True,
    markdown=True,
)

app = Playground(agents=[web_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)

