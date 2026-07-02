from enum import Enum

class LLMEnums(Enum):
    OPENAI = "openai"
    COHERE = "cohere"

class OpenAIEnums(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"