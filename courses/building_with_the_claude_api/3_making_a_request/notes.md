# Making a request

`https://anthropic.skilljar.com/claude-with-the-anthropic-api/287725`

## Setting up env

### Install dependencies

`%pip install anthropic python-dotenv`

### Place api key in env file

look at `.env.example` for example `.env file`

## The Create Function

The core of making API request is the *client.messages.create()* function. This function
requires three key parameters:
- *model* - The name of the Claude model you want to use
- *max_tokens* - A safety limit on response length (not a target)
- *messages* - The conversation history you're sending to Claude

## Understanding Messages

Messages represent the conversation between you and Claude, similar to a chat
application. There are two types of messages:
- *User Messages* - Content you want to send to Claude(written by humans)
- *Assistant Messages* - Responses that Claude has generated

Each message is a dictionary with a `role` (either "user" or "assistant") and `content`
(the actual text).

