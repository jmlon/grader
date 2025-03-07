#!/usr/bin/env python
import sys
import warnings
import os

from assignmentgrader.crew import Assignmentgrader
from crewai.crews.crew_output import CrewOutput

TOPIC = 'Basic Programming Skills'
ASSIGNMENT = 'assignments/assignment2/assignment.md'
RUBRIC = 'assignments/assignment2/rubric.md'
SUBMISSIONS_DIR = 'assignments/assignment2/submissions'
EVALUATIONS_DIR = 'assignments/assignment2/evaluations'

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def load_file(filename:str) -> str:
    text = ''
    with open(filename, 'r') as f:
        text += f.read()
    return text

def run():
    """
    Run the crew.
    """
    assignment = load_file(ASSIGNMENT)
    rubric = load_file(RUBRIC)
    submission_files = [f for f in os.listdir(SUBMISSIONS_DIR) if os.path.isfile(os.path.join(SUBMISSIONS_DIR,f))]

    for submission in submission_files:
        print("Evaluating submission:", submission)
        fullpath = os.path.join(SUBMISSIONS_DIR, submission)
        solution = load_file(fullpath)
        base,_ = os.path.splitext(submission)
        evaluation = os.path.join(EVALUATIONS_DIR, f'{base}-evaluation.md')  

        inputs = {
            'topic': TOPIC,
            'assignment': assignment,
            'rubric': rubric,        
            'solution': solution,        
        }
        
        try:
            result:CrewOutput = Assignmentgrader().crew().kickoff(inputs=inputs)
            with open(evaluation, 'w') as f:
                f.write(result.raw)
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'Basic Programming Skills',
    }
    try:
        Assignmentgrader().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Assignmentgrader().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': 'Basic Programming Skills',
    }
    try:
        Assignmentgrader().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
