def get_budget_tips(destination, interests, budget, tavily_tool, llm, start_date=None, end_date=None, currency="INR"):
    interests_str = ', '.join(interests)
    query = (
        f"Budget travel tips, cost-saving hacks, and average daily expenses for {destination} "
        f"for a trip from {start_date} to {end_date}, focusing on {interests_str}, "
        f"for a total budget of {budget} {currency}."
    )
    web_results = tavily_tool.invoke({"query": query})['results']
    prompt = (
        f"You are a travel budget expert. Summarize and beautify the following travel budget tips for {destination}. "
        f"Highlight key hacks, average costs, and how to maximize value. Use bullet points.\n\n"
        f"Web Search Results:\n"
        f"{web_results}"
    )
    response = llm.invoke(prompt)
    return response.content
