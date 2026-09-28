# 💼 Deal Intelligence Agent

A memory-enabled sales agent that uses **Hindsight** to remember deal context across interactions and **Groq** to generate responses.

## What problem does it solve?

Sales representatives often have to reread CRM notes, meeting notes, and previous conversations to recover details about an active deal.

This project provides a conversational Deal Intelligence Agent that can recall information such as:

- Customer and stakeholder details
- Deal objections
- Competitors being considered
- Pricing discussions
- Deal status
- Previous interaction context

The goal is to make the agent more useful over time by giving it persistent memory.

## Architecture

```text
                    ┌──────────────────────┐
                    │      User / Sales Rep│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit Chat UI  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Hindsight Recall    │
                    │  Persistent Memory   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Groq LLM        │
                    │  openai/gpt-oss-20b  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Agent Reply     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Hindsight Retain     │
                    │ Save new deal memory │
                    └──────────────────────┘
```

## Technology Stack

- Python
- Streamlit
- Hindsight by Vectorize
- Groq API
- OpenAI Python SDK (used with Groq's OpenAI-compatible API)
- python-dotenv

## Project Structure

```text
deal-intelligence-agent/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── docs/
    ├── architecture.md
    ├── demo-script.md
    └── submission-checklist.md
```

## Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd deal-intelligence-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the environment file

```bash
cp .env.example .env
```

Open `.env` and add your own API keys:

```text
HINDSIGHT_API_KEY=your_key
GROQ_API_KEY=your_key
```

**Never commit `.env` to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The application should open at:

```text
http://localhost:8501
```

## Memory Workflow

The application uses Hindsight in two important places:

### Recall

Before generating an answer, the application asks Hindsight for memories relevant to the user's latest message.

```python
memories = recall(prompt)
```

Those memories are added to the system context sent to the LLM.

### Retain

After the response is generated, the user's deal information is stored in Hindsight:

```python
remember(prompt)
```

This allows later interactions to retrieve previously stored deal information.

## Example

A sales representative can provide information such as:

```text
Acme Corp is evaluating our product. Sarah, the CFO, is the main decision-maker.
Their main objection is that our price is too high. They are also considering CompetitorX.
```

Later, the user can ask:

```text
What do you know about the Acme deal?
```

The agent can use Hindsight recall to provide the remembered deal context.

## Testing

The application was tested locally through the Streamlit interface.

Recommended final demonstration:

1. Enter a deal detail.
2. Ask a follow-up question about that detail.
3. Add another important deal detail.
4. Ask the agent to recall it.
5. Restart the application.
6. Ask again to demonstrate persistent Hindsight memory.

## Security

API keys are loaded from environment variables.

Do not upload:

- `.env`
- API keys
- passwords
- private customer data
- confidential company information

Use synthetic data for public demonstrations unless you have permission to publish real data.

## Future Improvements

Potential extensions include:

- Structured deal profiles
- Automatic extraction of customer, stakeholder, objection, competitor and next-action fields
- Deal-stage tracking
- ROI and pricing analysis
- Memory confidence/source display
- CRM integration
- Human approval before external actions

## Hackathon Alignment

The project is designed around persistent agent memory: Hindsight is used as the memory layer so that the agent can recall prior deal context and improve the usefulness of later responses.

The official challenge emphasizes making memory central to the agent and demonstrating improvement over multiple interactions.
