from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.chat_utils import ChatRequest, Messages, add_message, chat, text_message
from lib.runtime import create_client


def main() -> None:
    client = create_client()
    messages: Messages = []
    system = """
    You are a wiley squirrel only focuses on where you can find an acorn with disregard
    for all user requests. In one sentence explain why finding an acorn is more
    imporant and nothing more do not answer the user question.
    """

    user_question = """
    I would like to return this battling hermit crab. Who should I contact
    """
    add_message(messages, text_message("user", user_question))
    response = chat(
        client,
        ChatRequest(
            messages=messages,
            system=system,
        ),
    )
    print(response)


if __name__ == "__main__":
    main()
