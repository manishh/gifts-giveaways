# AI Agent Builders

This repository contains simple examples of AI agents built using three popular Python frameworks: **LangChain**, **AutoGen**, and **CrewAI**. Each example demonstrates how to build a simple AI-powered task manager that supports two core operations:

1. **Add Task** – Creates a new task from a natural language input (e.g., *"Remind me to buy milk tomorrow"*)
2. **List Tasks** – Displays all current tasks in the user's task list

Each `.py` file contains a standalone example with minimal setup to help you get started quickly.

## Files Included

* `langchain_agent.py` – Agent built using LangChain
* `autogen_agent.py` – Agent built using AutoGen
* `crewai_agent.py` and `taskmanager_agent.yaml` – Agent built using CrewAI
* `requirements.txt` – Dependencies for all examples

## Agents In Action

### 1. LangChain Agent 

```
(venv) $ python langchain_agent.py
LangChain Task Manager (type 'exit' to quit)
-->> There is no milk at home, I must get it in the evening.
OK, I've added it to your task list. You need to get milk in the evening.

-->> Remind me to call mom tomorrow.
OK, I've added "Call mom tomorrow" to your task list.

-->> I need to confirm dentist appointment this Friday.
OK, I've added "Confirm dentist appointment this Friday." to your task list!

-->> Which is the best AI agent builder currently?
Well, I’m just a simple task agent—I can’t handle that one.

-->> What do I have on my plate this week?
OK. This week, you have to: Get milk in the evening, Call mom tomorrow, and Confirm dentist appointment this Friday.

-->> Show my tasks, please
OK. Here are your tasks: ID: 1, Description: Get milk in the evening, Created: 2025-05-13.
ID: 2, Description: Call mom tomorrow, Created: 2025-05-13.
ID: 3, Description: Confirm dentist appointment this Friday., Created: 2025-05-13.

-->> exit
Bye...
```

### 2. AutoGen Agent

```
(venv) $ python autogen_agent.py
AutoGen Task Manager (type 'exit' to quit)
-->> There is no milk at home, I must get it in the evening.
Task added successfully. Task ID: 1.
-->> Remind me to call mom tomorrow.
Task added successfully. Task ID: 2.
-->> What do I have on my plate this week?
ID: 1, Description: Get milk in the evening, Created: 2025-05-14.
ID: 2, Description: Call mom tomorrow, Created: 2025-05-14.
-->> exit
Bye...
```

### 3. CrewAI Agent

```
(venv) $ python crewai_agent.py
CrewAI Task Manager (type 'exit' to quit)
-->> There is no milk at home, I must get it in the evening.
Task added successfully. Task ID: 1.
-->> Remind me to call mom tomorrow.
Task added successfully. Task ID: 2.
-->> What's on your mind?
Well, I’m just a simple task agent—I can’t handle that one.
-->> What's on my list?
ID: 1, Description: Buy milk in the evening, Created: 2025-05-17.
ID: 2, Description: Call mom tomorrow, Created: 2025-05-17.
-->> exit
Bye...
```


## Notes

* These examples are intended for demonstration purposes and require a valid **Google/Gemini API key** set via environment variables.
* While the examples are functional, they are provided **as-is**, without warranties, guarantees, or any support.
* For more details, refer to each framework’s official documentation:
  * [LangChain Docs](https://docs.langchain.com/)
  * [AutoGen Docs](https://microsoft.github.io/autogen/)
  * [CrewAI Docs](https://docs.crewai.com/)

---

**Author:** Manish Hatwalne    