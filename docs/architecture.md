# Architecture

## Core flow

1. The user enters a sales/deal message in Streamlit.
2. The application sends the message to Hindsight `recall()`.
3. Relevant memories are returned from the `deals` memory bank.
4. Those memories are placed into the LLM system prompt.
5. Groq generates the response using the recalled context.
6. The user sees the response in Streamlit.
7. The original user deal information is sent to Hindsight `retain()` for future retrieval.

## Components

### Streamlit
Provides the conversational interface.

### Hindsight
Provides persistent memory through the `deals` bank.

### Groq
Provides the LLM inference endpoint through its OpenAI-compatible API.

### Python
Coordinates the UI, memory retrieval/storage, prompt construction and LLM request.

## Key design decision

The important architectural distinction is between:

- short-term UI conversation history stored in `st.session_state`
- persistent deal memory stored in Hindsight

The UI history helps maintain the current conversation, while Hindsight is responsible for retrieving relevant information from previous interactions.
