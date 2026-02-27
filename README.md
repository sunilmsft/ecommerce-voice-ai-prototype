# Ask Microsoft Voice AI Agent — eCommerce Prototype

An interactive prototype demonstrating an AI-powered voice and chat assistant for Microsoft eCommerce. Built to explore how customers could get help with Microsoft 365 licensing through natural voice conversations, intelligent chat, and seamless handoff to human specialists.

> **Live demo:** [sunilmsft.github.io/ecommerce-voice-ai-prototype](https://sunilmsft.github.io/ecommerce-voice-ai-prototype/)

---

## What This Is

This is a **design prototype** (not production code) that simulates end-to-end customer journeys for an AI-powered sales assistant on Microsoft's eCommerce platform. It covers:

- **Voice-first conversations** — customers call and speak directly with an AI voice agent
- **Chat-to-voice modality switching** — start in chat, seamlessly switch to voice mid-conversation
- **Callback scheduling** — after-hours flows with form submission and follow-up
- **Live specialist handoff** — warm transfer to a human agent with full conversation context
- **Personalized quoting** — AI generates and emails tailored pricing quotes via QuoteX API

## Prototype Variants

| File | Description |
|------|-------------|
| [`voice-enabled/index.html`](voice-enabled/index.html) | **Primary demo** — Full voice-enabled prototype with Azure Speech SDK, modality switching, quoting flows, and live handoff |
| [`voice-enabled/classic.html`](voice-enabled/classic.html) | Voice-enabled variant with classic layout |
| [`original-prototype.html`](original-prototype.html) | Original chat + voice prototype |
| [`.eCommerce Voice AI Agent prototype.html`](.eCommerce%20Voice%20AI%20Agent%20prototype.html) | eCommerce-branded variant |
| [`.Hybrid - ai-chat-assistant-prototype.html`](.Hybrid%20-%20ai-chat-assistant-prototype.html) | Hybrid AI + human-first approach |
| [`.Opt#1- ai-chat-assistant-prototype-human-first.html`](.Opt%231-%20ai-chat-assistant-prototype-human-first.html) | Human-first assist model |
| [`.Opt#2 - AI-First Assist.html`](.Opt%232%20-%20AI-First%20Assist.html) | AI-first assist model |

## Key Features Demonstrated

- **Azure Speech Services** integration for text-to-speech voice output
- **Context carryover** between chat and voice modalities — no repeating yourself
- **Business hours detection** with different flows for during/after hours
- **Warm handoff** to live specialists with full conversation summary
- **Behind-the-scenes annotations** showing AI capabilities in real time (intent detection, quote generation, context passing)
- **Callback form** with pre-populated fields from conversation context
- **Interactive quoting** with three scenarios: happy path, email-later, and no-quote

## How to Run

1. **Online:** Visit [the GitHub Pages site](https://sunilmsft.github.io/ecommerce-voice-ai-prototype/)
2. **Locally:** Open any `.html` file directly in a browser (Chrome or Edge recommended for speech synthesis)

No build step, no dependencies, no server required — each file is a self-contained single-page prototype.

## Documentation

| File | Contents |
|------|----------|
| [AI-Chat-Prototype-README.md](AI-Chat-Prototype-README.md) | Detailed prototype documentation and usage guide |
| [ai-chat-design-specs.md](ai-chat-design-specs.md) | Design system — colors, typography, components, CSS specs |
| [ai-chat-user-flows.md](ai-chat-user-flows.md) | User flow diagrams (Mermaid) and branching logic |
| [AI-Voice-Assistant-Update-Summary.md](AI-Voice-Assistant-Update-Summary.md) | Voice assistant feature changelog |

## Tech Stack

- **HTML/CSS/JavaScript** — single-file prototypes, no frameworks
- **Azure Cognitive Services Speech SDK** — voice synthesis (voice-enabled variants)
- **GitHub Pages** — hosting

## Demo Tips

- Use the **variant switcher** (top of voice-enabled prototype) to toggle between Voice-First and Modality Switch flows
- Use the **quote scenario selector** to demo happy path, email-later, or no-quote flows
- Use the **business hours toggle** to switch between during-hours (live handoff) and after-hours (callback) experiences
- Watch the **call transcript panel** for behind-the-scenes system annotations showing AI capabilities

---

*Built for the Microsoft eCommerce AI experience exploration.*
