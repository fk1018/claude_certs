from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.chat_utils import ChatRequest, Messages, add_message, chat
from lib.runtime import DEFAULT_MAX_TOKENS, DEFAULT_MODEL, create_client


def main(model: str = DEFAULT_MODEL, max_tokens: int = DEFAULT_MAX_TOKENS) -> None:
    client = create_client()
    messages: Messages = []

    print("Chat CLI. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye.")
            break

        if not user_input:
            continue

        add_message(messages, "user", user_input)
        response = chat(
            client,
            ChatRequest(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
            ),
        )
        print(f"Assistant: {response}\n")
        add_message(messages, "assistant", response)


if __name__ == "__main__":
    main()
