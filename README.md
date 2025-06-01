# 🧳 Travel Buddy

> **Your AI-powered travel companion that crafts personalized travel experiences using LangChain, Gemini 1.5 Flash, and Tavily Search.**

## 📋 Table of Contents
- [Overview]
- [Architecture]
- [Project Structure]
- [Tech Stack]
- [Setup & Usage]


## 🌟 Overview

Travel Buddy is a sophisticated multi-agent AI system that creates personalized travel plans by leveraging specialized AI agents working in harmony. Each agent focuses on a specific aspect of travel planning, ensuring comprehensive and detailed travel recommendations.

## 🏗️ Architecture

### Basic Flow
```mermaid
flowchart TD
    User[User Input] -->|Form submission| UI[Streamlit UI]
    UI --> Orchestrator[Supervisor LLM]
    Orchestrator --> AgentsTeam[Specialized Agents]
    AgentsTeam -->|Parallel Tasks| Results[LLM-Polished Results]
    Results --> UI
    UI -->|Display| User
```

### Multi-Agent Orchestration
```mermaid
sequenceDiagram
    participant User
    participant UI
    participant Orchestrator
    participant Agents
    participant LLM

    User->>UI: Submit trip details
    UI->>Orchestrator: Forward request
    Orchestrator->>Agents: Delegate tasks
    Agents->>LLM: Process & polish data
    LLM-->>Agents: Return polished results
    Agents-->>Orchestrator: Aggregate results
    Orchestrator-->>UI: Display plan
    UI-->>User: Show recommendations
```

### Individual Agent Flows

#### Destination Agent
```mermaid
flowchart LR
    Input[User Request] -->|Process| DestAgent[Destination Agent]
    DestAgent -->|Search| Tavily[Tavily Search]
    Tavily -->|Data| DestAgent
    DestAgent -->|Polish| LLM[Gemini 1.5]
    LLM -->|Output| DestAgent
    DestAgent -->|Return| Results[Destination Info]
```

#### Flight Agent
```mermaid
flowchart LR
    Input[User Request] -->|Process| FlightAgent[Flight Agent]
    FlightAgent -->|Search| Tavily[Tavily Search]
    Tavily -->|Data| FlightAgent
    FlightAgent -->|Polish| LLM[Gemini 1.5]
    LLM -->|Output| FlightAgent
    FlightAgent -->|Return| Results[Flight Options]
```

#### Accommodation Agent
```mermaid
flowchart LR
    Input[User Request] -->|Process| AccomAgent[Accommodation Agent]
    AccomAgent -->|Search| Tavily[Tavily Search]
    Tavily -->|Data| AccomAgent
    AccomAgent -->|Polish| LLM[Gemini 1.5]
    LLM -->|Output| AccomAgent
    AccomAgent -->|Return| Results[Hotel Options]
```

#### Itinerary Agent
```mermaid
flowchart LR
    Input[User Request] -->|Process| ItinAgent[Itinerary Agent]
    ItinAgent -->|Generate| LLM[Gemini 1.5]
    LLM -->|Output| ItinAgent
    ItinAgent -->|Return| Results[Daily Schedule]
```

#### Local Experience Agent
```mermaid
flowchart LR
    Input[User Request] -->|Process| LocalAgent[Local Experience Agent]
    LocalAgent -->|Search| Tavily[Tavily Search]
    Tavily -->|Data| LocalAgent
    LocalAgent -->|Polish| LLM[Gemini 1.5]
    LLM -->|Output| LocalAgent
    LocalAgent -->|Return| Results[Local Activities]
```

#### Budget Agent
```mermaid
flowchart LR
    Input[User Request] -->|Process| BudgetAgent[Budget Agent]
    BudgetAgent -->|Search| Tavily[Tavily Search]
    Tavily -->|Data| BudgetAgent
    BudgetAgent -->|Polish| LLM[Gemini 1.5]
    LLM -->|Output| BudgetAgent
    BudgetAgent -->|Return| Results[Budget Tips]
```

#### Real-Time Alerts Agent
```mermaid
flowchart LR
    Input[User Request] -->|Process| AlertAgent[Real-Time Alerts Agent]
    AlertAgent -->|Search| Tavily[Tavily Search]
    Tavily -->|Data| AlertAgent
    AlertAgent -->|Polish| LLM[Gemini 1.5]
    LLM -->|Output| AlertAgent
    AlertAgent -->|Return| Results[Alerts & Updates]
```

### Tech Stack Flow
```mermaid
flowchart LR
    Input[User Input] -->|Process| Orchestrator[Supervisor LLM]
    Orchestrator -->|Delegate| Agents[Specialized Agents]
    Agents -->|Search| Tavily[Tavily Search]
    Agents -->|Process| LLM[Gemini 1.5]
    LLM -->|Output| Orchestrator
    Orchestrator -->|Display| UI[Streamlit UI]
    UI -->|Show| User
```

## 📁 Project Structure

```
travel-buddy/
├── agents/
│   ├── destination_agent.py
│   ├── flight_agent.py
│   ├── accommodation_agent.py
│   ├── itinerary_agent.py
│   ├── local_experience_agent.py
│   ├── budget_agent.py
│   └── realtime_adaptation_agent.py
├── orchestrator/
│   └── agent_manager.py
├── tools/
│   ├── tavily_search.py
│   └── llm.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## ⚙️ Tech Stack

- **LangChain**: Agent orchestration, memory, and tool integration
- **Gemini 1.5 Flash**: Fast, context-rich LLM for agent reasoning and communication
- **Tavily Search**: Real-time, web-grounded information
- **Streamlit**: Interactive, visually rich UI

## 🚀 Setup & Usage

1. Clone the repository
```bash
git clone https://github.com/srikrishnavansi/travel_buddy.git
cd travel-buddy
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run streamlit_app.py
```

4. Enter your Tavily and Google Gemini API keys in the sidebar

---

> **Built with ❤️ by leveraging the power of multi-agent AI, LLMs, and real-time data. Enjoy your next adventure!** 
