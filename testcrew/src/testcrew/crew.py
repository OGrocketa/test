from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from dotenv import load_dotenv

load_dotenv()
@CrewBase
class Pdfresearchers():
	"""Pdfresearchers crew"""

	pdf_source = PDFKnowledgeSource(
		file_paths=["ca2-data.pdf", "ca7-pipe.pdf","ca9-caches.pdf"]
	)


	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def data_extractor(self) -> Agent:
		return Agent(
			config=self.agents_config['data_extractor'],
			verbose=True,
			knowledge_sources=[self.pdf_source],

		)

	@agent
	def data_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['data_summarizer'],
			verbose=True,
		)


	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_data'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['summarize_data'],
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
