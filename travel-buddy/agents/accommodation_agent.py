def get_accommodation(destination, interests, budget, tavily_tool, llm, start_date=None, end_date=None, currency="INR"):
    interests_str = ', '.join(interests)
    query = (
        f"Top rated hotels and unique stays in {destination} "
        f"for dates {start_date} to {end_date}, "
        f"matching interests: {interests_str}, "
        f"with amenities and reviews, within a total budget of {budget} {currency}."
    )
    web_results = tavily_tool.invoke({"query": query})['results']
    prompt = (
        f"You are a travel accommodation expert. Summarize and beautify the following hotel search results for {destination}. "
        f"List the best options (name, location, highlights, price range), and give a short tip for choosing. Use bullet points or a short table.\n\n"
        f"Web Search Results:\n"
        f"{web_results}"
    )
    response = llm.invoke(prompt)
    return response.content
