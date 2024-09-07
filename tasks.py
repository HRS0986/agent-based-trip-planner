from crewai import Task, Agent
from textwrap import dedent

class TravelTasks:
    def __tip_section(self) -> str:
        return "If you do your best work, I'll give you a $10,000 commission."
    
    def plan_trip(self, agent, city, travel_dates, interests) -> Task:
        print(type(agent))
        return Task(
            description=dedent(
                f"""
                Tasks: Develop a 7-day travel plan
                Description: Expand the city guide into a full 7-day travel plan with detailed per-day plans, 
                including weather forecasts, places to eat, parking suggestions, and a budget breakdown.
                You must suggest actual places to visit, actual hotels to stay, and actual restaurants to eat.
                This travel plan should cover all aspects of the trip, from arrival to departure, integrating 
                the city guide information with practical travel logistics
                Parameters:
                    - City: {city}
                    - Travel Dates: {travel_dates}
                    - Interests: {interests}
                Note: {self.__tip_section()}
                """
            ),
            agent=agent
        )
    
    def identify_city(self, agent, origin, cities, interests, travel_dates) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Identify the best city to visit
                Description: Analyze the given cities based on weather, seasons, prices, and travel interests to 
                recommend the best city to visit. This task involves comparing multiple cities, considering factors 
                like current weather conditions, upcoming cultural or seasonal events, and overall travel expenses.
                Your final answer must be a detailed report on the chosen city including actual costs, weather forecast, and attractions
                Parameters:
                    - Origin: {origin}
                    - Cities: {cities}
                    - Interests: {interests}
                    - Travel Dates: {travel_dates}
                Note: {self.__tip_section()}
                """
            ),
            agent=agent
        )
    
    def gather_city_info(self, agent, city, travel_dates, interests) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: gather in-depth information about city
                Description: Compile an in-depth guide for the selected city, gathering information about key attractions, 
                local customs, special events, and daily activity recommendations. This guide should provide a thorough 
                overview of what the city has to offer, including hidden gems, cultural hotspots, must-visit landmarks, 
                weather forecasts, and high-level costs.
                Parameters:
                    - City: {city}
                    - Travel Dates: {travel_dates}
                    - Interests: {interests}
                Note: {self.__tip_section()}
                """
            ),
            agent=agent
        )