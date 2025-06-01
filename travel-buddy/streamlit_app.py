import streamlit as st
import pandas as pd
from datetime import date
from tools.tavily_search import get_tavily_tool
from tools.llm import get_gemini_llm
from orchestrator.agent_manager import AgentManager

st.set_page_config(page_title="Intelligent Travel Orchestrator", layout="wide")
st.title("🌍 Intelligent Travel Orchestrator")

# --- API Keys ---
with st.sidebar:
    st.header("🔑 API Keys (Required)")
    tavily_api_key = st.text_input("Tavily API Key", type="password")
    google_api_key = st.text_input("Google API Key (Gemini)", type="password")
    st.markdown(
        "[Get Tavily Key](https://app.tavily.com/) | [Get Google API Key](https://makersuite.google.com/app/apikey)"
    )

# --- User Inputs ---
with st.form("travel_form"):
    st.subheader("🧳 Your Trip Details")
    col1, col2 = st.columns(2)
    with col1:
        origin = st.text_input("Origin City/Airport", placeholder="e.g., Mumbai")
        destination = st.text_input("Destination", placeholder="e.g., Paris")
        start_date = st.date_input("Journey Start Date", value=date.today())
    with col2:
        end_date = st.date_input("Journey End Date", value=date.today())
        currency = st.selectbox("Currency", ["INR", "USD", "EUR", "GBP", "JPY", "CNY", "AUD"], index=0)
        budget = st.number_input(f"Total Budget ({currency})", min_value=100, max_value=10000000, value=100000)
        interests = st.multiselect(
            "What are your interests?",
            ["Sightseeing", "Food & Culinary", "Adventure", "Culture & History", "Shopping", "Nature", "Nightlife", "Relaxation", "Art", "Sports"],
            default=["Sightseeing", "Food & Culinary"]
        )
    submitted = st.form_submit_button("Generate My Travel Plan 🚀")

if not tavily_api_key or not google_api_key:
    st.warning("Please enter both Tavily and Google Gemini API keys in the sidebar.")
    st.stop()

if submitted and all([origin, destination, start_date, end_date, budget, interests]):
    tavily_tool = get_tavily_tool(tavily_api_key)
    llm = get_gemini_llm(google_api_key)
    agent_manager = AgentManager(tavily_tool, llm)

    # --- Summary Table ---
    st.header(f"🌟 {origin} → {destination} | {start_date.strftime('%b %d, %Y')} - {end_date.strftime('%b %d, %Y')}")
    st.subheader("🔎 Trip Summary")
    summary_dict = {
        "Origin": origin,
        "Destination": destination,
        "Dates": f"{start_date.strftime('%b %d, %Y')} - {end_date.strftime('%b %d, %Y')}",
        "Budget": f"{budget:,} {currency}",
        "Interests": ", ".join(interests)
    }
    summary_df = pd.DataFrame(summary_dict.items(), columns=["Item", "Value"])
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

    # --- Tabs for Each Section ---
    tab_names = [
        "Destination Overview", "Flights", "Accommodation", "Itinerary",
        "Local Experiences", "Budget Tips", "Real-time Alerts & Weather"
    ]
    tabs = st.tabs(tab_names)

    with tabs[0]:
        with st.spinner("🔎 Your destination is being researched thoroughly by our expert agent..."):
            dest_info = agent_manager.handle_query(
                "destination", destination, interests, budget,
                origin=origin, start_date=start_date, end_date=end_date, currency=currency
            )
            st.markdown("### 🗺️ Destination Overview")
            st.info(dest_info)

    with tabs[1]:
        with st.spinner("✈️ Flights are being scouted for you with utmost certainty..."):
            flights = agent_manager.handle_query(
                "flights", destination, interests, budget,
                origin=origin, start_date=start_date, end_date=end_date, currency=currency
            )
            st.markdown("### ✈️ Flight Options")
            st.info(flights)

    with tabs[2]:
        with st.spinner("🏨 Handpicking the best accommodation options for your comfort..."):
            hotels = agent_manager.handle_query(
                "accommodation", destination, interests, budget,
                start_date=start_date, end_date=end_date, currency=currency
            )
            st.markdown("### 🏨 Accommodation Suggestions")
            st.success(hotels)

    with tabs[3]:
        with st.spinner("🗓️ Crafting your perfect day-by-day itinerary..."):
            itinerary = agent_manager.handle_query(
                "itinerary", destination, interests, budget,
                start_date=start_date, end_date=end_date, origin=origin, currency=currency
            )
            st.markdown("### 🗓️ Your Day-by-Day Itinerary")
            st.markdown(itinerary, unsafe_allow_html=True)

    with tabs[4]:
        with st.spinner("🍜 Curating authentic local experiences and food adventures..."):
            local = agent_manager.handle_query(
                "local", destination, interests, budget,
                start_date=start_date, end_date=end_date, currency=currency
            )
            st.markdown("### 🍜 Local Experiences & Food")
            st.success(local)

    with tabs[5]:
        with st.spinner("💸 Uncovering the smartest budget tips for your journey..."):
            budget_tips = agent_manager.handle_query(
                "budget", destination, interests, budget,
                start_date=start_date, end_date=end_date, currency=currency
            )
            st.markdown("### 💸 Budget & Cost-Saving Tips")
            st.warning(budget_tips)

    with tabs[6]:
        with st.spinner("🚨 Checking real-time alerts and weather so you travel safe..."):
            realtime = agent_manager.handle_query(
                "realtime", destination, interests, budget,
                start_date=start_date, end_date=end_date, currency=currency
            )
            st.markdown("### 🚨 Real-time Alerts & Weather")
            st.error(realtime)

    st.balloons()
    st.success("Your personalized travel plan is ready! All information is fetched live from the web and LLM. No mock data used.")

st.markdown("---")
st.markdown("Built with ❤️ using LangChain, Gemini 1.5 Flash, and Tavily Search.")
