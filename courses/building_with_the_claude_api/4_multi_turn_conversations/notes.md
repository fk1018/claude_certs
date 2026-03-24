# Multi-Turn conversations

`https://anthropic.skilljar.com/claude-with-the-anthropic-api/287735`

*Claude doesn't store any of your conversation history.* Each request you make is
completely independent, with no memory of previous exchanges.

## The problem with stateless conversation
- There is no state

## How Multi-Turn Conversations Work
- Manually maintain list of all messages in your code
- Send the complete message history with every request

## Building helper functions
Heres three functions to make conversations easier
```python
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text
```

