# Response streaming

`https://anthropic.skilljar.com/claude-with-the-anthropic-api/287734`

## The problem

You don't wanna wait on full response.

## How Streaming Works

With streaming enabled, claude immediately sends back an initial repsonse. Then you
receive a series of events, each containing a small piece of overall response.

## Understanding Stream Events

- *MessageStart* - A new message is being sent
- *ContentBlockStart* - Start of a new block containing text, tool use, or other content
- *ContentBlockDelta* - Chunks of the actual generated text
- *ContentBlockStop* - The current content block has been completed
- *MessageDelta* - The current message is complete
- *MessageStop* - End of information about the current message

The `ContentBlockDelta` events contain the actual generated text that you want to
display to users.
