from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.chat_utils import ChatRequest, Messages, add_message, chat
from lib.runtime import DEFAULT_MAX_TOKENS, DEFAULT_MODEL, create_client


def main(model: str = DEFAULT_MODEL, max_tokens: int = DEFAULT_MAX_TOKENS) -> None:
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
    add_message(messages, "user", user_question)
    response = chat(
        client,
        ChatRequest(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            system=system,
        ),
    )
    print(response)


if __name__ == "__main__":
    main()
