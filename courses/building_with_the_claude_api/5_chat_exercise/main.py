from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.chat_utils import ChatRequest, Messages, add_message, chat, text_message
from lib.runtime import create_client


def main() -> None:
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

        add_message(messages, text_message("user", user_input))
        response = chat(
            client,
            ChatRequest(
                messages=messages,
            ),
        )
        print(f"Assistant: {response}\n")
        add_message(messages, text_message("assistant", response))


if __name__ == "__main__":
    main()
