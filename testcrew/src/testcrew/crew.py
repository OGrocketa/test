from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
@CrewBase
class Pdfresearchers:
	"""Pdfresearchers crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# groq_llm= LLM(
	# 	model="groq/llama-3.3-70b-versatile",
	# 	api_key=os.environ.get('GROQ_API_KEY'),
	# )

	@agent
	def joke_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['joke_creator'],
			verbose=True,
		)

	@agent
	def add_emojis(self) -> Agent:
		return Agent(
			config=self.agents_config['add_emojis'],
			verbose=True,
		)


	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['joke_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['add_emopjis_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Pdfresearchers crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
