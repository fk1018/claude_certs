from typing import Final

from anthropic import Anthropic
from anthropic.types import ModelParam
from dotenv import load_dotenv

DEFAULT_MODEL: Final[ModelParam] = "claude-sonnet-4-5"
DEFAULT_MAX_TOKENS: Final[int] = 1000


def create_client() -> Anthropic:
    load_dotenv()
    return Anthropic()
