from agents.destination_agent import get_destination_info
from agents.flight_agent import get_flights
from agents.accommodation_agent import get_accommodation
from agents.itinerary_agent import get_itinerary
from agents.local_experience_agent import get_local_experiences
from agents.budget_agent import get_budget_tips
from agents.realtime_adaptation_agent import get_realtime_updates

class AgentManager:
    def __init__(self, tavily_tool, llm):
        self.tavily_tool = tavily_tool
        self.llm = llm

    def handle_query(self, query_type, destination, interests, budget, **kwargs):
        if query_type == "destination":
            return get_destination_info(destination, interests, budget, self.tavily_tool, self.llm, **kwargs)
        elif query_type == "flights":
            return get_flights(destination, interests, budget, self.tavily_tool, self.llm, **kwargs)
        elif query_type == "accommodation":
            return get_accommodation(destination, interests, budget, self.tavily_tool, self.llm, **kwargs)
        elif query_type == "itinerary":
            return get_itinerary(destination, interests, budget, self.llm, **kwargs)
        elif query_type == "local":
            return get_local_experiences(destination, interests, budget, self.tavily_tool, self.llm, **kwargs)
        elif query_type == "budget":
            return get_budget_tips(destination, interests, budget, self.tavily_tool, self.llm, **kwargs)
        elif query_type == "realtime":
            return get_realtime_updates(destination, interests, budget, self.tavily_tool, self.llm, **kwargs)
        else:
            return "Unknown query type."
