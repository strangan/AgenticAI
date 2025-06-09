from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import pandas as pd
from crewai_tools import FileReadTool
from crewai.tools import tool
import os

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

file_tool = FileReadTool(file_path='././data/customer_churn_dataset-training-master.csv')
output_file_path = '././output/'

@CrewBase
class AgenticAiPocBedrock():
    """AgenticAiPocBedrock crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    
    @agent
    def data_ingestor(self) -> Agent:
        return Agent(
            config=self.agents_config['data_ingestor'], # type: ignore[index]
            verbose=True,
            allow_delegation=True,
            tools=[file_tool]
        )

    @agent
    def exploratory_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['exploratory_analyst'], # type: ignore[index]
            verbose=True,
            allow_delegation=True,
            context=[self.data_ingestor()]
        )
        
    @agent
    def visualization_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['visualization_analyst'], # type: ignore[index]
            verbose=True,
            allow_delegation=True,
            context=[self.exploratory_analyst()]
        )

    @agent
    def statistical_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['statistical_analyst'], # type: ignore[index]
            verbose=True,
            allow_delegation=True,
            context=[self.exploratory_analyst()]
        )
        
    @agent
    def insight_synthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config['insight_synthesizer'], # type: ignore[index]
            verbose=True,
            allow_delegation=True,
            context=[self.exploratory_analyst(), self.statistical_analyst()]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    @task
    def data_ingestion_cleaning_transformation_task(self) -> Task:
        fileName = "dataIngestion_Report"
        return Task(
            config=self.tasks_config['data_ingestion_cleaning_transformation_task'], # type: ignore[index]
            output_file=output_file_path + fileName + ".md"
        )

    @task
    def eda_task(self) -> Task:
        fileName = "eda_Report"
        return Task(
            config=self.tasks_config['eda_task'], # type: ignore[index]
            output_file=output_file_path + fileName + ".md"
        )
        
    @task
    def statistical_analysis_task(self) -> Task:
        fileName = "statistical_Report"
        return Task(
            config=self.tasks_config['statistical_analysis_task'], # type: ignore[index]
            output_file=output_file_path + fileName + ".md"
        )

    @task
    def causal_inference_modeling_task(self) -> Task:
        fileName = "causalinference_Report"
        return Task(
            config=self.tasks_config['causal_inference_modeling_task'], # type: ignore[index]
            output_file=output_file_path + fileName + ".md"
        )
        
    @task
    def visualization_generation_task(self) -> Task:
        fileName = "visualization_Report"
        return Task(
            config=self.tasks_config['visualization_generation_task'], # type: ignore[index]
            output_file=output_file_path + fileName + ".md"
        )
        
    @task
    def insights_reports_generation_task(self) -> Task:
        fileName = "FinalAnalysis_Report"
        return Task(
            config=self.tasks_config['insights_reports_generation_task'], # type: ignore[index]
            output_file=output_file_path + fileName + ".md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AgenticAiPocBedrock Data Analysis crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
        

