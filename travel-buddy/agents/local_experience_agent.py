def get_local_experiences(destination, interests, budget, tavily_tool, llm, start_date=None, end_date=None, currency="INR"):
    interests_str = ', '.join(interests)
    query = (
        f"Authentic local experiences, hidden gems, and best restaurants in {destination} "
        f"for a traveler visiting from {start_date} to {end_date}, interested in {interests_str}, "
        f"within a budget of {budget} {currency}."
    )
    web_results = tavily_tool.invoke({"query": query})['results']
    prompt = (
        f"You are a local guide. Summarize and beautify the following local experience search results for {destination}. "
        f"Highlight unique experiences, must-try foods, and hidden gems. Use bullet points or a short table.\n\n"
        f"Web Search Results:\n"
        f"{web_results}"
    )
    response = llm.invoke(prompt)
    return response.content
