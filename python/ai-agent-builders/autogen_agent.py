import asyncio
import os
from datetime import datetime
from dotenv import load_dotenv
from typing import List

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent

# Load API key from `.env` file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# In-memory task list, in real life this will be in DB.
tasks: List[dict] = []

# Define tools
def add_task(task_description: str) -> str:
    """Add a task given a natural language instruction."""
    task = {
        'id': len(tasks) + 1,
        'description': task_description,
        'created_at': datetime.now().date().isoformat()
    }
    tasks.append(task)
    return f"Task added successfully. Task ID: {task['id']}."

def list_tasks() -> str:
    """List all stored tasks."""
    if not tasks:
        return "No tasks found."

    task_list = "\n".join([
        f"ID: {task['id']}, Description: {task['description']}, Created: {task['created_at']}." 
        for task in tasks
    ])
    return task_list

# Initialize LLM model
model = OpenAIChatCompletionClient(
    model="gemini-2.0-flash",
    temperature=0.25,
    api_key=api_key
)

# List of available tools
tools=[add_task, list_tasks]

# Create prompt for task-management agent
system_prompt = """You are a task management assistant with access to these tools:
    1. add_task: Creates a new task
    2. list_tasks: Displays all existing tasks
    
    Instructions:
    - When a user wants to add a task (containing action items, deadlines, priorities, etc.), use the add_task tool
    - When a user wants to view their tasks, use the list_tasks tool
    - For non-task inputs, respond with: "Well, I’m just a simple task agent—I can’t handle that one."
    - Always confirm successful actions with clear, friendly feedback
     
    Remember to interpret the user's intent and respond accordingly, whether they use direct commands or natural language requests."""

agent = AssistantAgent(name="assistant", model_client=model, tools=tools, system_message=system_prompt)

# CLI demo
async def main():
    print("AutoGen Task Manager (type 'exit' to quit)")
    while True:
        user_input = input("-->> ").strip()
        if user_input.lower() == "exit":
            print("Bye...")
            break
        result = await agent.run(task=user_input)
        print(result.messages[-1].content)

if __name__ == "__main__":
    asyncio.run(main())
