# Python Tracing Test Suite

This directory contains standalone Python scripts that generate traces using different providers and tracing agents, mirroring the structure of the `js` folder.

## Structure

```
python/
├── index.py                    # Main entry point to run all providers
├── requirements.txt            # Python dependencies
├── helpers.py                  # Shared utility functions
├── wrap_anthropic/            # Anthropic SDK with wrap_anthropic
│   ├── main.py
│   ├── message.py
│   ├── streaming.py
│   ├── tool_call.py
│   ├── structured_outputs.py
│   ├── image_input.py
│   ├── pdf_input.py
│   ├── citations.py
│   └── serverside_tools.py
├── wrap_openai_chat/          # OpenAI Chat Completions API
│   ├── main.py
│   ├── message.py
│   ├── reasoning.py
│   ├── streaming.py
│   ├── tool_calls.py
│   ├── structured_outputs.py
│   └── multimodal.py
├── wrap_openai_responses/     # OpenAI Responses API
│   ├── main.py
│   ├── message.py
│   ├── reasoning.py
│   ├── streaming.py
│   ├── tool_calls.py
│   ├── structured_outputs.py
│   ├── multimodal.py
│   └── serverside_tools.py
└── langchain_v1/              # LangChain v1 with content blocks
    ├── main.py
    ├── message.py
    ├── streaming.py
    ├── tool_call.py
    ├── structured_outputs.py
    ├── multimodal_messages.py
    ├── multimodal_anthropic.py
    └── multimodal_openai.py
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env` file:
```bash
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
LANGSMITH_API_KEY=your_key_here
```

## Usage

### Run All Providers

```bash
python python/index.py
```

### Run Individual Providers

From the project root:
```bash
# Run wrap_anthropic examples
python python/wrap_anthropic/main.py

# Run wrap_openai chat completions examples
python python/wrap_openai_chat/main.py

# Run wrap_openai responses API examples
python python/wrap_openai_responses/main.py

# Run LangChain v1 examples
python python/langchain_v1/main.py
```

Or from the `python/` directory as modules:
```bash
cd python
python -m wrap_anthropic.main
python -m wrap_openai_chat.main
python -m wrap_openai_responses.main
python -m langchain_v1.main
```

## Features Tested

### wrap_anthropic
- Simple text messages
- Extended thinking (reasoning)
- Streaming responses
- Tool calls
- Structured outputs (JSON mode)
- Image inputs (base64 & URL)
- PDF inputs
- Citations (text/plain & PDF)
- Server-side tools (web search, code execution, Files API, MCP)

### wrap_openai_chat (Chat Completions)
- Simple chat messages
- Reasoning models (o1/o3)
- Streaming responses
- Tool calls (function calling)
- Structured outputs
- Multimodal (images & PDFs)

### wrap_openai_responses (Responses API)
- Simple response messages
- Reasoning
- Streaming responses
- Tool calls
- Structured outputs (parse with text_format)
- Multimodal (images & PDFs)
- Server-side tools (web search, image generation, code interpreter, MCP)

### langchain_v1
- Messages with init_chat_model (OpenAI & Anthropic)
- Streaming
- Tool binding and tool messages
- Structured outputs (with_structured_output)
- Multimodal messages (content_blocks)
- Anthropic-specific: reasoning/thinking, Files API, citations, web fetch
- OpenAI-specific: reasoning, web search, image generation, code interpreter

## Notes

- All scripts use `@traceable` decorator from LangSmith for tracing
- The structure mirrors the TypeScript implementation in the `js` folder
- Each provider can be run independently or all together via `index.py`
- Original Jupyter notebooks are preserved for reference

