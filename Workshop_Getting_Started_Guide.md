# PM MCP Server Installation Workshop
## Agenda & Presenter Guide

**Date:** [Tomorrow]  
**Duration:** 45-60 minutes  
**Target Audience:** Marketing Engineering PMs  
**Facilitator:** [Your Name]

---

## Pre-Session Checklist

- [ ] All participants have VS Code installed
- [ ] All participants have Node.js installed (verify: `node --version`)
- [ ] GitHub Copilot extension is installed on all machines
- [ ] Projector/screen share is set up
- [ ] PowerPoint or demo environment is ready
- [ ] Print or share the setup guides with participants

---

## Session Flow

### **Part 1: Introduction (5 minutes)**

**What to say:**

"Good morning/afternoon, everyone! Today we're doing something really cool with our development workflow. We're going to set up AI-powered tools that bring your work data directly into VS Code.

**What's an MCP Server?**

Think of MCP—Model Context Protocol—as a universal translator between your tools and AI. Normally, you might:
- Check Azure DevOps for work items
- Check Outlook for emails
- Open files manually
- Copy and paste things around

With MCP servers, you can ask GitHub Copilot to do all that *from inside VS Code*, using natural language.

**Example:**
Instead of 'Let me go check ADO to see the status of my features,' you just ask Copilot in VS Code: 'Show me the status of Feature 12345 in OneITVSO.' Copilot calls the Azure DevOps MCP server and gives you the answer.

**What We're Installing Today:**

We're setting up three MCP servers:
1. **Azure DevOps (ADO)** – Read/update work items, run queries, sync backlogs to Markdown
2. **Work IQ** – Access your Microsoft 365 data (emails, meetings, files) directly from Copilot
3. **MarkItDown** (stretch goal) – Convert PDFs, Word docs, Excel sheets to clean Markdown

By the end of this session, each of you will have a workspace with all three servers running, and you'll know how to use them with Copilot."

---

### **Part 2: The 5-Step Installation Pattern (3 minutes)**

**What to say:**

"All three servers follow the same basic pattern. Once you learn the pattern for ADO, Work IQ and MarkItDown are basically the same process. Here's the pattern:

**Step 1: Verify Prerequisites** – Make sure Node.js and other tools are installed  
**Step 2: Configure the Server** – Ask Copilot to add the server to your `.vscode/mcp.json` file  
**Step 3: Start the Server** – Use the MCP Servers panel in VS Code  
**Step 4: Verify Tools** – Check that Copilot sees the new tools  
**Step 5: Test** – Run a quick test to make sure it works  

We'll follow this same pattern three times today. The nice thing? Once you do it once, you're a pro."

---

### **Part 3: Azure DevOps MCP Server (20-25 minutes)**

#### **Introduction (1 minute)**

"Let's start with Azure DevOps. This server lets Copilot talk to ADO, so you can query and update work items without leaving VS Code."

#### **Live Demo/Walkthrough:**

**Step 1: Verify Prerequisites**

1. Ask the team: "Does everyone have Node.js installed?"
   - Quick verification: Open PowerShell, run `node --version`
   - Should see something like `v20.x.x` or higher

2. Check npm: `npm --version`

3. Point out: "This is the only time we'll need to verify prerequisites. We did this setup in the guides."

**Step 2: Configure the Server**

"Now comes the smart part. We're NOT going to manually edit the JSON file—that's error-prone. Instead, we'll ask GitHub Copilot to do it for us."

1. Demo steps:
   - Open Copilot Chat (`` Ctrl+Alt+I ``)
   - Switch to Agent Mode
   - Copy the ready-made prompt from the ADO_MCP_Setup_Guide.md file
   - Paste and let Copilot create the config

2. **Troubleshooting tip to mention:** "If Copilot doesn't add it correctly, you can ask it again or I can help manually. But 95% of the time, Copilot gets this right."

**Step 3: Start the Server**

1. Demonstrate:
   - Open MCP Servers panel (`` Ctrl+Shift+P `` → "MCP: Focus on MCP Servers View")
   - Find `azureMcpProvider`
   - Click Start
   - Wait a few seconds for it to initialize

2. Explain: "The first time you start it, you might be asked to authenticate with your Microsoft credentials. That's normal and expected. You'll see a browser window—just sign in and grant permissions."

**Step 4: Verify Tools**

1. Show:
   - Open Copilot Chat
   - Click "Refresh Tools" (circular arrow)
   - Should see ADO tools like `mcp_azuremcpprovi_wit_get_work_item`

2. Explain: "These tool names are technical—you don't need to memorize them. Copilot knows what to call."

**Step 5: Test**

1. Run a test:
   ```
   Get work item 12345 from project OneITVSO
   ```
   (Use a real work item ID from your project)

2. Show the result: "This is Copilot calling ADO and returning live data. Pretty cool, right?"

#### **Hands-on Activity (10-15 minutes)**

"Now it's your turn. Follow along with the ADO_MCP_Setup_Guide. I'll be here if you get stuck. Don't worry about speed—it's better to get it right.

**Here's what I want you to do:**
1. Open the ADO_MCP_Setup_Guide in your PM MCP Server Install Files folder
2. Follow Steps 1-5
3. Once you have the server running and tools visible, send me a thumbs up in Teams (or raise your hand)
4. Once everyone is done, we'll move to Work IQ

**If you get stuck:**
- Check the guide's troubleshooting section—lots of common issues are covered
- Post in Teams
- Wave at me and I'll come help

**You have 10-15 minutes. Go!**"

---

### **Part 4: Work IQ MCP Server (15-20 minutes)**

#### **Introduction (1 minute)**

"Great job, everyone! Now let's add Work IQ. This server gives Copilot access to your Microsoft 365 data—emails, meetings, files. It's like having your entire Outlook and OneDrive searchable from VS Code."

#### **Live Demo/Walkthrough:**

**Steps 1-2: Prerequisites & Configuration**

"Good news: The pattern is exactly the same as ADO.

1. **Prerequisites** – We already verified Node.js, so we're good.
2. **Configuration** – Open Copilot Chat, switch to Agent Mode, use the ready-made prompt from WorkIQ_MCP_Setup_Guide.md

The only difference: if you already have ADO configured, you'll tell Copilot to 'add Work IQ to my existing MCP config.' Copilot will merge it correctly."

**Step 3: Start the Server**

"Same as before: MCP Servers panel, find `workiq`, click Start."

**Step 4: Accept the EULA**

"Work IQ has one extra requirement—accepting the EULA. This is quick:

1. Open Copilot Chat
2. Type this prompt:
   ```
   I want to use the Work IQ MCP server. Please accept the EULA at https://github.com/microsoft/work-iq-mcp
   ```
3. Copilot will accept it for you
4. You'll be asked to authenticate with Microsoft—sign in and grant permissions

That's it. The EULA is a one-time thing."

**Step 5: Verify & Test**

"Once tools refresh, you can test:
```
What emails do I have from today?
```

or

```
What meetings do I have tomorrow?
```

Copilot will query your real M365 data."

#### **Hands-on Activity (12-15 minutes)**

"Alright, same process as ADO. Follow the WorkIQ_MCP_Setup_Guide:
1. Steps 1-4 (prerequisites through EULA acceptance)
2. Wait for authentication to complete
3. Step 5: Test a query
4. Give me a thumbs up when you're done

**You have 12-15 minutes. Go!**"

---

### **Part 5: MarkItDown MCP Server (Stretch Goal - 10 minutes)**

#### **Introduction (1 minute)**

"We have time, so let's do the stretch goal: MarkItDown. This one converts PDFs, Word docs, Excel files, and images to clean Markdown. Super useful if you need to turn documentation into git-friendly format.

**Fair warning:** MarkItDown requires Python 3.10+. If you don't have Python installed, we can skip this one or install it after. It's totally optional."

#### **Live Demo/Walkthrough:**

**Important:** "The big prerequisite here is Python. If you don't have it installed, hold up your hand and we can help during this session, or you can do it after."

1. **Prerequisites** – Check for Python: `python --version` must be 3.10+
2. **Installation** – Run `npm install -g markitdown-mcp-npx` (takes ~30 seconds)
3. **Configuration** – Ask Copilot to add it to your `.vscode/mcp.json` config
4. **Start** – MCP Servers panel, find `markitdown`, click Start
5. **Test** – Ask Copilot to convert a document:
   ```
   Convert the PDF at C:\path\to\document.pdf to Markdown
   ```

#### **Hands-on Activity (5-8 minutes, optional)**

"If you have Python installed and want to try, follow the MarkItDown_MCP_Setup_Guide. If not, don't worry—you can do this at your own pace later. The guide is in the same folder.

**5 minutes. Optional. Go if you'd like!**"

---

### **Part 6: Wrap-up & Q&A (5 minutes)**

**What to say:**

"Awesome work, everyone! You now have three powerful MCP servers in your workspace.

**Let me recap what you can do:**

1. **Azure DevOps** – Ask Copilot to fetch, update, and sync work items
   - Example: "Show me all Features assigned to me in OneITVSO"
   - Example: "Sync my Scenarios and Features to Markdown files"

2. **Work IQ** – Ask Copilot about your M365 data
   - Example: "What were the action items from my standup yesterday?"
   - Example: "Summarize emails from the past 3 days"

3. **MarkItDown** (if installed) – Convert documents to Markdown
   - Example: "Convert this PDF requirements document to Markdown"

**Next Steps:**

- **Explore.** Play around with different prompts. There's no wrong way to do it.
- **Share.** If you set these up in a shared workspace, commit the `.vscode/mcp.json` file to git so teammates get the same setup.
- **Reach out.** If you run into issues, check the troubleshooting sections in the guides or ask in Teams.
- **Feedback.** Let me know what works, what doesn't, and what you'd like to try next.

**Questions?**"

---

## Post-Session Follow-up

**Send to team:**

```
Thanks for coming to the MCP Server installation workshop! Here's what you need to know:

✅ **Your setup is ready.** You should have three MCP servers configured:
   - Azure DevOps (azureMcpProvider)
   - Work IQ (workiq)
   - MarkItDown (markitdown) [if you installed it]

📚 **Guides for reference** are in the PM MCP Server Install Files folder:
   - ADO_MCP_Setup_Guide.md
   - WorkIQ_MCP_Setup_Guide.md
   - MarkItDown_MCP_Setup_Guide.md

🚀 **Next session ideas:**
   - How to sync your ADO backlog to Markdown
   - Building custom Copilot workflows with MCP servers
   - Troubleshooting common issues

📝 **Feedback:** Let me know what you thought about the session and what you'd like to learn next.
```

---

## Facilitator Tips

### **Timing**
- **Part 1 (Intro):** 5 min
- **Part 2 (Pattern):** 3 min
- **Part 3 (ADO):** 20-25 min (10-15 min hands-on)
- **Part 4 (Work IQ):** 15-20 min (12-15 min hands-on)
- **Part 5 (MarkItDown):** 10 min (5-8 min optional hands-on)
- **Part 6 (Wrap-up):** 5 min
- **Total:** 50-65 minutes

### **Common Issues to Watch For**

1. **Node.js not found** – Have participants run `node --version` in PowerShell. If not found, help them install it.

2. **Python not found** (MarkItDown only) – Expected if they don't have Python. It's optional for this workshop.

3. **Authentication loops** – Happens sometimes. Solution: Clear browser cookies, try a different browser, or skip and retry after the session.

4. **JSON errors in config** – This shouldn't happen if they use Copilot to add the config, but if it does, help them restore from `.vscode/mcp.json` backup or paste the correct JSON.

5. **Slow server startup** – First-time startup can take 20-30 seconds. Let it load.

### **Demo Tips**

- Have a **backup workspace** ready in case your main one has issues
- **Test your internet** before the session (auth requires it)
- **Pre-authenticate** if possible, so you're not waiting for auth during the demo
- **Use real work items** from your project when demonstrating (more relatable)
- **Have a sample PDF or Word doc** ready if you're demoing MarkItDown

### **If You Run Over on Time**

- Skip Part 5 (MarkItDown) – it's marked as stretch goal for a reason
- Move Q&A offline – tell people to ask in Teams or reach out after
- Shorten Part 6 – just say "see the guides for next steps"

### **If You Have Extra Time**

- Demo combining servers: "Convert a PDF to Markdown, then create ADO work items from the content"
- Show how to commit `.vscode/mcp.json` to git so teammates get the same setup
- Walk through an actual use case from your team's workflow

---

## Session Success Metrics

By the end of the session:
- [ ] All participants have configured at least 2 MCP servers
- [ ] All participants can see MCP tools in Copilot Chat
- [ ] At least 80% of participants have run a successful test query
- [ ] Participants understand the 5-step installation pattern
- [ ] Participants know where to find troubleshooting help

---

## Checklist for the Day Before

- [ ] Test all three servers in your own workspace
- [ ] Review the setup guides one more time
- [ ] Prepare your demo workspace
- [ ] Send calendar reminder to team with download links for guides
- [ ] Test projector/screen share
- [ ] Prepare sample data for demos (work item IDs, document files)
- [ ] Have the PM MCP Server Install Files folder link ready to share

---

## Questions to Gauge Understanding

**At the end, you can ask:**

1. "What are the three MCP servers we set up today?" (ADO, Work IQ, MarkItDown)
2. "How do we add a new MCP server config? Do we edit JSON manually?" (No, ask Copilot)
3. "What's the first step when setting up a new MCP server?" (Verify prerequisites)
4. "Can you combine data from multiple MCP servers in one prompt?" (Yes! Great question.)
5. "If something goes wrong, where do you look first?" (Troubleshooting section in the guide)

---

Good luck with your session! You've got this. 🚀
