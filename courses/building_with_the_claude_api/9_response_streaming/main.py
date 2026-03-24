from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from anthropic import APIStatusError
from lib.chat_utils import ChatRequest, Messages, add_message, chat
from lib.runtime import DEFAULT_MAX_TOKENS, DEFAULT_MODEL, create_client


def main(model: str = DEFAULT_MODEL, max_tokens: int = DEFAULT_MAX_TOKENS) -> None:
    client = create_client()
    messages: Messages = []

    print("Chat CLI. Type 'quit' or 'exit' to leave.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not user_input:
            continue

        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye.")
            break

        add_message(messages, "user", user_input)
        # was testing with 'Provide me song lyrics to "Hit me baby one more time".'
        # it throws an error bc its copyright midway through wanted to see what error
        # handling looked like
        try:
            print("Assistant: ", end="", flush=True)
            response = chat(
                client,
                ChatRequest(
                    model=model,
                    messages=messages,
                    max_tokens=max_tokens,
                    stream=True,
                ),
            )
            add_message(messages, "assistant", response)

        except APIStatusError as e:
            print(f"\n[API error] {e}\n")

        except Exception as e:
            print(f"\n[Unexpected error] {e}\n")


if __name__ == "__main__":
    main()
