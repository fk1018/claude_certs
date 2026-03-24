# System Prompts

`https://anthropic.skilljar.com/claude-with-the-anthropic-api/287733`

System prompt are a powerful way to customize how Claude responds to user input. You
can shape Claude's tone, style, and approach to match your specific use case.

## Why System Prompts Matter

Consider building a math tutor chatbot. When a student asks " How do i solve x", you
want Claude to act like a real tutor, not just spit out the answer. A good tutor would:

- Initially give hints rather than complete solutions
- Patientily walk students through problems step by step
- Show solutions for similar problems as examples

You dont want Claude to:
- Immediately give direct answers
- Tell students to use a calculator

## How System Prompts Work

System prompts provide Claude with guidance on how to respond. You define them as a
plain string and pass them into create function call. The key benefits are:

- Provide claude guidance
- Helps claude on task
- Tries to respond same way the specified role would respond

example structure:
```python
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
    model=model,
    messages=messages,
    max_tokens=1000,
    system=system_prompt
)
```

## Seeing the Difference
Without a system prompt claude would immediately give a step by step solution. 

# Notes
- Updated our `chat_utils.py` chat method to include system