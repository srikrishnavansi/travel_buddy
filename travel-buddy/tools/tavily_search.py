from langchain_tavily import TavilySearch

def get_tavily_tool(tavily_api_key: str):
    # TavilySearch expects the API key to be set in the environment,
    # but we set it dynamically for each session.
    import os
    os.environ["TAVILY_API_KEY"] = tavily_api_key
    return TavilySearch(
        max_results=5,
        topic="general"
    )
