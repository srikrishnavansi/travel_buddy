def get_destination_info(destination, interests, budget, tavily_tool, llm, origin=None, start_date=None, end_date=None, currency="INR"):
    interests_str = ', '.join(interests)
    query = (
        f"Comprehensive travel guide for {destination} for a traveler from {origin or 'anywhere'}, "
        f"planning to visit from {start_date} to {end_date}. "
        f"Focus on these interests: {interests_str}. "
        f"Include safety, best time to visit, and current events. "
        f"Budget: {budget} {currency}."
    )
    web_results = tavily_tool.invoke({"query": query})['results']
    # Pass web results to LLM for summarization/beautification
    prompt = (
        f"You are a travel expert. Summarize and beautify the following web search results into a concise, engaging, and actionable destination overview for {destination}.\n"
        f"Focus on: {interests_str}, safety, best time to visit, and current events. Use bullet points and highlight key facts.\n\n"
        f"Web Search Results:\n"
        f"{web_results}"
    )
    response = llm.invoke(prompt)
    return response.content
