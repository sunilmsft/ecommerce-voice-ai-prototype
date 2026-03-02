# PM × Engineering: Roles, Handshakes, and Shipping Faster with GitHub Copilot

## The Opportunity

With PMs now equipped with GitHub Copilot (GHCP) and VS Code, the traditional boundary between "PM defines" and "Engineering builds" is shifting. PMs can go further than specs and mockups — they can produce **functional artifacts** that engineering builds *from*, not *after*.

This creates a real opportunity to ship faster — especially when both sides have a shared understanding of where each role adds the most value. When PMs and Engineering are aligned on who does what, the overlap shrinks and the momentum compounds.

This document proposes a **handshake model** that makes that collaboration intentional.

---

## The Core Principle

> **PMs should deliver *working proof*, not documentation about what to build.**
> **Engineering should start from *validated artifacts*, not requirements to interpret.**

The goal is to move the handshake point **downstream** — closer to buildable — without asking PMs to write production code or engineers to re-discover product intent.

---

## What Changes with GHCP-Enabled PMs

| Before GHCP | With GHCP |
|-------------|-----------|
| PM writes a spec → Engineering interprets it → builds from scratch | PM builds a functional prototype → Engineering refactors it into production |
| PM describes user flows in docs → Engineers guess at edge cases | PM produces interactive flows with real branching logic → Engineers see every path |
| PM creates wireframes → Engineering builds UI from screenshots | PM delivers working HTML/CSS → Engineering lifts the validated UI directly |
| The handshake is a meeting + a doc | The handshake is a repo + a working demo |
| 2–3 rounds of "that's not what I meant" | What you see is what was meant |

---

## The Handshake Model: "Prototype-Forward"

### PM Owns (Pre-Handshake)

| Deliverable | What It Looks Like | Why It Matters |
|-------------|-------------------|----------------|
| **Functional Prototype** | Working HTML/JS prototype that demonstrates the experience end-to-end | Engineering sees the *actual* experience, not a description of one |
| **Conversation/Flow Scripts** | Real scripted interactions with branching logic, edge cases, error states | Gives engineering a clear picture of every path upfront |
| **Design Specs as Code** | CSS values, component structure, responsive behavior — in the prototype itself | Engineers extract values directly instead of translating a Figma file |
| **User Flow Diagrams** | Mermaid or equivalent diagrams showing decision trees and state transitions | Engineers see the architecture before writing a line of code |
| **Demo-Ready Scenario** | A prototype that can be shown to stakeholders *before* engineering starts | Validates direction early so engineering starts with confidence |

### The Handshake Moment

The handshake happens when:

1. ✅ A stakeholder has **seen the prototype** and confirmed direction
2. ✅ The prototype covers **the primary flow and at least 2 edge cases**
3. ✅ The artifacts are **in a repo** (not a slide deck, not an email attachment)
4. ✅ Engineering can **open the prototype in a browser** and interact with it

The handshake is not a meeting. It's a **pull request** or a **repo link** with a README.

### Engineering Owns (Post-Handshake)

| Responsibility | What It Looks Like |
|---------------|-------------------|
| **Architecture & Systems Design** | Decompose the prototype experience into services, APIs, data models |
| **Production Code** | Rebuild the prototype logic in the production stack (React, backend services, etc.) |
| **Performance, Scale, Security** | Everything the prototype intentionally ignores |
| **API Integration** | Replace simulated data/calls with real service integrations |
| **Testing & CI/CD** | Unit tests, integration tests, deployment pipelines |
| **Tech Debt & Maintainability** | Code quality, documentation, monitoring |

### Where Each Role Adds the Most Value

When both sides lean into their strengths, the work moves faster and the quality goes up.

| PM's Sweet Spot | Engineering's Sweet Spot |
|----------------|------------------------|
| Defining the customer experience and validating it in a prototype | Translating that experience into production-grade architecture |
| Scripting conversation flows, edge cases, and branching logic | Building the NLU, APIs, and services that make it real |
| Embedding design specs (CSS, layout, responsive behavior) in the prototype | Lifting those specs into the production component library |
| Getting stakeholder sign-off before engineering ramps | Making architecture and infrastructure decisions |
| Flagging open questions and known limitations | Solving for performance, scale, and security |

---

## What This Looks Like in Practice

Here are concrete examples of what a PM prototype defines — and what engineering takes from there.

### Example 1: Click-to-Value — "How many clicks to get help?"

**PM defines in the prototype:**
- Customer lands on the eCommerce page → clicks the voice icon → is speaking with the AI agent. **Two clicks.**
- PM builds this in the prototype and validates: is two clicks the right number? Should the voice icon be persistent or contextual? What happens if the customer clicks it mid-checkout vs. from the homepage?
- The prototype *answers* these questions because stakeholders can click through it themselves.

**What PM delivers:** "The experience is two clicks to voice. Here's the working prototype — try it. The icon is always visible in the bottom-right. It works from any page state."

**What engineering builds:** The production implementation of that same two-click path — real audio capture, real speech-to-text, real routing — with the experience already validated, so the team can focus entirely on making it production-ready.

### Example 2: Cross-Surface Consistency — "The experience should feel the same everywhere"

**The problem PMs solve in the prototype:**
A customer who starts in **chat** and switches to **voice** should have the same warm transition as a customer who started in **voice** from the beginning. And when either of them gets transferred to a **human specialist**, that transition should feel seamless — not like starting over.

**PM defines in the prototype:**
- Chat → Voice: *"I can see you've been chatting about Microsoft 365 plans for your agency — let me pick up right where you left off."* Customer never repeats themselves.
- Voice → Human specialist: *"I'm transferring you now. They'll have the full context of our conversation."* No hold music, no queue theater — just a warm introduction.
- After-hours → Callback: *"Once you disconnect, I'll bring up the callback form so you can choose a time."* The form is pre-populated with everything from the conversation.

**What PM delivers:** Three working flows that demonstrate the *exact words*, *exact transitions*, and *exact UI state changes* for every modality switch. Engineering doesn't have to guess what "seamless" means — they can see it, hear it, click through it.

**What engineering builds:** The real-time context passing (conversation state, customer profile, quote data) that makes those transitions actually work at scale. The PM showed *what* seamless looks like; engineering makes it *real*.

### Example 3: Interaction Depth — "The AI should ask follow-up questions, not just answer"

**PM defines in the prototype:**
- Instead of jumping straight to a plan recommendation, the AI asks three discovery questions:
  1. *"Are your teams mostly in-office, fully remote, or hybrid?"*
  2. *"Are devices mostly company-managed, or do people also use personal devices?"*
  3. *"What decision timeline are you working toward?"*
- Only after those three responses does the AI make a tailored recommendation.
- PM scripts the actual dialogue, with different customer responses, and builds all of it into the prototype so stakeholders can hear the pacing and judge whether it feels natural or robotic.

**What PM delivers:** The validated conversation tree — every question, every branch, every response — as working code in the prototype. Not a flowchart. Not a table of intents. A playable conversation.

**What engineering builds:** The NLU pipeline, intent classification, and dynamic response generation that makes this work with *real* customer input instead of scripted responses. They're building toward a known-good experience — the conversation design is already there to build on.

### Example 4: Quoting Experience — "Generate a quote without friction"

**PM defines in the prototype:**
- Three quoting scenarios built and testable:
  - **Happy path:** Customer shares email → quote generated → sent instantly → *"It's in your inbox, valid for 30 days."*
  - **Email later:** Customer declines to share email → quote is staged → *"We'll send it along when you share your email on the callback form."*
  - **No quote:** Customer skips quoting entirely → conversation continues without friction.
- PM validates that in *every* scenario, the customer is never more than **one question away** from moving forward. No forms, no redirects, no "let me transfer you to someone who can do that."

**What PM delivers:** Three working quoting flows with the exact UX for each. Engineering can see that the quote generation feels instant (no loading spinner, no wait state), that the email prompt is a single conversational question (not a form field), and that declining is genuinely friction-free.

**What engineering builds:** The actual QuoteX API integration, email delivery pipeline, and quote persistence layer. But the *experience contract* is locked: one question to generate, instant confirmation, no dead ends.

### Why Examples Matter

These aren't edge cases — they're the *core* of what customers experience. And they're exactly the kind of details that get lost in a spec document:

| In a Spec | In a Prototype |
|-----------|---------------|
| "The transition should be seamless" | You can *hear* the AI say "They'll have full context" and watch the specialist appear with the conversation summary |
| "The quoting flow should be simple" | You can *click through* three scenarios and count the interactions: one question, one confirmation, done |
| "The voice agent should feel natural" | You can *listen* to the pacing of three discovery questions and judge whether it sounds like a conversation or an interrogation |
| "Consistent across modalities" | You can *switch* from chat to voice to human specialist and verify the experience yourself |

**The prototype makes the abstract concrete.** That's what keeps PM and Engineering aligned from the start — and that's what ships faster.

---

## Why This Ships Faster

| Traditional Flow | Prototype-Forward Flow |
|-----------------|----------------------|
| Spec (2 weeks) → Design review (1 week) → Engineering ramp (1 week) → Build (4 weeks) → "That's not what I meant" (2 weeks) | Prototype (1 week) → Stakeholder validation (2 days) → Engineering builds from prototype (3 weeks) |
| **~10 weeks** | **~5 weeks** |

The speed gain comes from three places:

1. **Shared understanding from day one** — Engineers see the experience, they don't read about it
2. **Front-loading validation** — Stakeholders react to something real before engineering starts
3. **Reusable artifacts** — CSS, flow logic, and UI patterns transfer directly from prototype to production

---

## Making It Consistent Across Teams

For this to work at scale, every PM–Engineering handshake should include the same artifact set:

### The Handshake Checklist

```
□ Functional prototype (HTML/JS, in a repo)
□ README explaining how to run it and what scenarios it covers
□ User flow diagrams (Mermaid or equivalent)
□ Design specs embedded in the prototype (not a separate doc)
□ At least one stakeholder demo completed with sign-off
□ Known limitations listed (what the prototype fakes/skips)
□ Open questions for engineering flagged explicitly
```

When these boxes are checked, the team has a shared starting point — engineering can ramp quickly, and both sides are working from the same source of truth.

---

## How Leadership Can Set This Up for Success

1. **Value prototype quality alongside spec quality.** A working prototype that everyone can interact with often communicates more than a lengthy document — and the two can complement each other.

2. **Encourage engineering to build on the PM's prototype as the starting point for *intent*.** Not for architecture, not for code quality — but for "what are we building and why."

3. **Make the handshake a shared artifact.** A repo with a working demo gives both sides a common reference point — something you can point to, run, and iterate on together.

4. **Invest in PM fluency with GHCP and VS Code.** The ROI is not "PMs who can code" — it's PMs who can express product vision in a form that engineering can build on immediately.

5. **Celebrate the overlap, clarify the lanes.** PMs go further downstream with GHCP, and that's a good thing. Engineering builds on that foundation and takes it to production. Both sides benefit: **PMs own the *what and why*. Engineering owns the *how*.** The handshake is where those meet.

---

## One-Line Summary

> When PM and Engineering start from the same working demo, alignment is built in — and that's how you ship faster.
