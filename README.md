# grader

CrewAI grader - An AI assisted assignment grader

## Really, really quick guide

### For running the assignment grader

1. Place assigment definition and rubric in the folder `assignmentgrader/assignment/`.
2. Place submissions in the folder `assignmentgrader/submissions/`.
3. Run the crew with the following commands

```bash
cd assignmentgrader
crewai run
```

4. Check the evaluations in the folder `assignmentgrader/evaluations/`.

### For running the rubric construction crew

1. Place assigment definition in the folder: `rubricgenerator/assignment/`
2. Run the crew with the following commands

```bash
cd rubricgenerator
crewai run
```

3. The generated rubric should be in the folder: `rubricgenerator/rubric/`

