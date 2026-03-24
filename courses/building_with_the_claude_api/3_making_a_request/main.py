from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from anthropic.types import MessageParam
from lib.runtime import DEFAULT_MAX_TOKENS, DEFAULT_MODEL, create_client


def main() -> None:
    client = create_client()
    messages: list[MessageParam] = [
        {"role": "user", "content": "What is a banana split. Answer in one sentence"}
    ]
    response = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=DEFAULT_MAX_TOKENS,
        messages=messages,
    )

    if not response.content:
        return

    block = response.content[0]
    if block.type == "text":
        print(block.text)


if __name__ == "__main__":
    main()
