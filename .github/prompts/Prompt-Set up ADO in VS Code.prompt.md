---
agent: agent
---
Define the task to achieve, including specific requirements, constraints, and success criteria.

# First-time setup: Sync Azure DevOps backlog → Markdown (via MCP)
 
This is a "copy/paste and run" setup guide you can share with teammates to reproduce the exact workflow we used: run an Azure DevOps saved query via an MCP server, batch-fetch work items, and materialize Scenarios + child Features as Markdown under `backlog/scenarios/`.
 
## Quick answers to your clarifications
 
 
- In this repo, the Azure DevOps MCP server is started via `.vscode/mcp.json` using `npx @azure-devops/mcp ...`.
- Copilot Chat (Agent Mode) then calls the MCP tools exposed by that server.
 
No additional Azure DevOps-specific VS Code extension is required for the NPX-based MCP server configuration in `.vscode/mcp.json`.
 
### What does the user need to supply?
At minimum:
- Azure DevOps **organization** `MicrosoftIT`
- Azure DevOps **project** `OneITVSO`
- **Area Path** `OneITVSO\BIC CXP\CME Engagement and Acquisition\LM Lead Qualification\Bots`
- A saved **query id** (or a WIQL query if their MCP server supports raw WIQL)
 
Authentication:
- With this repo's MCP approach, the user should be prompted to sign in interactively the first time they run an ADO tool.
 
## Prereqs (what to install)
 
### Required
- VS Code
- GitHub Copilot extension (for Copilot Chat / Agent Mode)
- Node.js (so `npx` works)
 
### Recommended (workspace)
This repo already includes extension recommendations in `.vscode/extensions.json`. The only *hard* requirement is Copilot + an MCP client UI (VS Code now has built-in MCP support in many builds; otherwise an MCP client extension may be needed).
 
## Required MCP server
 
We used the official Azure DevOps MCP server package started via NPX.
 
### `.vscode/mcp.json` (template)
Tell Copilot to generate this file (or copy it) in the new workspace:
 
```jsonc
{
  "servers": {
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
  }
}
```
 
Replace `<ORG>` with the organization name (ex: `MicrosoftIT`).
 
## How to start and verify MCP tools
 
1. Open the workspace in VS Code.
2. Start the MCP server:
   - Open the **MCP Servers** UI.
   - Start server: `azureMcpProvider`.
3. Open Copilot Chat and switch to **Agent Mode**.
4. Refresh/select tools and confirm you see ADO tools from the MCP server.
5. Run a simple read to force auth (you should be prompted to sign in):
   - Example: "Get work item 12345 in project `<PROJECT>`".
 
## What tools we used (and what they do)
 
During the Scenario/Feature sync, we used the MCP server's "work items" tools (names can vary slightly, but in this workspace they appeared as):
 
- `mcp_azuremcpprovi_wit_get_query_results_by_id`
  - Runs a **saved query** and returns matching work item references.
- `mcp_azuremcpprovi_wit_get_work_items_batch_by_ids`
  - Batch-fetches work items by ids with a requested field list.
- `mcp_azuremcpprovi_wit_get_work_item` (optional / used when drilling into one item)
  - Fetches a single work item.
 
(We also used local file tools to create folders/files, but your colleagues won't need to know those—Copilot will handle writing markdown.)
 
## Prompt template: "Sync my Scenarios + Features to Markdown"
 
Copy/paste this into Copilot Chat (Agent Mode) and fill in placeholders.
 
```text
You are syncing Azure DevOps work items to my local workspace as markdown.
 
Context:
- MCP server connection: azureMcpProvider
- Org: https://dev.azure.com/<ORG>
- Project: <PROJECT>
- Saved query id: <QUERY_ID>
- Area path (exact): <AREA_PATH>
 
Goal:
- Materialize all Scenario work items returned by the saved query into backlog/scenarios/<scenarioId>-<slug>/scenario.md
- For each Scenario, also materialize its child Feature work items into backlog/scenarios/<scenarioId>-<slug>/feature-<id>.md
 
Required fields to fetch for each work item:
- System.Id
- System.WorkItemType
- System.Title
- System.State
- System.AreaPath
- System.IterationPath
- System.AssignedTo
- System.Tags
- System.CreatedDate
- System.ChangedDate
- System.Description
 
Process (must follow):
1) Run the saved query by id to get Scenario ids.
2) Batch-get the Scenario work items by ids using only the fields above.
3) For each Scenario, discover child Features from the Scenario relations (Hierarchy-Forward).
4) Batch-get all Feature work items by ids using only the fields above.
5) Write/update markdown files using this contract:
   - YAML front matter: id/type/title/state/areaPath/iterationPath/assignedTo/tags/createdDate/changedDate/url/parentId/childIds
   - Body sections: metadata table + ## Description + ## Links
   - Scenario only: ## Child Features list linking to feature-<id>.md
 
Constraints:
- Idempotent: update files if they already exist.
- Never write secrets.
- Keep folder naming as <scenarioId>-<slug> (slug lowercased, non-alphanumerics -> '-', trimmed; limit total length).
 
Output:
- Print counts: scenarios synced, features synced, scenarios with no child features.
```
 
## Prompt template: "Generate my .vscode MCP config"
 
Use this if a colleague is starting from a blank workspace and wants Copilot to scaffold the right files.
 
```text
Create a .vscode/mcp.json that starts the Azure DevOps MCP server via npx.
- Connection name must be: azureMcpProvider
- Use org: <ORG>
- Enable domains: core, work-items, search
Also create a .vscode/settings.json that prevents committing secrets by excluding .env files.
Do not write any PATs or secrets into the repo.
```
 
## Troubleshooting
 
- If tools don't appear in Agent Mode:
  - Ensure the MCP server is started (MCP Servers UI)
  - Refresh tools in Copilot Chat
- If `npx` fails:
  - Install Node.js
- If the saved query returns unexpected items:
  - Confirm the query id and project
  - Confirm the Area Path string is exact (double backslashes in markdown)
