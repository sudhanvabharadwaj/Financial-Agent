# Financial-Agent
This project implements AI-powered agents for financial data analysis and web search using the phi library. The agents leverage tools like YFinance for stock data and DuckDuckGo for web searches. The project includes two main components: a Financial Agent for analyzing stock data and a Web Search Agent for retrieving relevant information from the internet. Additionally, a playground interface is provided for interactive exploration of the agents' capabilities.

## Features
- Web Search Agent: Retrieves information from the internet using DuckDuckGo.
- Finance AI Agent: Provides stock data, analyst recommendations, company news, and financial fundamentals using YFinance.
- Multi-Agent System: Combines the capabilities of multiple agents for enhanced functionality.
- Interactive Playground: A web-based interface to interact with the agents.

## Setup Instructions
### Prerequisites
1. Python 3.10 or higher.
2. Install the required dependencies using pip:
   ```
    pip install -r requirements.txt
   ```
4. Create a .env file in the root directory with the following content:
   ```
    PHI_API_KEY="your_phi_api_key"
    GROQ_API_KEY="your_groq_api_key"
   ```

## How to Run
### Running financial_agent.py
This script demonstrates the functionality of the Web Search Agent and Finance AI Agent in a multi-agent setup.

Steps to Run:
1. Activate the virtual environment:
   .\venv\Scripts\activate
