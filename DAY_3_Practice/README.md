\# Day 3 – Agentic AI Practice



\## Topics Covered



\- Tool Calling

\- AI Agent

\- Agent Loop

\- Webpage and Local File Reading

\- Calculator Tool

\- Guardrails

\- Repeat Tool-Call Detection

\- Character Limits

\- Large Input Handling

\- Groq API



\## Files



\### `my\_tools.py`

Contains the tools used by the agent:



\- Calculator

\- Webpage / local HTML file reader



\### `my\_agent.py`

A basic AI agent that:

1\. Receives a question

2\. Decides which tool to use

3\. Calls the tool

4\. Uses the tool result to generate an answer



\### `my\_agent\_fixed.py`

Improved agent with safety guards:



\- Detects repeated tool calls

\- Limits tool output

\- Limits total characters processed

\- Stops when the agent makes no progress



\### `make\_big\_page.py`

Creates a large `big.html` file containing student attendance records.



\### `notice.html`

Sample fee notice used for testing the file-reading tool.



\### `big.html`

Large HTML file generated using `make\_big\_page.py`.



\## Running the Programs



Install the required packages:



```bash

pip install groq beautifulsoup4

