"""Day 2: simple self-consistency experiment."""

import sys
sys.path.insert(0, r"..\DAY-1")

from config import client, MODEL


QUESTION = (
    "A shop gives a 20% discount on an item. "
    "The customer pays ₹800. What was the original price?"
)


answers = []

for i in range(5):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Solve the problem and give the final numerical answer."
            },
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        temperature=0.8
    )

    answer = response.choices[0].message.content
    answers.append(answer)

    print(f"\nRUN {i + 1}:")
    print(answer)


print("\n--- SUMMARY ---")
for i, answer in enumerate(answers, 1):
    print(f"Run {i}: {answer}")