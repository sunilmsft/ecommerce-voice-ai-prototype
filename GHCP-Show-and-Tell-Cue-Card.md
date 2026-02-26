# GHCP Show & Tell — Presenter Cue Card (10 Minutes)
## "PM as Builder: How I Used GitHub Copilot to Ship a Production-Quality Prototype in 10 Days"

---

## Pre-Demo Checklist
- [ ] Open **Microsoft Edge** (Neural voices only work properly in Edge)
- [ ] Pre-load GitHub Pages: `https://sunilmsft.github.io/ecommerce-voice-ai-prototype/`
- [ ] Navigate to **original-prototype.html** and let page fully load (voices cache on first load)
- [ ] Test speakers — make sure audio is unmuted and volume is up
- [ ] Open VS Code with the repo `C:\Users\sunilve\ecommerce-voice-ai-prototype`
- [ ] Have a terminal tab ready with `git log --oneline` output visible (89 commits)
- [ ] Close Outlook/Teams notifications to avoid interruptions during voice demo

---

## 0:00–1:00 | THE HOOK — Lead with the Punchline

**SAY:**
> "I shipped a production-quality interactive prototype — 30,000 lines of code across 8 working variants — in 10 days. I'm a PM. I don't write code. GitHub Copilot does."

**SHOW:** GitHub Pages landing page briefly — the grid of prototype cards. Let them see it's real, deployed, live.

**SAY:**
> "Every one of these is a fully interactive prototype with voice AI, real-time speech synthesis, quoting, and warm handoff. All built through conversation with Copilot."

**TRANSITION:** *"Let me tell you why I built this and then show you how."*

---

## 1:00–2:00 | THE WHY — PM Context

**SAY:**
> "Here's the business problem: when customers call our eCommerce line after business hours, they hit a dead end — voicemail or 'call back tomorrow.' We lose the sale."

> "I wanted to pitch an engineering investment for a Voice AI Agent that handles those calls. But engineering won't commit sprint capacity to explore an idea. I needed something tangible."

> "So instead of writing a spec and hoping — I built the prototype myself with Copilot."

**KEY POINT (say clearly):**
> "This flipped the conversation from 'should we explore this?' to 'when can we ship this?'"

---

## 2:00–5:00 | THE BUILD JOURNEY — How I Used Copilot (3 min)

### a) Conversation-Driven Development (1 min)
**SHOW:** VS Code with Copilot Chat panel open.

**SAY:**
> "I describe the experience I want in plain English — like I'm writing a user story — and Copilot writes the implementation. I'm not debugging semicolons. I'm designing the customer experience and Copilot translates it to code."

> "For example: I said 'add a follow-up question where the AI asks if there's anything else before wrapping up' — and it generated the voice flow, the timing, the transcript sync, everything."

### b) Iteration Velocity (1 min)
**SHOW:** Terminal with `git log --oneline` — scroll through the 89 commits.

**SAY:**
> "89 commits in 10 days. That's not a typo. I found a bug during a live demo — the AI and the customer were using the same voice, which was confusing. I described it to Copilot. It audited all 9 prototype files, identified where the voices overlapped, assigned distinct Neural voices to each speaker, added pitch and rate differentiation, and fixed it across every file in one commit."

> "Bug found to bug fixed to deployed — in minutes, not sprints."

**COMMIT TO REFERENCE:** `8656ab9` (voice overlap fix)

### c) System-Level Awareness (1 min)
**SHOW:** Briefly show the file explorer with 8 HTML files.

**SAY:**
> "Copilot isn't just autocomplete. When I renamed 'Sales AI Assistant' to 'Ask Microsoft Voice Agent,' it found and replaced every reference across 8 files — titles, headers, voice prompts, alt text — in one operation. It understands the codebase as a system, not just the line you're on."

**COMMIT TO REFERENCE:** `148fd29` (mass rename)

**TRANSITION:** *"But the best way to show you is to experience it. Let me run the prototype."*

---

## 5:00–9:00 | LIVE DEMO — The Prototype in Action (4 min)

### Setup (15 sec)
**SHOW:** Navigate to `original-prototype.html` on GitHub Pages.

**SAY:**
> "This is the Assisted Follow-Up variant — the customer starts with a callback request and gets connected to a Voice AI Agent while they wait."

### Demo Flow (rehearse this tight — 3 min 45 sec)

| Step | Action | What to Narrate |
|------|--------|-----------------|
| **1** | Click **"Request a Callback"** | *"Customer arrives after hours, requests a callback."* |
| **2** | Fill form: **Priya Nair**, **priya.nair@fabrikam-example.com**, **Fabrikam** | *"They provide basic info."* |
| **3** | Submit → See callback confirmation | *"Callback is confirmed — but instead of a dead end..."* |
| **4** | Click **"Talk to Ask Microsoft Voice Agent"** | *"...they can immediately talk to our Voice AI Agent."* |
| **5** | **LET THE VOICE PLAY** — AI greets Priya by name | **Pause and let the audience hear it.** This is the wow moment. |
| **6** | Discovery questions play (team size, remote/hybrid, security) | *"The AI is doing real discovery — not a phone tree. It's understanding their business."* |
| **7** | Plan recommendation + pricing | *"It recommends a plan with pricing tailored to what they told us."* |
| **8** | Quote generation + email | *"It generates a personalized quote and emails it — the customer has something concrete in their inbox."* |
| **9** | Follow-up: *"Is there anything else I can help with?"* | *"It asks before wrapping up — natural conversation flow."* |
| **10** | Call ends → **Compact wrap-up screen appears** | *"Look at what the customer sees — clean summary, buttons right there. No scrolling."* |
| **11** | Point out the summary lines | *"Callback submitted. Voice agent duration. Quote emailed. Status: scheduled."* |
| **12** | Click **"Keep My Callback"** | *"They keep the callback, and the specialist gets the full conversation summary and quote — zero repeat."* |

### While Voice Plays — Narrate the Business Value
> "The customer never hit a dead end. They got a plan recommendation, a quote in their inbox, and a warm handoff — all after hours. The specialist gets full context so the customer doesn't repeat themselves. That's the experience gap we're closing."

---

## 9:00–10:00 | TAKEAWAYS — What This Means for PMs

**SAY (pick 3–4 of these — don't rush all of them):**

1. **"Copilot turns PMs into builders."**
   > "You don't need to wait for eng capacity to validate an idea. Build the prototype, bring the evidence."

2. **"Prototypes beat slide decks."**
   > "This got more traction in one live demo than any spec doc would have. People believe what they can experience."

3. **"The iteration speed is the real superpower."**
   > "89 iterations in 10 days. The speed means you test more ideas, catch more edge cases, and arrive at a better product."

4. **"Start with a real scenario, not 'hello world.'"**
   > "The reason this is compelling isn't the JavaScript — it's because it solves a real business problem that our customers face every day."

**CLOSE:**
> "If you have a product idea that's stuck in the 'should we explore this?' phase — don't wait. Build it. Copilot makes that possible for PMs today."

**SHOW:** GitHub Pages URL one more time so people can try it themselves.

---

## Q&A Bridge Lines (if questions come up)

| Question Type | Response |
|---------------|----------|
| "How long did it actually take?" | "10 calendar days, evenings and weekends. 89 commits. About 30K lines of code across 8 prototypes." |
| "Did you write any code yourself?" | "I wrote zero code from scratch. I described what I wanted in natural language. Copilot wrote the code, I validated the experience." |
| "What about bugs?" | "Bugs happened — audio lag, voice overlap, sync issues. But the point is I described the bug to Copilot and it fixed it. The iteration cycle is minutes, not days." |
| "Could this actually ship to production?" | "This is a prototype — it proves the experience concept. Production would need real APIs, auth, telephony integration. But the prototype is what convinced the team to invest." |
| "What languages/frameworks?" | "Pure HTML, CSS, and JavaScript — no frameworks, no build tools. It runs from a single file. Copilot chose simplicity because I described a demo prototype, not a production app." |
| "What model/version of Copilot?" | "GitHub Copilot in VS Code — Agent mode with Claude. I used chat-based conversations, not just inline suggestions." |
| "Is the voice real AI or pre-recorded?" | "It's the browser's built-in speech synthesis API using Microsoft Edge Neural voices. No external AI service — it runs entirely in the browser." |

---

## Numbers to Have Ready

| Metric | Value |
|--------|-------|
| Total commits | 89 |
| Calendar days | 10 (Feb 16–25, 2026) |
| Prototype variants | 8 interactive HTML files |
| Total lines of code | ~30,000 |
| Frameworks used | 0 (pure HTML/CSS/JS) |
| Lines of code written manually | 0 |
| GitHub Pages deployed | Yes — live URL |
| Voice engine | Browser `speechSynthesis` API + Edge Neural voices |

---

## Emergency Fallbacks

| Problem | Fix |
|---------|-----|
| Voice doesn't play | Refresh the page in Edge. If still broken, say "The Neural voices need Edge — let me switch browsers." |
| Audio sounds robotic | You're in Chrome. Switch to Edge. |
| Page loads slowly | Pre-cached version: open `original-prototype.html` locally from `C:\Users\sunilve\ecommerce-voice-ai-prototype\` |
| Demo breaks mid-flow | Say "This is a prototype — bugs are part of the story. Let me show you how fast Copilot fixes them." Open VS Code and show the fix live — that's actually more impressive. |
| Runs over 10 min | Cut the Build Journey section to 1 minute (just show commit log + one example). Spend the time on the live demo — that's what people remember. |
