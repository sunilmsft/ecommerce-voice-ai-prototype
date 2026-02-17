# AI Chat Assistant - User Flows & Branching

## 1. Main Conversation Flow

```mermaid
graph TD
    A[User Opens Chat] --> B[AI Assistant Greeting]
    B --> C{User Input Type}
    C -->|General Question| D[AI Provides Answer]
    C -->|Account Issue| E[AI Troubleshoots]
    C -->|Request Human Agent| F[Handoff Process]
    C -->|Quick Action Button| G[Pre-filled Query]
    
    D --> H{Issue Resolved?}
    E --> H
    G --> D
    
    H -->|Yes| I[User Thanks & Ends]
    H -->|No| J{Escalation Needed?}
    
    J -->|Yes| F
    J -->|No| K[AI Asks Follow-up Questions]
    K --> D
    
    F --> L[Transfer to Human Agent]
    L --> M[Human Agent Responses]
    M --> N[Issue Resolution]
    N --> O[End Conversation]
    
    I --> P[End Session]
    
    style A fill:#667eea,color:#fff
    style F fill:#f59e0b,color:#fff
    style L fill:#3b82f6,color:#fff
    style M fill:#3b82f6,color:#fff
    style P fill:#10b981,color:#fff
    style O fill:#10b981,color:#fff
```

## 2. Human Agent Handoff Decision Tree

```mermaid
graph TD
    A[User Message Received] --> B{Analyze Intent}
    
    B -->|Explicit Request| C[Keywords: human, agent, person, representative]
    B -->|Complex Issue| D[Multiple Failed Attempts]
    B -->|Sensitive Topic| E[Billing, Legal, Complaints]
    B -->|High Priority| F[Urgent, Critical, Emergency]
    
    C --> G[Immediate Handoff]
    D --> H{Attempt Count}
    E --> I{Issue Type}
    F --> G
    
    H -->|>3 Attempts| G
    H -->|<=3 Attempts| J[Continue AI Support]
    
    I -->|Refund Request| G
    I -->|General Billing| K[AI Provides Info]
    I -->|Account Closure| G
    
    K --> L{Satisfied?}
    L -->|No| G
    L -->|Yes| M[Continue AI Chat]
    
    G --> N[Display Handoff Message]
    N --> O[Update UI for Human Agent]
    O --> P[Show Transfer Banner]
    P --> Q[Human Agent Joins]
    
    style G fill:#f59e0b,color:#fff
    style Q fill:#3b82f6,color:#fff
    style M fill:#10b981,color:#fff
```

## 3. User Journey States

```mermaid
stateDiagram-v2
    [*] --> ChatLanding
    ChatLanding --> AIConversation: Start Chat
    
    AIConversation --> AIConversation: AI Responds
    AIConversation --> QuickActions: Use Quick Button
    QuickActions --> AIConversation: Query Sent
    
    AIConversation --> HandoffInitiated: Request Human / Complex Issue
    HandoffInitiated --> AgentQueue: Transfer Process
    AgentQueue --> HumanConversation: Agent Available
    
    HumanConversation --> HumanConversation: Agent Responds
    HumanConversation --> Resolved: Issue Solved
    HumanConversation --> Escalated: Complex Case
    
    AIConversation --> Resolved: Simple Issue Solved
    Resolved --> FeedbackRequest: Ask for Rating
    FeedbackRequest --> ChatEnded: Submit Feedback
    
    Escalated --> FollowUp: Email/Ticket Created
    FollowUp --> [*]
    ChatEnded --> [*]
```

## 4. Detailed Handoff Process Flow

```mermaid
sequenceDiagram
    participant User
    participant ChatUI
    participant AIBot
    participant HandoffSystem
    participant HumanAgent
    
    User->>ChatUI: Types "I need a human agent"
    ChatUI->>AIBot: Send message
    AIBot->>AIBot: Detect handoff trigger
    AIBot->>ChatUI: Display confirmation message
    AIBot->>HandoffSystem: Initiate transfer request
    
    HandoffSystem->>HandoffSystem: Queue user request
    HandoffSystem->>ChatUI: Show "Transferring..." system message
    ChatUI->>ChatUI: Update header (AI → Human)
    ChatUI->>ChatUI: Show handoff banner
    ChatUI->>ChatUI: Hide quick action buttons
    
    HandoffSystem->>HumanAgent: Notify agent with context
    HumanAgent->>HandoffSystem: Accept request
    HandoffSystem->>ChatUI: Update status "Agent connected"
    
    HumanAgent->>ChatUI: Send greeting message
    ChatUI->>User: Display agent message
    User->>ChatUI: Continue conversation
    ChatUI->>HumanAgent: Forward messages
    
    Note over HumanAgent,User: Human-assisted conversation continues
    
    HumanAgent->>ChatUI: Resolution provided
    User->>ChatUI: Thanks & goodbye
    HumanAgent->>ChatUI: Close conversation
    ChatUI->>User: Show feedback request
```

## 5. AI Response Decision Logic

```mermaid
flowchart TD
    A[User Message] --> B[Natural Language Processing]
    B --> C{Message Category}
    
    C -->|FAQ/Common| D[Match Knowledge Base]
    C -->|Account-Specific| E[Check User Context]
    C -->|Unclear/Ambiguous| F[Ask Clarifying Questions]
    C -->|Handoff Request| G[Trigger Handoff]
    
    D --> H{Confidence Score}
    E --> I{Data Available}
    
    H -->|>85%| J[Provide Direct Answer]
    H -->|50-85%| K[Provide Answer + Alternatives]
    H -->|<50%| F
    
    I -->|Yes| L[Personalized Response]
    I -->|No| M[Request Authentication]
    
    J --> N[Add Feedback Buttons]
    K --> N
    L --> N
    M --> O{Authenticated?}
    
    O -->|Yes| E
    O -->|No| P[Generic Guidance]
    
    F --> Q[User Provides Clarification]
    Q --> B
    
    N --> R{User Feedback}
    R -->|Positive| S[Log Success]
    R -->|Negative| T{Auto-Escalate?}
    
    T -->|Yes| G
    T -->|No| U[Offer Alternative Solutions]
    U --> V{Resolved?}
    V -->|No| G
    V -->|Yes| S
    
    style G fill:#f59e0b,color:#fff
    style J fill:#10b981,color:#fff
    style S fill:#10b981,color:#fff
```

## 6. Key Branching Scenarios

### Scenario A: Simple Question (AI Resolves)
1. User: "How do I reset my password?"
2. AI: Provides step-by-step instructions
3. User: "Thanks!"
4. AI: "You're welcome! Anything else?"
5. User: "No, that's all"
6. Chat ends successfully

### Scenario B: Complex Issue (AI → Human)
1. User: "My account was charged twice"
2. AI: "Let me look into billing issues..."
3. AI: Detects sensitive billing topic
4. AI: "I'll connect you with a specialist"
5. **HANDOFF TRIGGERED**
6. Human agent reviews charge
7. Agent processes refund
8. Issue resolved

### Scenario C: Explicit Human Request
1. User: "I want to talk to a person"
2. AI: "I'll connect you right away!"
3. **IMMEDIATE HANDOFF**
4. Human agent greets user
5. Agent assists with inquiry
6. Conversation continues with human

### Scenario D: Progressive Escalation
1. User asks question
2. AI provides answer
3. User: "That didn't work"
4. AI tries alternative solution
5. User: Still not working"
6. AI: After 3 attempts → "Let me connect you with a specialist"
7. **HANDOFF TRIGGERED**

## 7. UI State Changes During Handoff

```mermaid
graph LR
    A[AI Assistant State] -->|Handoff Trigger| B[Transition State]
    B -->|Update UI| C[Human Agent State]
    
    A1[Avatar: 🤖] --> B1[System Message]
    A2[Name: AI Assistant] --> B2[Show Banner]
    A3[Status: Always Available] --> B3[Hide Quick Actions]
    A4[Quick Action Buttons Visible] --> B4[Update Header]
    
    B1 --> C1[Avatar: 👤]
    B2 --> C2[Name: Agent Name]
    B3 --> C3[Status: Online]
    B4 --> C4[Quick Actions Hidden]
    
    style A fill:#667eea,color:#fff
    style B fill:#f59e0b,color:#fff
    style C fill:#3b82f6,color:#fff
```

## 8. Interaction Patterns Summary

| User Action | AI Response | Handoff? | Follow-up |
|-------------|-------------|----------|-----------|
| General question | Direct answer | ❌ No | Ask if helpful |
| Password reset | Instructions | ❌ No | Offer to send link |
| Billing issue | Initial info | ⚠️ Maybe | Escalate if sensitive |
| "Talk to human" | Acknowledge | ✅ Yes | Immediate transfer |
| Technical error | Troubleshoot | ⚠️ Maybe | After 2-3 attempts |
| Account closure | Acknowledge | ✅ Yes | Require human approval |
| Thanks/goodbye | Polite closing | ❌ No | End conversation |
| Frustrated tone | Empathy + options | ⚠️ Maybe | Offer human agent |

## Implementation Notes

1. **Trigger Keywords for Handoff:**
   - Explicit: "human", "agent", "representative", "person", "speak to someone"
   - Implicit: "frustrated", "not working", "still broken", "terrible service"
   - Sentiment: Negative sentiment score < -0.5

2. **Context Preservation:**
   - Full conversation history passed to human agent
   - User information and account details
   - Previous AI attempts and suggested solutions

3. **Response Time Expectations:**
   - AI: < 2 seconds
   - Human agent queue: 30-60 seconds
   - Human agent response: 1-3 minutes

4. **Analytics to Track:**
   - Handoff rate (target: < 15%)
   - AI resolution rate (target: > 85%)
   - User satisfaction scores
   - Average conversation length
   - Time to resolution
