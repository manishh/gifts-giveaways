import os
from datetime import datetime
from dotenv import load_dotenv
from typing import List

import yaml
from crewai import LLM, Agent, Task, Crew
from crewai.tools import BaseTool

# Load API key from `.env` file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# In-memory task list, in real life this will be in DB.
tasks: List[dict] = []

# Initialize LLM model, API key via environment variable: GEMINI_API_KEY
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.25
)

# Define tools
class AddTaskTool(BaseTool):
    name: str = "add_task"
    description: str = "Add a task given a natural language instruction."
    
    def _run(self, task_description: str):
        task = {
            'id': len(tasks) + 1,
            'description': task_description,
            'created_at': datetime.now().date().isoformat()
        }
        tasks.append(task)
        return f"Task added successfully. Task ID: {task['id']}."

class ListTasksTool(BaseTool):
    name: str = "list_tasks"
    description: str = "List all stored tasks."

    def _run(self):
        if not tasks:
            return "No tasks found."
        return "\n".join([
            f"ID: {task['id']}, Description: {task['description']}, Created: {task['created_at']}."
            for task in tasks
        ])

# List of available tools
tools = [AddTaskTool(), ListTasksTool()]

# Load YAML configs properly
def load_yaml_config(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

agents_config = load_yaml_config("./taskmanager_agent.yaml")
# print(agents_config)

# Create agent from configuration, LLM model, and tools
task_agent = Agent(config=agents_config['task_manager'], tools=tools, use_system_prompt=True)

# Task to handle user input (single-agent crew)
def process_command(user_input: str) -> str:
    task = Task(
        description=user_input,
        agent=task_agent,
        expected_output="Processed task command or error message. For non-task related input, respond with: 'Well, I’m just a simple task agent—I can’t handle that one.'"
    )
    crew = Crew(agents=[task_agent], tasks=[task])
    result = crew.kickoff()
    return result


# CLI demo
if __name__ == "__main__":
    print("CrewAI Task Manager (type 'exit' to quit)")
    while True:
        user_input = input("-->> ").strip()
        if user_input.lower() == "exit":
            print("Bye...")
            break
        result = process_command(user_input)
        print(result)