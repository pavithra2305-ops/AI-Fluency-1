from agent import run_agent


CHALLENGE_QUESTIONS = [
    "What is the fee for CS101?",
    "What is the fee for DS303?",
    "What is the total fee for AI202 and DS303?",
    "What will I pay for CS101 and AI202 with a 20% scholarship?",
    "Which is more expensive, AI202 or DS303, and by how much?",
]


if __name__ == "__main__":
    print("\n=== DAY 1 CHALLENGE ===\n")

    for question in CHALLENGE_QUESTIONS:
        print("Q:", question)
        print("A:", run_agent(question))
        print("-" * 70)