from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat
from streamlit import markdown

load_dotenv()

def get_company_Symbol(company: str) -> str:

    """Use this function to get the symbol for a company.


    Args:
        company(str): The name of the company.


    Returns:
        str: The symbol for the company
    """

    symbols = {
        "phidata" : "MSFT",
        "Infosys" : "INFY",
        "Tesla" : "TSLA",
        "Apple" : "AAPL",
        "Microsoft" : "MSFT",
        "Amazon" : "AMZN",
        "Google" : "GOOGL"
    }

    return symbols.get(company, "Unknown")

    




agent = Agent(
    model = OpenAIChat(id="gpt-4o"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_Symbol],
    show_tool_calls = True,
    markdown=True,
    instructions  = ['use tables to display the data', 'If you do not know the company symbol, please use get_company_symbol tool'],
    debug_mode = True,
)


agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA AND Apple")

