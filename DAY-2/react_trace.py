"""Day 2: print the agent's real ReAct trace to compare with your paper trace."""

import sys
sys.path.insert(0, r"..\DAY-1")

from agent import run_agent

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or CS101, AI202, and DS303 with a 25% scholarship? By how much?"
)

print("QUESTION:", QUESTION, "\n")

print("--- the agent's actions and observations ---")

answer = run_agent(QUESTION)

print("\nFINAL ANSWER:", answer)