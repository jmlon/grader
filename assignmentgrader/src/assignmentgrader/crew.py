from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class Assignmentgrader():
	"""Assignmentgrader crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def grader(self) -> Agent:
		return Agent(
			config=self.agents_config['grader'],
			verbose=False
		)

	@agent
	def checker(self) -> Agent:
		return Agent(
			config=self.agents_config['checker'],
			verbose=False
		)

	@task
	def evaluation(self) -> Task:
		return Task(
			config=self.tasks_config['evaluation'],
		)

	@task
	def reviewing(self) -> Task:
		return Task(
			config=self.tasks_config['reviewing'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Assignmentgrader crew"""

		return Crew(
			agents=self.agents, 
			tasks=self.tasks,
			process=Process.sequential,
			verbose=False,
			max_rpm=3,
		)
