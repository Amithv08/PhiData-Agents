from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.wikipedia import WikipediaTools
from phi.tools.googlesearch import GoogleSearch
from streamlit import markdown
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app
from streamlit import markdown


load_dotenv()
agent = Agent(
    model = OpenAIChat(id="gpt-4o"),
    tools = [GoogleSearch(), DuckDuckGo(), WikipediaTools()],
    markdown=True,
    show_tool_calls=True,
)



agent.print_response("Please explain about the picture in 5 lines",



images = ["https://st1.uvnimg.com/fb/da/2ee413844aa6b65c8eac16670756/cristiano-ronaldo.jpg"],
                     stream=True)


