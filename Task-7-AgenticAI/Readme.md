# 🧠 Task 07: Mastering OpenAI Agents SDK  
Welcome to **Task 07** of **Panaversity’s Learn Agentic AI** course!  
In this task, we explore the **OpenAI Agents SDK**, breaking down core concepts like the `Agent` and `Runner` classes.

---

## 🎯 What’s This About?

This task is designed to help you understand how the **OpenAI Agents SDK** works by simplifying its key parts and providing clear explanations in **English** and **Roman Urdu** with examples.

---

## ❓ Questions & Answers

### 1️⃣ Why is the `Agent` class a dataclass?

#### 🧾 English  
The `Agent` class uses Python’s `@dataclass` to store data like `name`, `instructions`, and `model` efficiently. It auto-generates methods like `__init__` and `__repr__`, making code:

- **Clean:** Less boilerplate.  
- **Safe:** Type hints ensure correctness.  
- **Simple:** Default values for flexibility.

#### 🗣️ Roman Urdu  
`Agent` class `@dataclass` isliye hai kyunke yeh `name`, `instructions`, aur `model` jaise data ko asaan tarike se store karta hai. Yeh `__init__`, `__repr__` jaise methods khud bana deta hai, jisse:

- **Code Saaf:** Kam likhna parta hai.  
- **Safe:** Type hints se galti nahi hoti.  
- **Asaan:** Default values milte hain.

#### 💻 Code Example

```python
from dataclasses import dataclass
from typing import Callable, List, Optional

@dataclass
class Agent:
    name: str
    instructions: str | Callable
    model: str = "gpt-4o-mini"
    tools: Optional[List[str]] = None

```


### 2️⃣ a. Why are `instructions` in the `Agent` class? Why can they be a Callable?

#### 🧾 English  
`instructions` define the agent’s role (e.g., “You’re a helpful assistant”).  
They are included in the `Agent` class for reuse across tasks.  
A **Callable** allows dynamic instructions based on context, making it more flexible.

#### 🗣️ Roman Urdu  
`instructions` agent ka role batate hain (jaise “Tum helpful assistant ho”).  
Yeh `Agent` class mein isliye hain kyunke har task ke liye reuse hote hain.  
Callable hone se aap function ke zariye instructions ko context ke hisaab se change kar sakte hain.

#### 💻 Code Example

```python
# Static instructions
agent = Agent(name="Helper", instructions="You are a helpful assistant.")

# Dynamic instructions
def dynamic_instructions(context):
    return f"You are a {context['role']} assistant."

agent = Agent(name="Dynamic", instructions=dynamic_instructions)

```


## 2️⃣ b. Why is the user prompt passed to `Runner.run`, and why is it a `classmethod`?

### 🧾 English  
The user prompt (e.g., “Write a poem”) is passed to `Runner.run` because it's specific to each task.  
It is a `classmethod` so you can run it without creating a `Runner` object:

```python
Runner.run(agent, prompt)

```

#### 🗣️ Roman Urdu

User prompt (jaise “Ek poem likho”) Runner.run mein isliye pass hota hai kyunke yeh har task ke liye naya hota hai.run method classmethod hai taake Runner ka object banaye baghair directly call ho sake, jo code ko asaan rakhta hai.

#### 💻 Code Example

from agents import Agent, Runner

```python
agent = Agent(name="Poet", instructions="Write creative poems.")
result = Runner.run(agent, "Write a poem about stars.")
print(result.final_output)
```


### 3️⃣ What does the Runner class do?

### 💾 English

- The Runner class is the “engine” that:
- Runs the agent with the user prompt
- Calls the LLM (e.g., OpenAI API)
- Manages tools, guardrails, and tracing
- Supports 100+ LLMs for flexibility

### 🗣️ Roman Urdu

- Runner class ek “engine” hai jo:
- Agent ko user prompt ke sath chalata hai
- LLM (jaise OpenAI API) se baat karta hai
- Tools, guardrails, aur tracing handle karta hai
- 100+ LLMs ke sath kaam karta hai



### 4️⃣ What are Generics in Python? Why use TContext?

### 💾 English

Generics (from the typing module) make code reusable and type-safe.TContext is a generic type for the agent’s context (e.g., a dictionary).It ensures type safety and lets developers customize the context without changing the SDK.

### 🗣️ Roman Urdu

Generics (typing module se) code ko reusable aur type-safe banate hain.TContext agent ke context (jaise dictionary) ke liye generic type hai.Yeh ensure karta hai ke context sahi type ka ho aur developers ko apna context 

### 💻 Code Example

``` python
from typing import TypeVar, Dict, Any

TContext = TypeVar('TContext', bound=Dict[str, Any])

class Runner:
    @classmethod
    def run(cls, agent: Agent, prompt: str, context: TContext) -> TContext:
        return context

```


