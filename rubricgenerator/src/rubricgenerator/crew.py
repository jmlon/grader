from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task



@CrewBase
class Rubricgenerator():
	"""Rubricgenerator crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def rubric_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['rubric_writer'],
			verbose=False
		)

	@task
	def rubric_task(self) -> Task:
		return Task(
			config=self.tasks_config['rubric_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Rubricgenerator crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=False,
		)
