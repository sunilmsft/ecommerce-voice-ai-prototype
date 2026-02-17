# Work IQ MCP Server Setup Guide for PMs

**Target Audience:** Product Managers in Marketing Engineering  
**Last Updated:** February 12, 2026  
**Time to Complete:** 10-15 minutes

## What This Guide Does

This guide will help you enable the Work IQ Model Context Protocol (MCP) Server in VS Code, allowing GitHub Copilot to access your Microsoft 365 data—including emails, meetings, chats, files, and documents—directly from within your editor using natural language.

**What you'll be able to do after setup:**
- Ask Copilot questions about your emails and meetings
- Search across your M365 files and documents
- Get context from Teams chats and conversations
- Access your work data without leaving VS Code
- Use your M365 context to inform code, documentation, or planning work

---

## Background: What is Work IQ?

**Work IQ** is Microsoft's AI-powered service that provides unified access to your Microsoft 365 data. It powers features like Microsoft 365 Copilot and can surface insights from:
- Outlook emails
- Teams meetings and chats
- OneDrive and SharePoint files
- Calendar events
- OneNote notebooks
- And more...

**The Work IQ MCP Server** exposes this data to GitHub Copilot through the Model Context Protocol, enabling you to:
- Ask natural language questions about your work data
- Get summaries of recent meetings or emails
- Find files or information without context switching
- Use your M365 context to inform technical decisions

**Key benefits for PMs:**
- **Unified context** – Bring meeting notes, emails, and docs into your development workflow
- **No context switching** – Query your M365 data directly from VS Code
- **Natural language** – Ask questions like "What was discussed in yesterday's planning meeting?"
- **Privacy-first** – Respects all existing M365 permissions and security boundaries

---

## Prerequisites

Before you begin, ensure you have:

### Required Software
1. **VS Code** (latest version recommended)
   - Download: https://code.visualstudio.com/

2. **Node.js** (version 18 or higher)
   - Download: https://nodejs.org/
   - Used to run the MCP server via `npx`
   - Verify installation: Open PowerShell and run `node --version`

3. **GitHub Copilot extension** for VS Code
   - Install from VS Code Extensions marketplace
   - Must have an active Copilot license

### Required Access
4. **Microsoft 365 account**
   - Active Microsoft work account with M365 license
   - Access to Outlook, Teams, OneDrive, etc.

5. **Microsoft Entra ID authentication**
   - You'll be prompted to sign in with your Microsoft credentials during first use

---

## Step-by-Step Setup

### Step 1: Verify Prerequisites

1. Open PowerShell in VS Code (`` Ctrl+` ``)
2. Verify Node.js is installed:
   ```powershell
   node --version
   ```
   Should return something like `v20.x.x` or higher

3. Verify npm is available:
   ```powershell
   npm --version
   ```

### Step 2: Create MCP Configuration File

The MCP server configuration tells VS Code how to connect to Work IQ.

**Choose Your Setup Approach:**

#### Option A: Workspace-Specific Setup (Recommended)

Configuration lives in your project and can be shared with the team.

**Let GitHub Copilot add the configuration for you** (prevents JSON syntax errors):

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I ``)

2. Switch to **Agent Mode** (toggle at the top of the chat panel)

3. Copy and paste this prompt:

**If this is your first MCP server:**
```
Add the Work IQ MCP server to my .vscode/mcp.json configuration file. The server config is:

"workiq": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "@microsoft/work-iq-mcp"
  ]
}

Create the .vscode folder and mcp.json file if they don't exist.
```

**If you already have other MCP servers (like Azure DevOps):**
```
Add the Work IQ MCP server to my existing .vscode/mcp.json configuration file. The server config to add is:

"workiq": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "@microsoft/work-iq-mcp"
  ]
}

Keep all existing server configurations and add this as a new entry.
```

4. Copilot will create or update your `.vscode/mcp.json` file

5. Verify the configuration was added correctly by opening `.vscode/mcp.json`

#### Option B: Global Setup

Configuration applies to all your VS Code workspaces.

**Let GitHub Copilot add the configuration for you:**

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I ``)

2. Switch to **Agent Mode**

3. Copy and paste this prompt:

```
Add the Work IQ MCP server to my global VS Code settings (user settings.json). The server config is:

"workiq": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "@microsoft/work-iq-mcp"
  ]
}

Add this under mcp.servers in my user settings.
```

4. Copilot will update your user settings file

**Configuration explained:**
- `"workiq"` – The connection name (used by Copilot)
- `"@microsoft/work-iq-mcp"` – The NPM package for Work IQ MCP server
- `"-y"` – Auto-confirms NPM prompts

**Recommendation:** Use workspace-specific setup if working in shared repositories so teammates get the same configuration.

---

### Step 3: Start the MCP Server

1. Open the **MCP Servers** panel in VS Code:
   - Open Command Palette: `Ctrl+Shift+P`
   - Search for: `MCP: Focus on MCP Servers View`
   - (Or look for the MCP icon in the Activity Bar)

2. Find `workiq` in the list

3. Click the **Start** button next to it

4. **First-time setup:**
   - The server will start and may download dependencies
   - This may take a moment on first run

### Step 4: Accept the EULA

Work IQ requires accepting the End User License Agreement before full access is enabled.

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I `` or click the Copilot icon)

2. Switch to **Agent Mode** (toggle at the top of the chat panel)

3. Click the **Refresh Tools** button (circular arrow icon)

4. Look for Work IQ tools in the list - you should see:
   - `mcp_workiq_accept_eula`
   - `mcp_workiq_ask_work_iq`

5. **Accept the EULA by typing this prompt:**

```
I want to use the Work IQ MCP server. Please accept the EULA at https://github.com/microsoft/work-iq-mcp
```

6. Copilot will call the `accept_eula` tool and confirm acceptance

7. **Authenticate with Microsoft:**
   - A browser window will open asking you to sign in
   - Use your Microsoft work credentials
   - Grant the requested permissions (read emails, calendar, files, etc.)
   - The browser will confirm success – you can close it

### Step 5: Test the Connection

Run a simple test to ensure everything works:

1. In Copilot Chat (Agent Mode), try one of these test prompts:

```
What meetings do I have today?
```

```
Summarize my emails from this week
```

```
What files have I recently worked on?
```

2. Copilot should call the Work IQ MCP tool and return results from your M365 data

3. If this works, you're all set!

---

## Using Work IQ with Copilot

### Example Prompts to Try

Once you're set up, try these prompts in Copilot Chat (Agent Mode):

**Meeting & Calendar Queries:**
```
What meetings do I have tomorrow?
```
```
Summarize the key points from my standup meeting yesterday
```
```
Who did I meet with last week?
```

**Email Queries:**
```
Do I have any unread emails from [person name]?
```
```
What were the action items in emails from the past 3 days?
```
```
Find emails about the Lead Acquisition project
```

**File & Document Queries:**
```
What files have I edited this week?
```
```
Find documents about Azure DevOps setup
```
```
Show me recent PowerPoint presentations I worked on
```

**Context-Aware Development:**
```
Based on my recent meeting notes, what are the top priorities for the Lead Acquisition project?
```
```
What questions came up in Teams chats about the MCP server setup?
```
```
Summarize feedback from stakeholders in my recent emails
```

### Combining Work IQ with Other MCP Servers

If you have multiple MCP servers configured (e.g., Work IQ + Azure DevOps), you can combine them in powerful ways:

```
Based on my meeting notes from this week, what ADO work items should I prioritize?
```

```
Get the status of work item 12345, then draft an email update to the team
```

```
Find files related to the Segmentation project and summarize the current state from ADO
```

---

## Common Troubleshooting

### Problem: Work IQ Tools Don't Appear in Copilot Chat

**Symptoms:**
- Copilot Chat doesn't show Work IQ tools in the tool list
- Prompts fail with "I don't have access to that tool"

**Solutions:**
1. **Verify the MCP server is running:**
   - Open MCP Servers panel
   - Check if `workiq` shows as "Running"
   - If not, click Start

2. **Refresh tools in Copilot Chat:**
   - Click the circular arrow (Refresh Tools) button in Chat
   - Toggle Agent Mode off and on

3. **Restart VS Code:**
   - Close and reopen VS Code
   - MCP servers should auto-start on launch

4. **Check the MCP server logs:**
   - In MCP Servers panel, right-click `workiq` → View Logs
   - Look for installation or connection errors

---

### Problem: `npx` Command Not Found

**Symptoms:**
- MCP server fails to start
- Error message: `'npx' is not recognized as an internal or external command`

**Solutions:**
1. **Install Node.js:**
   - Download from https://nodejs.org/
   - Choose LTS version
   - Restart VS Code after installation

2. **Verify installation:**
   ```powershell
   node --version
   npx --version
   ```

3. **Add Node.js to PATH:**
   - If installed but still not found, ensure Node.js is in your system PATH
   - Search Windows for "Environment Variables"
   - Add `C:\Program Files\nodejs\` to PATH
   - Restart VS Code

---

### Problem: Authentication Fails or Loops

**Symptoms:**
- Browser opens but authentication doesn't complete
- Repeatedly prompted to sign in
- "Permission denied" errors

**Solutions:**
1. **Clear browser cache/cookies** and try again

2. **Try a different browser:**
   - The auth prompt may work better in Edge or Chrome

3. **Check M365 permissions:**
   - Verify you can access Outlook, Teams, OneDrive in the browser
   - Some organizations have conditional access policies that may affect MCP server access

4. **Revoke and re-authorize:**
   - Go to https://myaccount.microsoft.com/
   - Find Work IQ or related app in connected apps
   - Revoke access, then restart MCP server to re-authenticate

5. **Contact IT admin:**
   - Some organizations require admin approval for third-party apps
   - Share the EULA link: https://github.com/microsoft/work-iq-mcp

---

### Problem: EULA Acceptance Fails

**Symptoms:**
- Can't accept the EULA
- Acceptance doesn't persist

**Solutions:**
1. **Use the exact prompt:**
   ```
   I want to use the Work IQ MCP server. Please accept the EULA at https://github.com/microsoft/work-iq-mcp
   ```

2. **Verify you're in Agent Mode:**
   - The EULA acceptance tool only works in Agent Mode
   - Check the toggle at the top of Copilot Chat

3. **Restart the MCP server:**
   - Stop and restart the `workiq` server in MCP Servers panel
   - Try accepting the EULA again

---

### Problem: No Results or "Access Denied" for Queries

**Symptoms:**
- Queries return no results
- "You don't have permission" errors
- Empty responses

**Solutions:**
1. **Verify M365 data exists:**
   - Check that you actually have emails/meetings/files in your M365 account
   - Try a specific query like "emails from today" rather than broad searches

2. **Check date ranges:**
   - Work IQ may have limits on how far back it searches
   - Try more recent queries: "meetings this week" vs "meetings from last year"

3. **Permissions and retention policies:**
   - Your organization may have data retention policies that limit access
   - Some content types may be restricted by your IT admin

4. **Wait for indexing:**
   - If you just accepted the EULA, indexing may take a few minutes
   - Try again in 5-10 minutes

---

### Problem: Slow Performance or Timeouts

**Symptoms:**
- Work IQ queries take a long time to respond
- Requests time out
- Partial results returned

**Solutions:**
1. **Make queries more specific:**
   - Instead of "all my emails", try "emails from this week"
   - Add sender names, date ranges, or topics

2. **Check network connectivity:**
   - Ensure you're on Microsoft corporate network or VPN
   - Test M365 access in browser

3. **Reduce query scope:**
   - Query one data type at a time (emails OR meetings, not both)
   - Use smaller time windows

---

### Problem: Package Installation Errors

**Symptoms:**
- Error: `Failed to download @microsoft/work-iq-mcp`
- NPM errors during server start

**Solutions:**
1. **Check NPM registry access:**
   ```powershell
   npm config get registry
   ```
   Should return `https://registry.npmjs.org/`

2. **Clear NPM cache:**
   ```powershell
   npm cache clean --force
   ```

3. **Install manually:**
   ```powershell
   npm install -g @microsoft/work-iq-mcp
   ```

4. **Check corporate proxy settings:**
   - Your organization may require proxy configuration for NPM
   - Contact IT support for proxy settings

---

## Privacy & Security Considerations

### What Data Does Work IQ Access?

The Work IQ MCP server can access:
- Your emails (Outlook)
- Your calendar events
- Your Teams chats and meetings
- Your files in OneDrive and SharePoint (that you have access to)
- Your OneNote notebooks

### Privacy Protections

- **Permission-based:** Only accesses data you already have permission to see
- **User-scoped:** Cannot see other users' data unless explicitly shared with you
- **No storage:** Queries run in real-time; Work IQ doesn't store your data
- **Audit trail:** All access is logged in Microsoft's compliance systems
- **Consent-driven:** Requires explicit authentication and EULA acceptance

### Best Practices

✅ **Do's:**
- Use Work IQ for your own data retrieval and context gathering
- Verify information before sharing sensitive details
- Revoke access if you're no longer using the tool
- Review granted permissions periodically

❌ **Don'ts:**
- Don't share authentication tokens or credentials
- Don't use Work IQ to access data you shouldn't have access to
- Don't assume all queries will return complete results (retention policies apply)
- Don't bypass your organization's security policies

---

## Workspace vs. Global Setup

### Workspace-Specific Setup (Recommended for Teams)

✅ **Advantages:**
- Configuration in `.vscode/mcp.json` can be committed to git
- Team members get the same setup automatically
- Easy to see what MCP servers a project uses
- Can have different configurations per project

❌ **Limitations:**
- Need to set up for each workspace/project
- EULA acceptance is per-user (not shared)

### Global Setup

✅ **Advantages:**
- Configure once, works everywhere
- Don't need to set up for each project
- Personal preferences follow you across all workspaces

❌ **Limitations:**
- Can't easily share with team
- Configuration lives in user settings (not in repo)

**Recommendation for Marketing Engineering PMs:**

Use **workspace-specific** if you want the team to have consistent access to Work IQ context. Use **global** if it's just for your personal productivity workflow.

---

## Additional Resources

### Internal Microsoft Resources
- **Work IQ MCP GitHub:** https://github.com/microsoft/work-iq-mcp
- **Model Context Protocol Docs:** Search "MCP" in Docs.microsoft.com
- **Microsoft 365 Copilot Documentation:** https://aka.ms/m365copilot

### Getting Help
- **Teams Channel:** [Power Platform Ninjas](https://teams.microsoft.com/l/team/19:7896b998b92945d68fcfbd5cef889e03@thread.tacv2)
- **GitHub Issues:** https://github.com/microsoft/work-iq-mcp/issues
- **IT Support:** For authentication or M365 access issues

---

## Next Steps

After completing this guide:
1. **Experiment with queries** – Try different types of questions to understand what Work IQ can find
2. **Combine with ADO MCP** – Use both tools together for comprehensive context
3. **Share with your team** – Help other PMs set up Work IQ for collaborative workflows
4. **Provide feedback** – Report issues or suggestions to improve the tool

---

## Changelog

| Date | Change |
|------|--------|
| 2026-02-12 | Initial guide created for Marketing Engineering PMs |

---

## Questions or Feedback?

Contact: [Your Team Lead or Engineering Contact]
