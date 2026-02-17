# AI Chat Assistant - Design Specifications

## Design System

### Color Palette

```
Primary Colors:
- Primary Purple: #667eea
- Primary Dark Purple: #764ba2
- Gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%)

Semantic Colors:
- Success Green: #10b981, #4ade80
- Info Blue: #3b82f6, #dbeafe
- Warning Yellow: #f59e0b, #fef3c7
- Error Red: #ef4444, #fee2e2

Neutral Colors:
- White: #ffffff
- Gray 50: #f9fafb
- Gray 200: #e5e7eb
- Gray 300: #d1d5db
- Gray 400: #9ca3af
- Gray 900: #1f2937
- Black: #000000
```

### Typography

```
Font Family:
- Primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif

Font Sizes:
- XS: 11px (timestamps, metadata)
- SM: 13px (quick actions, status)
- Base: 14px (messages, input)
- LG: 18px (agent name)
- XL: 24px (avatars, icons)

Font Weights:
- Normal: 400
- Semibold: 600
```

### Spacing Scale

```
- XS: 4px
- SM: 8px
- MD: 12px
- LG: 16px
- XL: 20px
- 2XL: 24px
```

### Border Radius

```
- Small: 8px (feedback buttons)
- Medium: 12px (system messages)
- Large: 18px-20px (message bubbles, input)
- Full: 50% (avatars, send button)
```

## Component Specifications

### 1. Chat Container
```css
Dimensions: 800px max-width, 90vh height
Background: White
Border Radius: 20px
Shadow: 0 20px 60px rgba(0, 0, 0, 0.3)
```

### 2. Chat Header
```
Height: Auto (content-based, ~90px)
Background: Primary gradient
Padding: 20px
Elements:
  - Avatar (50x50px, circle)
  - Agent name (18px, semibold)
  - Status indicator (8px pulsing dot)
  - Status text (13px)
```

### 3. Message Bubbles

**AI Messages:**
```css
Background: White
Border: 1px solid #e5e7eb
Color: #1f2937
Max-width: 70%
Padding: 12px 16px
Border-radius: 18px (bottom-left: 4px)
Alignment: Left
```

**User Messages:**
```css
Background: Primary gradient
Color: White
Max-width: 70%
Padding: 12px 16px
Border-radius: 18px (bottom-right: 4px)
Alignment: Right
```

**Human Agent Messages:**
```css
Background: #dbeafe
Border: 1px solid #3b82f6
Color: #1e40af
Max-width: 70%
Padding: 12px 16px
Border-radius: 18px (bottom-left: 4px)
Alignment: Left
```

**System Messages:**
```css
Background: #fef3c7
Border: 1px solid #fde047
Color: #92400e
Max-width: 85%
Padding: 12px 16px
Border-radius: 12px
Alignment: Center
Font-size: 13px
```

### 4. Typing Indicator
```
Dimensions: Auto-width, fits content
Background: White
Border: 1px solid #e5e7eb
Padding: 12px 16px
Dots: 3 × 8px circles
Animation: Bounce effect with 0.2s delay between dots
```

### 5. Quick Action Buttons
```css
Height: Auto
Padding: 8px 16px
Background: White
Border: 1px solid #667eea
Color: #667eea
Border-radius: 20px
Font-size: 13px
Hover State: Background → #667eea, Color → White
```

### 6. Chat Input
```css
Height: Auto (~45px)
Padding: 12px 16px
Border: 1px solid #e5e7eb
Border-radius: 24px
Font-size: 14px
Focus State: Border-color → #667eea
```

### 7. Send Button
```css
Dimensions: 45px × 45px
Background: Primary gradient
Color: White
Border-radius: 50%
Icon: ➤ (18px)
Hover State: Scale 1.05
Disabled State: Opacity 0.5
```

### 8. Handoff Banner
```css
Background: #dbeafe
Border-left: 4px solid #3b82f6
Color: #1e40af
Padding: 12px 20px
Margin: 0 20px 16px
Border-radius: 8px
Font-size: 14px
Initial State: display: none
Active State: display: block with slide-in animation
```

### 9. Feedback Buttons
```css
Padding: 4px 8px
Font-size: 11px
Background: #f3f4f6
Border: 1px solid #e5e7eb
Border-radius: 8px
Hover State: Background → #e5e7eb
```

## Animations

### Slide In (Messages)
```css
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
Duration: 0.3s
Easing: ease-out
```

### Pulse (Status Indicator)
```css
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}
Duration: 2s
Repeat: infinite
```

### Typing (Dots)
```css
@keyframes typing {
    0%, 60%, 100% { transform: translateY(0); }
    30% { transform: translateY(-10px); }
}
Duration: 1.4s
Delay: 0.2s between dots
Repeat: infinite
```

### Button Hover
```css
Transform: scale(1.05)
Duration: 0.2s
Easing: ease
```

## Interactive States

### Message States
1. **Sending** - Appears on user's side immediately
2. **Delivered** - Timestamp appears
3. **Bot Typing** - Animated typing indicator shows
4. **Bot Response** - Message appears with slide-in animation

### Agent States
1. **AI Mode**
   - Avatar: 🤖
   - Name: "AI Assistant"
   - Status: "Always here to help"
   - Quick actions: Visible

2. **Handoff Mode**
   - System message appears
   - Handoff banner shows
   - Header updates in progress

3. **Human Agent Mode**
   - Avatar: 👤
   - Name: "Agent Name"
   - Status: "Online"
   - Quick actions: Hidden
   - Message color changes to blue theme

## Responsive Behavior

### Desktop (> 768px)
```
Container: 800px max-width
Message bubbles: 70% max-width
Padding: 20px
```

### Tablet (481px - 768px)
```
Container: 100% width
Message bubbles: 75% max-width
Padding: 16px
```

### Mobile (< 480px)
```
Container: 100% width
Message bubbles: 85% max-width
Padding: 12px
Header: Compact layout
Font sizes: Slightly reduced
```

## Accessibility Features

### Keyboard Navigation
- Tab through interactive elements
- Enter to send message
- Escape to close quick actions (if implemented)

### Screen Reader Support
```html
- ARIA labels on buttons
- Alt text on avatars
- Role="log" for chat messages
- Live regions for dynamic updates
```

### Color Contrast
- All text meets WCAG AA standards (4.5:1 minimum)
- Focus indicators visible on all interactive elements

### Focus States
```css
All interactive elements:
- Outline: 2px solid #667eea
- Outline-offset: 2px
```

## User Experience Flows

### Happy Path (AI Resolution)
1. User opens chat → Greeting appears (0.5s delay)
2. User sees quick actions (1.5s delay)
3. User types or clicks quick action
4. Typing indicator shows (1-2s)
5. AI responds with helpful answer
6. Feedback buttons appear
7. User clicks "Helpful" or continues conversation

### Handoff Path
1. User requests human or AI detects need
2. AI confirms: "Let me connect you..." (immediate)
3. System message: "Transferring..." (0.3s delay)
4. Header animates to human agent (smooth transition)
5. Handoff banner appears
6. Quick actions hide
7. Human agent message: "Hi, I'm [Name]..." (2s delay)
8. Conversation continues with human

### Error States
1. **Network Error**: Banner shows "Connection lost. Trying to reconnect..."
2. **No Agents Available**: "All agents are busy. Estimated wait: X minutes"
3. **Message Failed**: Retry button appears next to failed message

## Testing Scenarios

### Scenario 1: Quick Resolution
```
User: "How do I reset my password?"
Expected: AI provides step-by-step instructions
Metric: < 2s response time
```

### Scenario 2: Handoff Trigger
```
User: "I want to talk to a human"
Expected: Handoff banner + system message + UI update
Metric: < 1s for UI response
```

### Scenario 3: Progressive Escalation
```
User: Asks question → AI answers → "That didn't work" → AI tries again → "Still broken"
Expected: After 3rd attempt, AI offers human agent
Metric: Track attempt counter
```

### Scenario 4: Quick Action
```
User: Clicks "Human Agent" button
Expected: Pre-fills message and triggers handoff flow
Metric: Same as Scenario 2
```

## Future Enhancements

### Phase 2 Features
- [ ] File upload support
- [ ] Voice message integration
- [ ] Video call capability
- [ ] Co-browsing for complex issues
- [ ] Multilingual support
- [ ] Sentiment analysis with real-time mood detection
- [ ] Proactive suggestions based on user behavior
- [ ] Rich media responses (images, carousels, cards)

### Analytics Dashboard
- Conversation transcripts
- Handoff reasons and frequency
- Resolution time metrics
- User satisfaction scores
- Agent performance metrics
- Popular topics and questions

### Advanced AI Features
- Context retention across sessions
- Personalized greetings for returning users
- Predictive handoff (before user requests)
- Smart routing to specialized agents
- Auto-suggestions while typing

## Technical Implementation Notes

### Key JavaScript Functions
```javascript
- sendMessage(): Handles user message submission
- addMessage(): Appends new message to chat
- showTypingIndicator(): Displays typing animation
- getBotResponse(): Determines AI response logic
- handoffToHuman(): Manages agent handoff process
- scrollToBottom(): Auto-scrolls to latest message
```

### State Management
```javascript
- isHumanAgent: boolean (tracks current agent type)
- conversation: array (stores full chat history)
- messageQueue: array (handles message ordering)
```

### Event Handlers
```javascript
- onkeypress: Enter key sends message
- onclick: Button clicks and quick actions
- onfocus: Input focus state
- onblur: Input blur state
```

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile Safari iOS 14+
- Chrome Android 90+
