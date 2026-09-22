# 🤖 Agentic AI – Day 2 Practice Lab

## ReAct, Chain-of-Thought and Self-Consistency

This practice lab explores how AI agents solve multi-step problems using **ReAct (Reasoning + Acting)**, **Chain-of-Thought (CoT)** prompting, and **Self-Consistency**.

---

## 🎯 Objectives

* Trace the Thought → Action → Observation cycle of a ReAct agent.
* Compare a paper ReAct trace with a real agent trace.
* Compare answers with and without Chain-of-Thought prompting.
* Understand how step-by-step prompting affects reasoning.
* Experiment with Self-Consistency using multiple reasoning attempts.
* Understand when AI agents need tools to obtain external information.

---

## 🧪 Practice 1 – ReAct Trace

### Problem

Which is cheaper?

* CS101 + AI202 with a **10% scholarship**
* All three courses with a **25% scholarship**

### Course Fees

| Course |        Fee |
| ------ | ---------: |
| CS101  | Rs. 12,000 |
| AI202  | Rs. 18,000 |
| DS303  | Rs. 15,000 |

### Calculation

**Option 1:**

```text
(12,000 + 18,000) × 0.9
= Rs. 27,000
```

**Option 2:**

```text
(12,000 + 18,000 + 15,000) × 0.75
= Rs. 33,750
```

**Difference:**

```text
33,750 - 27,000
= Rs. 6,750
```

### Result

**CS101 + AI202 with 10% scholarship is cheaper by Rs. 6,750.**

The ReAct trace uses:

```text
Thought
   ↓
Action
   ↓
Observation
   ↓
Thought
   ↓
Action
   ↓
Observation
```

Tools used:

```text
get_course_fee(course_code)
calculator(expression)
```

---

## 🔧 Practice 2 – Real ReAct Agent

The `react_trace.py` program runs the same question using the Day 1 agent.

### Run

```bash
python react_trace.py
```

The program displays:

* Question
* Agent actions
* Tool observations
* Final answer

Expected result:

```text
Option 1 = Rs. 27,000
Option 2 = Rs. 33,750
Difference = Rs. 6,750
```

---

## 🧠 Practice 3 – Chain-of-Thought Comparison

The `cot_compare.py` program compares two prompting approaches.

### Without CoT

The model is asked to provide only the final answer.

```text
Give only the final answer. Do not explain.
```

### With CoT

The model is asked to solve the problem step by step.

```text
Solve the problem step by step.
Number each step and show the calculation in that step.
```

### Questions

#### Q1 – Instalments

Three courses cost Rs. 12,000, Rs. 18,000 and Rs. 15,000.

After a 15% scholarship, the remaining amount is paid in 4 instalments.

Expected answer:

```text
Rs. 9,562.50
```

#### Q2 – Lab Sittings

A lab has 18 computers.

* Morning: 2 students per computer
* Afternoon: 3 students per computer

Expected answer:

```text
90 student sittings
```

#### Q3 – Ordering

Ravi is taller than Kumar.
Kumar is taller than Arun.
Priya is shorter than Arun.

Expected answer:

```text
Tallest: Ravi
Shortest: Priya
```

### Run

```bash
python cot_compare.py
```

---

## 🔄 Practice 4 – Self-Consistency

The `self_consistency.py` program runs the same Chain-of-Thought question multiple times and selects the most frequent final answer.

### Configuration

```python
RUNS = 5
TEMPERATURE = 0.8
```

### Run

```bash
python self_consistency.py
```

Example:

```text
run 1: Rs. 9,562.50
run 2: Rs. 9,562.50
run 3: Rs. 11,250
run 4: Rs. 9,562.50
run 5: Rs. 9,562.50

Majority answer: Rs. 9,562.50
```

---

## 📂 Project Structure

```text
day1_lab/
│
├── .venv/
├── .env
├── config.py
├── tools.py
├── agent.py
│
├── react_trace.py
├── cot_compare.py
└── self_consistency.py
```

---

## 📊 Key Concepts

### ReAct

**ReAct = Reasoning + Acting**

The agent reasons about what it needs, calls a tool, observes the result, and continues until it can answer.

### Chain-of-Thought

Chain-of-Thought prompting asks the model to work through a problem step by step.

### Self-Consistency

Self-Consistency generates multiple reasoning attempts and uses the most common final answer.

---

## 💡 Key Learning

```text
Chain-of-Thought
       ↓
Reason using available information
```

```text
ReAct
       ↓
Reason
   +
Use Tools
   +
Observe Results
```

Chain-of-Thought cannot obtain information that is missing from the question. ReAct can use tools to retrieve required information.

---

## 📝 Discussion

The lab demonstrates that:

1. Different ReAct tool orders can still reach the same answer.
2. Step-by-step prompting can affect reasoning performance.
3. Chain-of-Thought does not provide missing external information.
4. ReAct can use tools to obtain required information.
5. Self-Consistency uses multiple reasoning attempts.
6. Temperature affects variation between multiple attempts.

---

## 🎓 Viva Questions

1. What are the three stages of a ReAct trace?
2. What is the difference between Thought, Action and Observation?
3. What is Chain-of-Thought prompting?
4. What is the difference between CoT and ReAct?
5. Why can Chain-of-Thought fail when information is missing?
6. Why does Self-Consistency require a non-zero temperature?
7. Why is voting performed on the final answer?
8. What happens when two tool calls have the same step number?
9. Give one advantage of Chain-of-Thought.
10. Give one limitation of Chain-of-Thought.

---

## 🛠️ Technologies Used

* Python
* Visual Studio Code
* Ollama / Groq / Hugging Face
* Python Virtual Environment
* ReAct
* Chain-of-Thought Prompting
* Self-Consistency

---

## ✅ Result

The Day 2 practice lab provided practical experience with:

```text
ReAct Trace
     +
Chain-of-Thought
     +
Self-Consistency
     ↓
Understanding Agentic AI Reasoning
```

The lab demonstrates how reasoning, tool usage, and multiple reasoning attempts can be used to solve multi-step problems.
