def get_realtime_updates(destination, interests, budget, tavily_tool, llm, start_date=None, end_date=None, currency="INR"):
    query = (
        f"Latest travel advisories, weather alerts, and disruptions for {destination} "
        f"between {start_date} and {end_date}."
    )
    web_results = tavily_tool.invoke({"query": query})['results']
    prompt = (
        f"You are a travel safety and weather expert. Summarize and beautify the following real-time travel alerts and weather information for {destination}. "
        f"Highlight weather, safety tips, and any disruptions. Use bullet points or a short summary card.\n\n"
        f"Web Search Results:\n"
        f"{web_results}"
    )
    response = llm.invoke(prompt)
    return response.content
