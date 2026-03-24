# Accessing the API

## Key Takeaways
- Design secure architectures that protect your API keys
- Set appropriate token limits for your use case
- Handle different stop reasons in your application logic
- Debug issues by understanding where they might occur in the pipeline

## The Five-Step Request Flow

Every Interaction with Claude follows a predictable pattern with five distinct phases:

1. Request to Server
2. Request to Anthropic API
3. Model Processing
4. Response to Server
5. Response to Client

## Why You Need A Server

You should never make requests directly from clien-side code. Here is why:

- API requests require a secret API key for authentication
- Exposing this key in client code creates a serious security vulnerability
- Anyone could extract the key and make unauthorized requests

Instead, your web or mobile app sends the requests to your own server, which then
communicates with the Anthropic API using the securely stored key.

## Making API Requests

You can use sdks or normal http requests. Anthropic has offical support for Python,
Typescript, Javascript, Go, and Ruby.

Every Request must include these essential fields:
- *API Key* 	- Identifies your request to Anthropic
- *Model* 		- Name of the model to use
- *Messages* 	- List containing the user's input text 
- *Max Tokens* 	- Limit for how many tokens Claude can generate

## Inside Claude's Processing

Once Anthropic receives your request, Claude processes it through four man stages:
1. tokenization
2. embedding
3. contextualization
4. generation

### Tokenization

Claude first breaks your input into smaller chunks called tokens. These can be whole
words, parts of words, spaces, or symbols.

### Embedding

Each token gets converted into an embedding, which is a long list of numbers that
represents all possible meanings of that word. Think of embeddings as numberical
definitions that capture semantic relationships.

### Contextualization

Claude refines each embedding based on surrounding words to determine the most likely
meaning in the context. This process adjusts the numerical representations to highlight
the appropriate definition.

### Generation

The contextualized embeddings pass through an output layer that calculates probabilities
for each possible word, it uses a mis of probability and controlled randomness to create
natural, varied responses.

## When Claude Stops Generating

After each token, Claude checks several conditions to decide whether to continue:
- *Max tokens reached* - Has it hit the limit you specified?
- *Natural ending* - Did it generate an end-of-sequence token?
- *Stop sequence* - Did it encounter a predefined stop phrase?

## The API Response

When generation completes the API sends back a structured response containing:
- *Message* - The generated text
- *Usage* - Count of intput and output tokens
- *Stop Rease* - Why generation ended