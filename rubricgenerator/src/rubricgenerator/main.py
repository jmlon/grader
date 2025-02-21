#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai.crews.crew_output import CrewOutput
from rubricgenerator.crew import Rubricgenerator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


ASSIGNMENT = 'assignment/assignment.md'
RUBRIC = 'rubric/rubric.md'

def run():
    """
    Run the crew.
    """

    with open(ASSIGNMENT, 'r') as f:
        exercise = f.read()
    inputs = {
        'exercise': exercise,
    }
    
    try:
        result:CrewOutput = Rubricgenerator().crew().kickoff(inputs=inputs)
        with open(RUBRIC, 'w') as f:
            f.write(result.raw)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Rubricgenerator().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Rubricgenerator().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Rubricgenerator().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
