# VS Code Setup Guide — eCommerce Voice AI Prototype

A step-by-step guide to setting up VS Code on a new machine so everything works the same way: extensions, MCP servers, GitHub Copilot, and this repository.

---

## Prerequisites

Install these three tools first:

| Tool | Download | Purpose |
|------|----------|---------|
| **Visual Studio Code** | [code.visualstudio.com](https://code.visualstudio.com/) | Code editor |
| **Git** | [git-scm.com/downloads](https://git-scm.com/downloads) | Version control |
| **Node.js (LTS)** | [nodejs.org](https://nodejs.org/) | Required for MCP servers via `npx` |

> After installing, restart your terminal so the `code`, `git`, and `node` commands are available.

---

## Step 1: Configure Git

Open a terminal (PowerShell on Windows, Terminal on Mac) and set your identity:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@microsoft.com"
```

---

## Step 2: Clone the Repository

```powershell
git clone https://github.com/sunilmsft/ecommerce-voice-ai-prototype.git
cd ecommerce-voice-ai-prototype
code .
```

This opens the project in VS Code. The workspace settings (`.vscode/settings.json`) and MCP server configs (`.vscode/mcp.json`) are included in the repo and will be picked up automatically.

---

## Step 3: Install VS Code Extensions

Run these commands in a terminal to install all required extensions:

```powershell
code --install-extension github.copilot-chat
code --install-extension ms-azuretools.vscode-azure-github-copilot
code --install-extension ms-azuretools.vscode-azure-mcp-server
code --install-extension ms-azuretools.vscode-azureresourcegroups
code --install-extension pm-lab.vscode-pm-tips
code --install-extension pm-lab.welcome-agent
code --install-extension ritwickdey.liveserver
```

### What each extension does

| Extension | Purpose |
|-----------|---------|
| **GitHub Copilot Chat** | AI pair programmer — chat, inline suggestions, agent mode |
| **Azure GitHub Copilot** | Azure-aware Copilot skills (deploy, diagnose, resource lookup) |
| **Azure MCP Server** | Connects Copilot to Azure resources via MCP protocol |
| **Azure Resource Groups** | Browse and manage Azure resources from the sidebar |
| **PM Lab Tips** | PM-specific tips and workflows |
| **Welcome Agent** | Onboarding agent for new workspace setup |
| **Live Server** | Launch a local dev server with live reload for HTML prototypes |

---

## Step 4: Sign Into GitHub Copilot

1. Click the **Accounts** icon in the bottom-left corner of VS Code
2. Sign in with your **GitHub account** that has Copilot access
3. Copilot Chat should activate — you'll see the chat icon in the sidebar

---

## Step 5: Verify MCP Servers

The repository includes a `.vscode/mcp.json` that configures three MCP (Model Context Protocol) servers:

| Server | What It Does |
|--------|-------------|
| **Azure DevOps MCP** | Query ADO work items and search across projects |
| **WorkIQ** | Microsoft internal productivity tooling |
| **MarkItDown** | Convert documents (PDF, DOCX, PPTX) to Markdown |

These servers use `npx` and download automatically on first use — no separate installation needed.

**To verify they're working:**
1. Open **Copilot Chat** (Ctrl+Shift+I)
2. Click the **tools icon** (🔧) at the bottom of the chat input
3. You should see tools listed from each MCP server

---

## Step 6: Run the Prototype Locally

**Option A — Direct browser:**
- Double-click any `.html` file in the repo to open it in your browser

**Option B — Live Server (recommended):**
1. Open any `.html` file in VS Code
2. Click **"Go Live"** in the bottom status bar (from the Live Server extension)
3. Your browser opens with live reload — changes update automatically

> Use **Chrome** or **Edge** for best results — the voice-enabled prototypes use Azure Speech SDK and Web Speech API which work best in Chromium browsers.

---

## Repository Structure

```
ecommerce-voice-ai-prototype/
├── voice-enabled/
│   ├── index.html          ← Primary demo (voice + chat + quoting)
│   └── classic.html         ← Classic layout variant
├── original-prototype.html  ← Original chat + voice prototype
├── .eCommerce Voice AI Agent prototype.html
├── .Hybrid - ai-chat-assistant-prototype.html
├── .Opt#1- ai-chat-assistant-prototype-human-first.html
├── .Opt#2 - AI-First Assist.html
├── .vscode/
│   ├── settings.json        ← Workspace settings (auto-applied)
│   └── mcp.json             ← MCP server configs (auto-applied)
├── ai-chat-design-specs.md  ← Design system documentation
├── ai-chat-user-flows.md    ← User flow diagrams (Mermaid)
└── README.md                ← Project overview
```

---

## Optional: Enable Settings Sync

To avoid repeating these steps on future machines:

1. In VS Code, click the **Accounts** icon (bottom-left)
2. Select **Turn on Settings Sync**
3. Choose what to sync: ✅ Extensions, ✅ Settings, ✅ Keybindings, ✅ UI State
4. Sign in with your Microsoft or GitHub account

Once enabled, any new VS Code installation where you sign in will automatically restore your extensions and settings.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `code` command not found | Reinstall VS Code, or run **Cmd+Shift+P → "Install 'code' command in PATH"** |
| `npx` not found | Install Node.js and restart your terminal |
| MCP servers not showing tools | Restart VS Code; check that Node.js is installed |
| Voice not working in prototype | Use Chrome or Edge; check that your system volume is on |
| Git push rejected | Make sure you have write access to the GitHub repo |

---

## Live Demo

The prototype is deployed via GitHub Pages:

🔗 **[sunilmsft.github.io/ecommerce-voice-ai-prototype](https://sunilmsft.github.io/ecommerce-voice-ai-prototype/)**

For the full voice-enabled experience:

🔗 **[sunilmsft.github.io/ecommerce-voice-ai-prototype/voice-enabled/](https://sunilmsft.github.io/ecommerce-voice-ai-prototype/voice-enabled/)**
