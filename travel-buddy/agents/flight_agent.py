def get_flights(destination, interests, budget, tavily_tool, llm, origin=None, start_date=None, end_date=None, currency="INR"):
    query = (
        f"Best flight options from {origin or 'major international airports'} to {destination}, "
        f"departing around {start_date} and returning around {end_date}, "
        f"for a traveler interested in {', '.join(interests)}. "
        f"Show airlines, layovers, and prices within a budget of {budget} {currency}."
    )
    web_results = tavily_tool.invoke({"query": query})['results']
    prompt = (
        f"You are a travel assistant. Summarize and format the following flight search results into a clear, user-friendly section. "
        f"Highlight best options, price ranges, and any tips for booking. Use bullet points or a neat table if possible.\n\n"
        f"Web Search Results:\n"
        f"{web_results}"
    )
    response = llm.invoke(prompt)
    return response.content
