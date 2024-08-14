

import os
from dotenv import load_dotenv
from langchain.agents.agent_toolkits import GmailToolkit
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent

# Load environment variables from .env file
load_dotenv()

# Initialize the Gmail toolkit
toolkit = GmailToolkit()

# Retrieve the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Did not find OPENAI_API_KEY, please add it to the .env file.")

# Initialize the language model
llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo", openai_api_key=openai_api_key)

# Initialize the agent with the toolkit and language model
agent = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    verbose=True,
    max_iterations=1000,
    max_execution_time=1600,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
)

# Run the agent with a query
print(agent.run("send emial to dpmudra@gmail.com,asking for a leave tommarrow as i am not feeling well"))