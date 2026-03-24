from dataclasses import dataclass
from typing import Literal

from anthropic import Anthropic
from anthropic.types import MessageParam, ModelParam
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from lib.runtime import DEFAULT_MAX_TOKENS, DEFAULT_MODEL

type MessageRole = Literal["user", "assistant"]
type Messages = list[MessageParam]


@dataclass(slots=True, kw_only=True)
class ChatRequest:
    model: ModelParam = DEFAULT_MODEL
    messages: Messages
    max_tokens: int = DEFAULT_MAX_TOKENS
    system: str | None = None
    temperature: float = 1.0
    stream: bool = False
    stop_sequences: list[str] | None = None

    def api_kwargs(self) -> MessageCreateParamsNonStreaming:
        params: MessageCreateParamsNonStreaming = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": self.messages,
            "temperature": self.temperature,
        }

        if self.system is not None:
            params["system"] = self.system

        if self.stop_sequences is not None:
            params["stop_sequences"] = self.stop_sequences

        return params


def add_message(messages: Messages, message: MessageParam) -> None:
    messages.append(message)


def text_message(role: MessageRole, text: str) -> MessageParam:
    return {"role": role, "content": text}


def chat(client: Anthropic, request: ChatRequest) -> str:
    params = request.api_kwargs()

    if request.stream:
        full_text = ""

        with client.messages.stream(**params) as stream_obj:
            for text in stream_obj.text_stream:
                print(text, end="", flush=True)
                full_text += text
            print()

        return full_text

    response = client.messages.create(**params)

    if not response.content:
        return ""

    block = response.content[0]
    if block.type == "text":
        return block.text

    return ""
