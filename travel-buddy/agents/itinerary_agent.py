def get_itinerary(destination, interests, budget, llm, start_date=None, end_date=None, origin=None, currency="INR"):
    interests_str = ', '.join(interests)
    prompt = (
        f"You are a world-class travel planner. Create a visually structured, day-by-day itinerary for a trip from {origin or 'home'} to {destination}, "
        f"from {start_date} to {end_date}. Traveler's interests: {interests_str}. Total budget: {budget} {currency}. "
        f"Include sightseeing, food, local experiences, and tips for each day. "
        f"Format as a markdown table or bullet list with bold day headings and clear separation."
    )
    response = llm.invoke(prompt)
    return response.content
