from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()

websearch_agent = Agent(
    name="Web Search Agent",
    role="A web search agent that can find information on the internet.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source of the information you find."],
    show_tools_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
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

multi_ai_agent = Agent(
    team=[websearch_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display stock data."],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarise analyst recommendation and share the latest news for NVDA", stream=True)