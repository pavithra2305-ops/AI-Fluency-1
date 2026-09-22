"""Day 2: compare answers with and without Chain-of-Thought."""

import sys
sys.path.insert(0, r"..\DAY-1")

from config import client, MODEL


QUESTIONS = [
    "A student pays ₹10,000 after receiving a 20% discount. What was the original fee?",
    "A lab has 120 students. They are divided equally into 4 groups. Each group has 3 lab sittings. How many lab sittings are there in total?",
    "Ravi is taller than Arun. Arun is taller than Priya. Who is the tallest and who is the shortest?"
]


def ask(question, cot=False):
    if cot:
        instruction = (
            "Solve the problem step by step before giving the final answer. "
            "Show the reasoning clearly."
        )
    else:
        instruction = "Give only the final answer."

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": instruction
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content


for i, question in enumerate(QUESTIONS, 1):
    print(f"\nQUESTION {i}: {question}")

    print("\nWITHOUT CHAIN-OF-THOUGHT:")
    print(ask(question, cot=False))

    print("\nWITH CHAIN-OF-THOUGHT:")
    print(ask(question, cot=True))

    print("-" * 70)