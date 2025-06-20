# Configuration for AI Web & Video Summarizer

# Ollama Configuration
OLLAMA_BASE_URL = "http://127.0.0.1:11434"
OLLAMA_MODEL = "qwen3:1.7b"

# Streamlit Configuration
STREAMLIT_PORT = 8501
STREAMLIT_HOST = "0.0.0.0"

# Text Processing Configuration
CHUNK_SIZE = 7500
CHUNK_OVERLAP = 100

# Supported Languages for Translation
SUPPORTED_LANGUAGES = {
    "turkish": "Turkish",
    "spanish": "Spanish",
    "french": "French",
    "german": "German"
}

# Default Translation Language
DEFAULT_TRANSLATION_LANGUAGE = "turkish"
