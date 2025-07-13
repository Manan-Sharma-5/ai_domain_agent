from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
import os
from typing import List
from ai_domain_agent.tools.custom_tool import (
    keyword_research_tool,
    domain_availability_checker
)

@CrewBase
class AiDomainAgent():
    """AiDomainAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    agent_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
    )
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=self.gemini_llm,
            verbose=True
        )

    @agent
    def domain_name_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['domain_name_creator'],
            verbose=True,
            llm=self.gemini_llm,
        )
        
    @agent
    def domain_availability_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['domain_availability_checker'],
            tools=[domain_availability_checker],
            llm=self.gemini_llm,
            verbose=True
        )
        
    @agent
    def domain_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['domain_evaluator'],
            llm=self.gemini_llm,
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], 
        )

    @task
    def domain_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['domain_creation_task'],
        )
        
    @task
    def availability_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['availability_check_task'],
        )
        
    @task
    def domain_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['domain_evaluation_task'],
            output_file="output/domain_recommendations.md"  # Markdown file for recommendations

        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiDomainAgent crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
