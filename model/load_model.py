from pydantic_ai import Agent
from model.get_model import get_azure_model
from model.prompt import system_prompt

description_agent = Agent(
    get_azure_model("gpt-4.1"),
    name="Orchestrator Agent",
    system_prompt=system_prompt,
)