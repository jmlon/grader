# Setting up the CrewAI environment

This setup instructions have been tested on Linux Mint 21.3

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install 'crewai[tools]'
pip freeze > requirements.txt

crewai create crew assignmentgrader
cd assignmentgrader
crewai install
crewai run

```



