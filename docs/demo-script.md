# 3-Minute Demo Script

## 0:00–0:30 — Introduction

"Hi, I'm [YOUR NAME]. I built a Deal Intelligence Agent that uses Hindsight memory to help sales representatives remember important deal context across conversations."

Show the Streamlit application.

## 0:30–1:00 — The problem

"Sales teams repeatedly revisit previous conversations to remember objections, competitors, stakeholders and pricing concerns. A normal stateless chatbot may not remember this context in a later interaction."

Explain that this project uses Hindsight as persistent memory.

## 1:00–2:15 — Live demonstration

Enter:

"Acme Corp is evaluating our product. Sarah, the CFO, is the primary decision-maker. Their main objection is that our price is too high, and they are considering CompetitorX."

Then ask:

"What do you know about the Acme deal?"

Show that the agent recalls:

- Acme Corp
- Sarah / CFO
- pricing objection
- CompetitorX
- deal status

Add another memory:

"Sarah said they need an ROI analysis before making a decision."

Ask:

"What does Sarah need before making a decision?"

Show the answer.

For the strongest memory demonstration, restart the application and ask the same question again.

## 2:15–2:45 — Explain the architecture

Show the architecture diagram.

Explain:

"Before the LLM responds, the application recalls relevant memories from Hindsight. The recalled information is inserted into the LLM context. New deal information is then retained in Hindsight for future conversations."

## 2:45–3:00 — Conclusion

"The key point is that the agent is not only generating responses. It can use persistent memory to recover relevant deal context from previous interactions."
