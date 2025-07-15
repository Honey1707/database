import os
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.azure import AzureProvider
from dotenv import load_dotenv

load_dotenv()

def get_azure_model(model_name):
    if model_name not in [
        "gpt-4.1",
        "gpt-4.1-mini",
        "gpt-4.1-nano",
        "o4-mini",
    ]:
        raise ValueError(f"Model {model_name} not supported")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    model = OpenAIModel(
        model_name,
        provider=AzureProvider(
            azure_endpoint=azure_endpoint,
            api_version=azure_api_version,
            api_key=azure_api_key,
        ),
    )
    
    return model


