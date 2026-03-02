# PM × Engineering: Roles, Handoffs, and Shipping Faster with GitHub Copilot

## The Opportunity

With PMs now equipped with GitHub Copilot (GHCP) and VS Code, the traditional boundary between "PM defines" and "Engineering builds" is shifting. PMs can go further than specs and mockups — they can produce **functional artifacts** that engineering builds *from*, not *after*.

This creates a real opportunity to ship faster, but only if we draw clear lines. Without them, we get the worst of both worlds: PMs doing engineering work poorly, and engineers re-doing PM work they didn't know existed.

This document proposes a **handoff model** that eliminates that overlap.

---

## The Core Principle

> **PMs should hand off *working proof*, not documentation about what to build.**
> **Engineering should start from *validated artifacts*, not requirements to interpret.**

The goal is to move the handoff point **downstream** — closer to buildable — without asking PMs to write production code or engineers to re-discover product intent.

---

## What Changes with GHCP-Enabled PMs

| Before GHCP | With GHCP |
|-------------|-----------|
| PM writes a spec → Engineering interprets it → builds from scratch | PM builds a functional prototype → Engineering refactors it into production |
| PM describes user flows in docs → Engineers guess at edge cases | PM produces interactive flows with real branching logic → Engineers see every path |
| PM creates wireframes → Engineering builds UI from screenshots | PM delivers working HTML/CSS → Engineering lifts the validated UI directly |
| Handoff is a meeting + a doc | Handoff is a repo + a working demo |
| 2–3 rounds of "that's not what I meant" | What you see is what was meant |

---

## The Handoff Model: "Prototype-Forward"

### PM Owns (Pre-Handoff)

| Deliverable | What It Looks Like | Why It Matters |
|-------------|-------------------|----------------|
| **Functional Prototype** | Working HTML/JS prototype that demonstrates the experience end-to-end | Engineering sees the *actual* experience, not a description of one |
| **Conversation/Flow Scripts** | Real scripted interactions with branching logic, edge cases, error states | Eliminates "what happens when…?" back-and-forth |
| **Design Specs as Code** | CSS values, component structure, responsive behavior — in the prototype itself | Engineers extract values directly instead of translating a Figma file |
| **User Flow Diagrams** | Mermaid or equivalent diagrams showing decision trees and state transitions | Engineers see the architecture before writing a line of code |
| **Demo-Ready Scenario** | A prototype that can be shown to stakeholders *before* engineering starts | Validates direction early; kills bad ideas before they consume sprint cycles |

### The Handoff Moment

The PM hands off when:

1. ✅ A stakeholder has **seen the prototype** and confirmed direction
2. ✅ The prototype covers **the primary flow and at least 2 edge cases**
3. ✅ The artifacts are **in a repo** (not a slide deck, not an email attachment)
4. ✅ Engineering can **open the prototype in a browser** and interact with it

The handoff is not a meeting. It's a **pull request** or a **repo link** with a README.

### Engineering Owns (Post-Handoff)

| Responsibility | What It Looks Like |
|---------------|-------------------|
| **Architecture & Systems Design** | Decompose the prototype experience into services, APIs, data models |
| **Production Code** | Rebuild the prototype logic in the production stack (React, backend services, etc.) |
| **Performance, Scale, Security** | Everything the prototype intentionally ignores |
| **API Integration** | Replace simulated data/calls with real service integrations |
| **Testing & CI/CD** | Unit tests, integration tests, deployment pipelines |
| **Tech Debt & Maintainability** | Code quality, documentation, monitoring |

### What Engineering Should NOT Do

- ❌ Re-discover product requirements from scratch
- ❌ Redesign the UX that was already validated in the prototype
- ❌ Build a competing prototype to "explore the space"
- ❌ Wait for a spec doc when a working prototype exists

### What PMs Should NOT Do

- ❌ Write production-quality code or attempt to deploy to production
- ❌ Make architectural decisions (database choices, service boundaries, auth patterns)
- ❌ Optimize for performance or scale in the prototype
- ❌ Block engineering from improving the UX based on technical constraints

---

## What This Looks Like in Practice

Here are concrete examples of what a PM prototype defines — and what engineering takes from there.

### Example 1: Click-to-Value — "How many clicks to get help?"

**PM defines in the prototype:**
- Customer lands on the eCommerce page → clicks the voice icon → is speaking with the AI agent. **Two clicks.**
- PM builds this in the prototype and validates: is two clicks the right number? Should the voice icon be persistent or contextual? What happens if the customer clicks it mid-checkout vs. from the homepage?
- The prototype *answers* these questions because stakeholders can click through it themselves.

**What PM hands off:** "The experience is two clicks to voice. Here's the working prototype — try it. The icon is always visible in the bottom-right. It works from any page state."

**What engineering builds:** The production implementation of that same two-click path — real audio capture, real speech-to-text, real routing — but they're not debating *whether* it should be two clicks or where the icon goes. That's settled.

### Example 2: Cross-Surface Consistency — "Handoff should feel the same everywhere"

**The problem PMs solve in the prototype:**
A customer who starts in **chat** and switches to **voice** should have the same handoff warmth as a customer who started in **voice** from the beginning. And when either of them gets transferred to a **human specialist**, that transition should feel seamless — not like starting over.

**PM defines in the prototype:**
- Chat → Voice: *"I can see you've been chatting about Microsoft 365 plans for your agency — let me pick up right where you left off."* Customer never repeats themselves.
- Voice → Human specialist: *"I'm transferring you now. They'll have the full context of our conversation."* No hold music, no queue theater — just a warm introduction.
- After-hours → Callback: *"Once you disconnect, I'll bring up the callback form so you can choose a time."* The form is pre-populated with everything from the conversation.

**What PM hands off:** Three working flows that demonstrate the *exact words*, *exact transitions*, and *exact UI state changes* for every modality switch. Engineering doesn't have to guess what "seamless" means — they can see it, hear it, click through it.

**What engineering builds:** The real-time context passing (conversation state, customer profile, quote data) that makes those transitions actually work at scale. The PM showed *what* seamless looks like; engineering makes it *real*.

### Example 3: Interaction Depth — "The AI should ask follow-up questions, not just answer"

**PM defines in the prototype:**
- Instead of jumping straight to a plan recommendation, the AI asks three discovery questions:
  1. *"Are your teams mostly in-office, fully remote, or hybrid?"*
  2. *"Are devices mostly company-managed, or do people also use personal devices?"*
  3. *"What decision timeline are you working toward?"*
- Only after those three responses does the AI make a tailored recommendation.
- PM scripts the actual dialogue, with different customer responses, and builds all of it into the prototype so stakeholders can hear the pacing and judge whether it feels natural or robotic.

**What PM hands off:** The validated conversation tree — every question, every branch, every response — as working code in the prototype. Not a flowchart. Not a table of intents. A playable conversation.

**What engineering builds:** The NLU pipeline, intent classification, and dynamic response generation that makes this work with *real* customer input instead of scripted responses. But they're building toward a known-good experience, not inventing the conversation design from scratch.

### Example 4: Quoting Experience — "Generate a quote without friction"

**PM defines in the prototype:**
- Three quoting scenarios built and testable:
  - **Happy path:** Customer shares email → quote generated → sent instantly → *"It's in your inbox, valid for 30 days."*
  - **Email later:** Customer declines to share email → quote is staged → *"We'll send it along when you share your email on the callback form."*
  - **No quote:** Customer skips quoting entirely → conversation continues without friction.
- PM validates that in *every* scenario, the customer is never more than **one question away** from moving forward. No forms, no redirects, no "let me transfer you to someone who can do that."

**What PM hands off:** Three working quoting flows with the exact UX for each. Engineering can see that the quote generation feels instant (no loading spinner, no wait state), that the email prompt is a single conversational question (not a form field), and that declining is genuinely friction-free.

**What engineering builds:** The actual QuoteX API integration, email delivery pipeline, and quote persistence layer. But the *experience contract* is locked: one question to generate, instant confirmation, no dead ends.

### Why Examples Matter

These aren't edge cases — they're the *core* of what customers experience. And they're exactly the kind of details that get lost in a spec document:

| In a Spec | In a Prototype |
|-----------|---------------|
| "The handoff should be seamless" | You can *hear* the AI say "They'll have full context" and watch the specialist appear with the conversation summary |
| "The quoting flow should be simple" | You can *click through* three scenarios and count the interactions: one question, one confirmation, done |
| "The voice agent should feel natural" | You can *listen* to the pacing of three discovery questions and judge whether it sounds like a conversation or an interrogation |
| "Consistent across modalities" | You can *switch* from chat to voice to human handoff and verify the experience yourself |

**The prototype makes the abstract concrete.** That's what eliminates the back-and-forth between PM and Engineering — and that's what ships faster.

---

## Why This Ships Faster

| Traditional Flow | Prototype-Forward Flow |
|-----------------|----------------------|
| Spec (2 weeks) → Design review (1 week) → Engineering ramp (1 week) → Build (4 weeks) → "That's not what I meant" (2 weeks) | Prototype (1 week) → Stakeholder validation (2 days) → Engineering builds from prototype (3 weeks) |
| **~10 weeks** | **~5 weeks** |

The speed gain comes from three places:

1. **Eliminating interpretation gaps** — Engineers see the experience, they don't read about it
2. **Front-loading validation** — Stakeholders react to something real before engineering starts
3. **Reusable artifacts** — CSS, flow logic, and UI patterns transfer directly from prototype to production

---

## Making It Consistent Across Teams

For this to work at scale, every PM–Engineering handoff should include the same artifact set:

### The Handoff Checklist

```
□ Functional prototype (HTML/JS, in a repo)
□ README explaining how to run it and what scenarios it covers
□ User flow diagrams (Mermaid or equivalent)
□ Design specs embedded in the prototype (not a separate doc)
□ At least one stakeholder demo completed with sign-off
□ Known limitations listed (what the prototype fakes/skips)
□ Open questions for engineering flagged explicitly
```

If a PM can check these boxes, engineering has everything they need to start building — no ambiguity, no ramp-up time, no "let me set up a meeting to walk you through the vision."

---

## What Leadership Should Reinforce

1. **PMs should be measured on prototype quality, not spec length.** A 50-page PRD that nobody reads is less valuable than a working prototype that everyone can interact with.

2. **Engineering should treat PM prototypes as the source of truth for *intent*.** Not for architecture, not for code quality — but for "what are we building and why."

3. **The handoff is a repo, not a meeting.** If it can't be cloned and run, it's not ready to hand off.

4. **Invest in PM fluency with GHCP and VS Code.** The ROI is not "PMs who can code" — it's "PMs who can ship validated proof before engineering writes line one."

5. **Protect the boundary.** PMs go further downstream, but they stop at the prototype. Engineers start from the prototype, but they don't re-litigate product decisions. The line is clear: **PMs own the *what and why*. Engineering owns the *how*.** GHCP just lets PMs express the *what* in a form that's closer to the *how*.

---

## One-Line Summary

> Give engineering a working demo to build from — not a document to interpret. That's how you ship faster.
