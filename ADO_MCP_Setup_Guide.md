# Azure DevOps MCP Server Setup Guide for PMs

**Target Audience:** Product Managers in Marketing Engineering  
**Last Updated:** February 12, 2026  
**Time to Complete:** 15-20 minutes

## What This Guide Does

This guide will help you enable the Azure DevOps (ADO) Model Context Protocol (MCP) Server in VS Code, allowing GitHub Copilot to directly read and update work items in your ADO backlog—all from within your editor, using natural language.

**What you'll be able to do after setup:**
- Ask Copilot to fetch work items from saved queries
- Sync your ADO Scenarios and Features to local Markdown files
- Update work item fields using natural language
- Link work items, add comments, and manage backlogs without leaving VS Code

---

## Background: What is MCP?

**Model Context Protocol (MCP)** is a standardized protocol that allows AI clients (like GitHub Copilot) to communicate with enterprise tools and APIs in a consistent, discoverable way.

Think of it like this:
- **Without MCP:** You manually copy data from ADO to your editor, update it, then paste it back
- **With MCP:** Copilot sees ADO as a "toolbox" and can read/write work items directly based on your natural language requests

**Key benefits for PMs:**
- **No context switching** – Stay in VS Code while working with ADO
- **Natural language interface** – Ask Copilot to "update the status of Feature 12345" instead of clicking through the ADO portal
- **Bulk operations** – Sync entire backlogs or batch-update work items with simple prompts
- **Audit trail** – All changes respect ADO permissions and are logged

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
4. **Azure DevOps access**
   - Organization: `MicrosoftIT`
   - Project: `OneITVSO` (or your specific project)
   - Permissions: Must be able to read/write work items in your team's area path

5. **Microsoft Entra ID authentication**
   - You'll be prompted to sign in with your Microsoft credentials during first use

### Helpful Context
Before proceeding, have the following information ready:
- Your ADO **organization name** (e.g., `MicrosoftIT`)
- Your ADO **project name** (e.g., `OneITVSO`)
- Your team's **Area Path** (e.g., `OneITVSO\BIC CXP\CME Engagement and Acquisition\LM Lead Qualification\Bots`)
- (Optional) A saved **query ID** if you want to sync specific work items

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

### Step 2: Run the Setup Prompt

The easiest way to configure the MCP server is to use the included setup prompt, which will automatically create the necessary configuration files.

**Option A: Copy and Paste the Prompt (Recommended)**

1. Open the file [Prompt-Set up ADO in VS Code.prompt.md](Prompt-Set%20up%20ADO%20in%20VS%20Code.prompt.md) in this folder

2. Find the section: **"Prompt template: 'Generate my .vscode MCP config'"**

3. Copy the entire prompt text (starting with `Create a .vscode/mcp.json...`)

4. Open GitHub Copilot Chat in VS Code (`` Ctrl+Alt+I ``)

5. Switch to **Agent Mode** (toggle at the top of the chat panel)

6. Paste the prompt and replace `<ORG>` with your organization name (e.g., `MicrosoftIT`)

7. Press Enter and let Copilot create the files for you

**Option B: Install as a Workspace Prompt**

Alternatively, you can ask Copilot to install the prompt file:

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I ``)

2. Type or paste:
   ```
   Install the prompt file "Prompt-Set up ADO in VS Code.prompt.md" from the PM MCP Server Install Files folder as a workspace prompt
   ```

3. Once installed, you can invoke it using `#file:Prompt-Set up ADO in VS Code.prompt.md` in future chats

### What the Setup Prompt Will Do

When you run the setup prompt, Copilot will automatically:

1. **Create `.vscode/mcp.json`** with the Azure DevOps MCP server configuration
2. **Create `.vscode/settings.json`** with security settings to prevent committing secrets
3. Configure the MCP server to use your specified organization

**The generated MCP configuration will look like this:**

```json
{
  "servers": {
    "azureMcpProvider": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@azure-devops/mcp",
        "MicrosoftIT",
        "-d",
        "core",
        "work-items",
        "search"
      ]
    }
  }
}
```

**Configuration explained:**
- `"azureMcpProvider"` – The connection name (used in prompts later)
- `"MicrosoftIT"` – Your ADO organization name
- `"-d"` flag enables specific domains:
  - `core` – Basic project/team info
  - `work-items` – Work item read/write operations
  - `search` – Query and search capabilities

---

### Workspace vs. Global MCP Server Setup

You can configure MCP servers either for a specific workspace or globally for all your VS Code projects. Here's what to consider:

**Workspace-Specific Setup (Recommended for PMs)**

This is what the setup prompt creates by default.

✅ **Advantages:**
- Configuration lives in `.vscode/mcp.json` within your project
- Can be committed to git and shared with team members
- Each project can have different ADO organizations or settings
- Easy to see what MCP servers a project uses
- Team consistency – everyone uses the same configuration

❌ **Limitations:**
- Need to set up MCP for each workspace/project
- Configuration doesn't follow you to other workspaces

**How to do it:**
- Follow Step 2 above (the setup prompt creates workspace config)
- The `.vscode/mcp.json` file will be in your project root
- Commit `.vscode/mcp.json` to git so teammates can use it

---

**Global Setup**

Configures MCP servers for all your VS Code workspaces.

✅ **Advantages:**
- Configure once, works everywhere
- Don't need to set up for each project
- Personal preferences follow you across all workspaces

❌ **Limitations:**
- Configuration file location varies by OS
- Can't easily share with team
- Less flexible for multi-org scenarios
- Harder to troubleshoot when things go wrong

**How to do it:**

1. Open VS Code Settings (`` Ctrl+, ``)

2. Search for: `mcp`

3. Click "Edit in settings.json"

4. Add the MCP server configuration to your user settings:
   ```json
   {
     "mcp.servers": {
       "azureMcpProvider": {
         "type": "stdio",
         "command": "npx",
         "args": [
           "-y",
           "@azure-devops/mcp",
           "MicrosoftIT",
           "-d",
           "core",
           "work-items",
           "search"
         ]
       }
     }
   }
   ```

**Recommendation for Marketing Engineering PMs:**

Use **workspace-specific setup** because:
- Your team works in shared repositories
- Different projects may use different ADO organizations
- Teammates can clone the repo and immediately have the right MCP configuration
- Easier to get help when everyone has the same setup

---

### Step 3: Create MCP Configuration File (Manual Alternative)

If you prefer not to use the setup prompt from Step 2, you can ask Copilot to add the configuration directly:

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I ``)

2. Switch to **Agent Mode**

3. Copy and paste this prompt (replace `<ORG>` with your organization name, e.g., `MicrosoftIT`):

```
Add the Azure DevOps MCP server to my .vscode/mcp.json configuration file. The server config is:

"azureMcpProvider": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "@azure-devops/mcp",
    "<ORG>",
    "-d",
    "core",
    "work-items",
    "search"
  ]
}

Create the .vscode folder and mcp.json file if they don't exist.
```

4. Copilot will create or update your `.vscode/mcp.json` file

5. Verify the configuration was added correctly by opening `.vscode/mcp.json`

### Step 4: Start the MCP Server

1. Open the **MCP Servers** panel in VS Code:
   - Open Command Palette: `Ctrl+Shift+P`
   - Search for: `MCP: Focus on MCP Servers View`
   - (Or look for the MCP icon in the Activity Bar)

2. Find `azureMcpProvider` in the list

3. Click the **Start** button next to it

4. **First-time authentication:**
   - A browser window will open asking you to sign in
   - Use your Microsoft credentials
   - Grant the requested permissions (read/write work items)
   - The browser will confirm success – you can close it

### Step 5: Verify MCP Tools Are Available

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I `` or click the Copilot icon)

2. Switch to **Agent Mode** (toggle at the top of the chat panel)

3. Click the **Refresh Tools** button (circular arrow icon)

4. Look for ADO-related tools in the tool list. You should see tools like:
   - `mcp_azuremcpprovi_wit_get_work_item`
   - `mcp_azuremcpprovi_wit_update_work_item`
   - `mcp_azuremcpprovi_wit_get_query_results_by_id`

### Step 6: Test the Connection

Run a simple test to ensure everything works:

1. In Copilot Chat (Agent Mode), paste this prompt (replace `<WORK_ITEM_ID>` with a real work item ID from your project):

```
Get work item <WORK_ITEM_ID> from project OneITVSO
```

2. Copilot should call the MCP tool and return the work item details

3. If this works, you're all set!

---

## Common Troubleshooting

### Problem: MCP Tools Don't Appear in Copilot Chat

**Symptoms:**
- Copilot Chat doesn't show ADO tools in the tool list
- Prompts fail with "I don't have access to that tool"

**Solutions:**
1. **Verify the MCP server is running:**
   - Open MCP Servers panel
   - Check if `azureMcpProvider` shows as "Running"
   - If not, click Start

2. **Refresh tools in Copilot Chat:**
   - Click the circular arrow (Refresh Tools) button in Chat
   - Toggle Agent Mode off and on

3. **Restart VS Code:**
   - Close and reopen VS Code
   - MCP servers should auto-start on launch

4. **Check the MCP server logs:**
   - In MCP Servers panel, right-click `azureMcpProvider` → View Logs
   - Look for authentication or connection errors

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

---

### Problem: Authentication Fails or Loops

**Symptoms:**
- Browser opens but authentication doesn't complete
- Repeatedly prompted to sign in

**Solutions:**
1. **Clear browser cache/cookies** and try again

2. **Try a different browser:**
   - The auth prompt may work better in Edge or Chrome

3. **Check ADO permissions:**
   - Go to https://dev.azure.com/MicrosoftIT/OneITVSO
   - Verify you can view work items in the ADO portal
   - Ensure you have "Contributor" or higher permissions

4. **Revoke and re-authorize:**
   - Go to https://myaccount.microsoft.com/
   - Find Azure DevOps in connected apps
   - Revoke access, then restart MCP server to re-authenticate

---

### Problem: Query Returns No Results or Wrong Items

**Symptoms:**
- Prompt completes but syncs 0 work items
- Syncs items from the wrong area path

**Solutions:**
1. **Verify the query ID:**
   - In ADO, go to Queries
   - Open your saved query
   - Copy the GUID from the URL (format: `12345678-1234-1234-1234-123456789abc`)

2. **Check the Area Path string:**
   - Must match **exactly** (case-sensitive, correct backslashes)
   - In ADO, check the work item's Area Path field and copy it exactly
   - Example: `OneITVSO\BIC CXP\CME Engagement and Acquisition\LM Lead Qualification\Bots`

3. **Test the query in ADO first:**
   - Run the query in the ADO portal to see what it returns
   - Make sure it returns Scenario work items

4. **Check project name:**
   - Verify you're using the correct project name (e.g., `OneITVSO`, not `OneIT` or `VSTO`)

---

### Problem: Slow Performance or Timeouts

**Symptoms:**
- MCP tools take a long time to respond
- Requests time out

**Solutions:**
1. **Reduce batch size:**
   - If syncing many work items, try fetching smaller batches
   - Add `"top": 50` parameter to limit results

2. **Limit fields:**
   - Only request the fields you need
   - The prompt template already uses a minimal field set

3. **Check network connectivity:**
   - Ensure you're on Microsoft corporate network or VPN
   - Test ADO access in browser

---

### Problem: Permission Denied Errors

**Symptoms:**
- Error: "You do not have permission to perform this action"
- Can read work items but not update them

**Solutions:**
1. **Verify ADO permissions:**
   - In ADO, go to Project Settings → Security
   - Check your area path permissions
   - Ensure you have "Edit work items in this node" permission

2. **Check organization-level access:**
   - Some operations require organization-level permissions
   - Contact your ADO project admin

---

### Problem: Markdown Files Not Created

**Symptoms:**
- Prompt completes successfully but no files appear
- Files created in wrong location

**Solutions:**
1. **Check the workspace folder:**
   - Ensure VS Code is opened to your repo root
   - The prompt creates `backlog/scenarios/` relative to workspace root

2. **Verify file paths in output:**
   - Copilot should report created file paths
   - Check if there were any write errors

3. **Check file permissions:**
   - Ensure your user has write access to the workspace folder

---

## Additional Resources

### Internal Microsoft Resources
- **MCP Documentation:** Search "Model Context Protocol" in Docs.microsoft.com
- **Azure DevOps MCP Server:** https://www.npmjs.com/package/@azure-devops/mcp
- **GitHub Copilot for VS Code:** https://aka.ms/copilot-docs

### Getting Help
- **Teams Channel:** [Power Platform Ninjas](https://teams.microsoft.com/l/team/19:7896b998b92945d68fcfbd5cef889e03@thread.tacv2)
- **Your Team's ADO Admin:** For project-specific permission issues
- **IT Support:** For Node.js installation or network issues

### Example Prompts to Try

Once you're set up, try these prompts in Copilot Chat:

**Get a single work item:**
```
Get work item 12345 from project OneITVSO
```

**List my assigned work items:**
```
Show me all work items assigned to me in project OneITVSO
```

**Update a work item:**
```
Update work item 12345 in OneITVSO:
- Set state to Active
- Add tag "Q1-2026"
```

**Add a comment:**
```
Add a comment to work item 12345 in OneITVSO: "Reviewed in standup, moving forward"
```

**Link work items:**
```
Link work item 12345 to 12346 in OneITVSO as a parent-child relationship
```

---

## Best Practices

### Do's
- ✅ **Keep your local markdown synced regularly** – Run the sync prompt weekly or before planning sessions
- ✅ **Use version control** – Commit markdown files to git for historical tracking
- ✅ **Test read operations first** – Before updating work items, test with read-only queries
- ✅ **Use specific work item IDs** – Be explicit when updating items to avoid mistakes
- ✅ **Review before bulk updates** – Ask Copilot to show you what will change before confirming

### Don'ts
- ❌ **Don't commit secrets** – Never put PATs or tokens in `.vscode/mcp.json`
- ❌ **Don't skip authentication** – Always authenticate with your Microsoft account
- ❌ **Don't use stale query IDs** – Verify query IDs exist and return expected results
- ❌ **Don't bypass ADO permissions** – MCP respects your existing access; don't try to work around it
- ❌ **Don't forget to refresh tools** – After restarting VS Code, refresh Copilot's tool list

---

## Next Steps

After completing this guide:
1. **Explore other MCP servers** – Microsoft has MCP servers for M365, IcM, and more
2. **Customize the sync prompt** – Adjust fields, folder structure, or filters to match your workflow
3. **Share with your team** – Help other PMs set up MCP for consistent backlog management
4. **Provide feedback** – If you encounter issues or have suggestions, share them with the team

---

## Changelog

| Date | Change |
|------|--------|
| 2026-02-12 | Initial guide created for Marketing Engineering PMs |

---

## Questions or Feedback?

Contact: [Your Team Lead or Engineering Contact]
