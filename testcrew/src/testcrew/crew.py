from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from testcrew.tools.DirectoryPdfSearch import directory_pdf_search
from dotenv import load_dotenv

load_dotenv()
@CrewBase
class Testcrew:
	"""Testcrew crew"""


	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def data_extractor(self) -> Agent:
		return Agent(
			config=self.agents_config['data_extractor'],
			max_iter = 5,
			tools = [directory_pdf_search]
		)

	@agent
	def data_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['data_summarizer'],
		)

	@agent
	def standup_comedian(self)->Agent:
		return Agent(
			config=self.agents_config['standup_comedian'],
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_data'],
			tools = [directory_pdf_search]
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['summarize_data'],
		)

	@task
	def add_joke(self)->Task:
		return Task(
			config=self.tasks_config['add_joke'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Testcrew crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			memory=True,
			long_term_memory = LongTermMemory(
				storage=LTMSQLiteStorage(
						db_path="./db/long_term_memory_storage.db"
					)
			),


		)
