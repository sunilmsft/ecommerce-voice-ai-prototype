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
