from enum import Enum

class LLMEnums(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAIEnums(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class CoHereEnums(Enum):
    USER = "USER"
    ASSISTANT = "CHATBOT"
    SYSTEM = "SYSTEM"

    DOCUMENT_TYPE = "search_document"
    QUERY_TYPE = "search_query"

class DocumentTypeEnums(Enum):
    DOCUMENT = "document"
    QUERY = "query"