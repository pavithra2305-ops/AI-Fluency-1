import json
from config import client, MODEL, QUESTIONS
from tools import TOOLS, TOOL_FUNCTIONS


def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful college course-fee assistant. "
                "You must use the available tools to answer the question. "
"First get the required course fees using get_course_fee. "
"Then use calculator for all arithmetic. "
"Do not calculate arithmetic yourself. "
"Only give the final answer after using the required tools."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:
            name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            result = TOOL_FUNCTIONS[name](**arguments)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )


if __name__ == "__main__":
    print("\n=== SYSTEM 3: AI AGENT ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", run_agent(question))
        print("-" * 70)