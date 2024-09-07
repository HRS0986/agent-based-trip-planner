from textwrap import dedent

from crewai import Agent
from langchain_openai import ChatOpenAI

from tools.calculator import CalculatorTool
from tools.search import SearchTool

class TravelAgents:
    def __init__(self):
        self.openai_gpt4o = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

    def expert_travel_agent(self) -> Agent:
        return Agent(
                role="Expert Travel Agent",
                goal=dedent(
                    """Create a 7-day travel plan with detailed per-day plans. Include budget, packing suggestions, and safety tips."""
                ),
                backstory=dedent(
                    """Expert in travel planning and logistics. 
                    I have decades of experience in the travel industry and have helped thousands of clients plan their dream vacations. 
                    I can provide expert advice on destinations, accommodations, transportation, and more."""
                ),
                verbose=True,
                llm=self.openai_gpt4o,
                tools=[CalculatorTool.calculate, SearchTool.search]
            )
        

    def city_selection_agent(self) -> Agent:
        return Agent(
            role="City Selection Agent",
            goal=dedent(
                """Select best cities based on weather, seasons, prices and travel interests."""
            ),
            backstory=dedent(
                """Expert at analyzing travel data to pick ideal destinations."""
            ),
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[CalculatorTool.calculate, SearchTool.search]
        )

    def local_tour_agent(self) -> Agent:
        return Agent(
            role="Local Tour Guide",
            goal=dedent("""Provide best insights about selected city."""),
            backstory=dedent(
                """Knowledgeable local guide with extensive information about the city, it's attractions and customs."""
            ),
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[CalculatorTool.calculate, SearchTool.search]
        )
