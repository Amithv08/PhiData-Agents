from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv


load_dotenv()     # I have deleted the env file, as code is on public, add OPENAPIKEY AND GROQ API KEY on local.

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile")
)


agent.print_response("write 5 lines poem on Lord Shiva")