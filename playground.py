from phi.agent import Agent
import phi.api
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
from phi.playground import Playground, serve_playground_app
from phi.model.groq import Groq

load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

websearch_agent = Agent(
    name="Web Search Agent",
    role="A web search agent that can find information on the internet about stock data.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source of the information you find."],
    show_tools_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    role="A finance agent that can give historical information about stock data.",
    tools=[
        YFinanceTools(
            stock_price=True, 
            analyst_recommendations=True, 
            stock_fundamentals=True, 
            company_news=True
        ),
    ],
    instructions=["Use tables to display stock data."],
    show_tools_calls=True,
    markdown=True,
)

app = Playground(agents=[websearch_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)