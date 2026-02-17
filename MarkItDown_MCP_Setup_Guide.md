# MarkItDown MCP Server Setup Guide for PMs

**Target Audience:** Product Managers in Marketing Engineering  
**Last Updated:** February 12, 2026  
**Time to Complete:** 15-20 minutes

## What This Guide Does

This guide will help you enable the MarkItDown Model Context Protocol (MCP) Server in VS Code, allowing GitHub Copilot to convert documents (PDF, Word, Excel, images, etc.) to Markdown format directly from your editor.

**What you'll be able to do after setup:**
- Convert PDF documents to clean Markdown
- Extract text from Word documents (.docx)
- Convert Excel spreadsheets to Markdown tables
- Extract text from images (OCR)
- Process multiple document types at once
- Ask Copilot to convert documents and summarize the results

---

## Background: What is MarkItDown?

**MarkItDown** is Microsoft's document-to-Markdown conversion tool. It extracts text and structure from various document formats and converts them to clean, readable Markdown.

**Supported formats:**
- PDF documents
- Microsoft Word (.docx, .doc)
- Microsoft Excel (.xlsx, .xls)
- Microsoft PowerPoint (.pptx)
- Images (PNG, JPG, BMP, GIF, WEBP, TIFF)
- HTML files
- Plain text files

**Key benefits for PMs:**
- **Convert documentation to Markdown** – Turn PDFs and Word docs into git-friendly Markdown
- **Extract structured data** – Convert Excel spreadsheets to Markdown tables
- **Prepare content for AI** – Convert documents to Markdown for processing by Copilot or other AI tools
- **Bulk processing** – Use Copilot to convert multiple documents at once
- **No manual copy/paste** – Automate document conversion workflows

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

4. **Python 3.10 or higher** ⚠️ **Required for MarkItDown**
   - Download: https://www.python.org/downloads/ (Choose version 3.10+)
   - **Important:** During installation, check the box: **"Add Python to PATH"**
   - Verify installation: Open PowerShell and run `python --version`
   - Should return something like `Python 3.10.x` or higher

---

## Step-by-Step Setup

### Step 1: Verify Prerequisites

1. Open PowerShell in VS Code (`` Ctrl+` ``)

2. Verify Node.js is installed:
   ```powershell
   node --version
   ```
   Should return `v18.x.x` or higher

3. Verify npm is available:
   ```powershell
   npm --version
   ```

4. **Verify Python is installed:**
   ```powershell
   python --version
   ```
   Should return `Python 3.10.x` or higher

   **If Python is not found:**
   - Download and install Python from https://www.python.org/downloads/
   - **Critical:** Check "Add Python to PATH" during installation
   - Restart VS Code after installation
   - Re-run `python --version` to verify

### Step 2: Install the MarkItDown MCP Server

Install the MarkItDown NPM package globally (so it's available to all your VS Code workspaces):

```powershell
npm install -g markitdown-mcp-npx
```

Verify the installation:
```powershell
npm list -g markitdown-mcp-npx
```

You should see output confirming the package is installed.

### Step 3: Add MarkItDown to Your MCP Configuration

Let GitHub Copilot add the configuration to your `.vscode/mcp.json` file (prevents JSON errors).

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I ``)

2. Switch to **Agent Mode** (toggle at the top of the chat panel)

3. **If this is your first MCP server**, copy and paste this prompt:

```
Add the MarkItDown MCP server to my .vscode/mcp.json configuration file. The server config is:

"markitdown": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "markitdown-mcp-npx"
  ]
}

Create the .vscode folder and mcp.json file if they don't exist.
```

4. **If you already have other MCP servers (like Azure DevOps or Work IQ)**, copy and paste this prompt:

```
Add the MarkItDown MCP server to my existing .vscode/mcp.json configuration file. The server config to add is:

"markitdown": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "markitdown-mcp-npx"
  ]
}

Keep all existing server configurations and add this as a new entry.
```

5. Copilot will create or update your `.vscode/mcp.json` file

6. Verify the configuration was added correctly by opening `.vscode/mcp.json`

### Step 4: Start the MCP Server

1. Open the **MCP Servers** panel in VS Code:
   - Open Command Palette: `Ctrl+Shift+P`
   - Search for: `MCP: Focus on MCP Servers View`
   - (Or look for the MCP icon in the Activity Bar)

2. Find `markitdown` in the list

3. Click the **Start** button next to it

4. The server should start without errors
   - If you get a Python error, make sure Python 3.10+ is installed and in your PATH (see Step 1, #4)

### Step 5: Verify MCP Tools Are Available

1. Open GitHub Copilot Chat (`` Ctrl+Alt+I `` or click the Copilot icon)

2. Switch to **Agent Mode** (toggle at the top of the chat panel)

3. Click the **Refresh Tools** button (circular arrow icon)

4. Look for MarkItDown-related tools in the tool list. You should see tools for document conversion

### Step 6: Test the Connection

Try converting a document:

1. Have a test document ready (PDF, Word, Excel, or image)

2. In Copilot Chat (Agent Mode), try a prompt like:

```
Convert the file "C:\path\to\document.pdf" to Markdown and show me the result
```

Or:

```
Read the Excel file at "C:\Users\ryansc\Documents\data.xlsx" and convert it to Markdown table format
```

3. Copilot should call the MarkItDown tool and display the converted Markdown

4. If this works, you're all set!

---

## Using MarkItDown with Copilot

### Example Prompts

Once you're set up, try these prompts in Copilot Chat (Agent Mode):

**Convert individual documents:**
```
Convert the PDF at C:\Documents\project-requirements.pdf to Markdown
```

```
Extract the content from this Word document and convert to Markdown: C:\Documents\meeting-notes.docx
```

```
Read the Excel spreadsheet at C:\Documents\budget.xlsx and create a Markdown table
```

**Bulk document processing:**
```
Convert all PDF files in C:\Documents\Archive to Markdown format
```

**Extract and analyze:**
```
Convert C:\Documents\proposal.pdf to Markdown, then summarize the key points
```

```
Extract text from the image C:\Screenshots\diagram.png and describe what you see
```

**Prepare content for AI:**
```
Convert C:\Documents\requirements.docx to Markdown, then create a feature list from the content
```

### Combining with Other MCP Servers

You can combine MarkItDown with other tools:

```
Convert C:\Documents\project-plan.pdf to Markdown, then create ADO work items based on the requirements
```

```
Extract text from C:\Documents\specs.docx, convert to Markdown, and ask Work IQ if this aligns with our recent meeting notes
```

---

## Workspace vs. Global Setup

### Workspace-Specific Setup

Configuration lives in your project's `.vscode/mcp.json`.

✅ **Advantages:**
- Can be committed to git and shared with team
- Each project can have different settings
- Easy to see what MCP servers a project uses

❌ **Limitations:**
- Need to set up for each workspace/project

### Global Setup

Configuration applies to all your VS Code workspaces (user settings).

✅ **Advantages:**
- Configure once, works everywhere
- No need to set up for each project

❌ **Limitations:**
- Can't easily share with team
- Configuration lives in user settings (not in repo)

**Recommendation for Marketing Engineering PMs:**

Use **workspace-specific** if working in shared repositories so teammates can use MarkItDown too. Use **global** if it's just for your personal document processing workflow.

---

## Common Troubleshooting

### Problem: Python 3.10+ Not Found

**Symptoms:**
- Error: `Python 3.10+ is required but not found`
- MCP server fails to start

**Solutions:**
1. **Install Python:**
   - Download from https://www.python.org/downloads/
   - Choose Python 3.10 or higher
   - **CRITICAL:** During installation, check "Add Python to PATH"
   - Restart VS Code after installation

2. **Verify Python is in PATH:**
   ```powershell
   python --version
   ```
   Should return `Python 3.10.x` or higher

3. **Check if Python is added to PATH:**
   ```powershell
   Get-Command python
   ```
   Should show the path to python.exe

4. **Manually add Python to PATH:**
   - Search Windows for "Environment Variables"
   - Click "Edit the system environment variables"
   - Click "Environment Variables..." button
   - Find "Path" in the "System variables" section
   - Click "Edit..." and add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\` (adjust version number)
   - Click OK, OK, OK
   - Restart VS Code

---

### Problem: MCP Server Fails to Start

**Symptoms:**
- `markitdown` server shows as "Error" or "Stopped"
- Error: "Process exited with code 1"

**Solutions:**
1. **Check Python version again:**
   ```powershell
   python --version
   ```
   Must be 3.10 or higher

2. **Verify the package is installed:**
   ```powershell
   npm list -g markitdown-mcp-npx
   ```

3. **Reinstall the package:**
   ```powershell
   npm uninstall -g markitdown-mcp-npx
   npm install -g markitdown-mcp-npx
   ```

4. **Check VS Code logs:**
   - In MCP Servers panel, right-click `markitdown` → View Logs
   - Look for specific error messages

5. **Restart VS Code:**
   - Close and reopen VS Code
   - Try starting the server again

---

### Problem: MCP Tools Don't Appear in Copilot Chat

**Symptoms:**
- Copilot Chat doesn't show MarkItDown tools
- Prompts fail with "I don't have access to that tool"

**Solutions:**
1. **Verify the server is running:**
   - Open MCP Servers panel
   - Check if `markitdown` shows as "Running"
   - If not, click Start

2. **Refresh tools in Copilot Chat:**
   - Click the circular arrow (Refresh Tools) button in Chat
   - Toggle Agent Mode off and on

3. **Restart VS Code:**
   - Close and reopen VS Code
   - MCP servers should auto-start on launch

---

### Problem: Document Conversion Fails

**Symptoms:**
- Copilot tries to convert a document but gets an error
- "File not found" or "Access denied" errors

**Solutions:**
1. **Verify the file path:**
   - Use the full absolute path (e.g., `C:\Users\ryansc\Documents\file.pdf`)
   - Avoid relative paths or network paths
   - Ensure the file exists and you have read permissions

2. **Check the file format:**
   - MarkItDown supports: PDF, DOCX, XLSX, PPTX, images, HTML, TXT
   - Unsupported formats will fail

3. **Close files before converting:**
   - If a file is open in another application (Word, Excel, etc.), close it
   - Some file formats lock when open

4. **Check file permissions:**
   - Ensure you have read access to the file
   - Right-click file → Properties → Security to verify

---

### Problem: NPX Command Not Found

**Symptoms:**
- Error: `'npx' is not recognized as an internal or external command`
- MCP server fails to start

**Solutions:**
1. **Verify Node.js is installed:**
   ```powershell
   node --version
   npm --version
   ```

2. **Install Node.js if needed:**
   - Download from https://nodejs.org/
   - Choose LTS version
   - Restart VS Code after installation

3. **Add Node.js to PATH:**
   - If installed but still not found, ensure Node.js is in your system PATH
   - Search Windows for "Environment Variables"
   - Add `C:\Program Files\nodejs\` to the Path variable
   - Restart VS Code

---

### Problem: Package Installation Errors

**Symptoms:**
- Error during `npm install -g markitdown-mcp-npx`
- Permission denied errors

**Solutions:**
1. **Run PowerShell as Administrator:**
   - Right-click PowerShell → Run as Administrator
   - Then run `npm install -g markitdown-mcp-npx`

2. **Check NPM registry:**
   ```powershell
   npm config get registry
   ```
   Should return `https://registry.npmjs.org/`

3. **Clear NPM cache:**
   ```powershell
   npm cache clean --force
   ```

4. **Install again:**
   ```powershell
   npm install -g markitdown-mcp-npx
   ```

---

### Problem: Slow Performance or Timeouts

**Symptoms:**
- Document conversion is very slow
- Requests time out

**Solutions:**
1. **Check file size:**
   - Very large PDF files (500+ pages) may take longer
   - Try with a smaller file first

2. **Check disk space:**
   - Ensure you have free disk space
   - Temporary files are created during conversion

3. **Check system resources:**
   - Document conversion uses CPU and RAM
   - Close other heavy applications

4. **Try a different format:**
   - If a PDF is slow, the issue may be with that specific file
   - Try a different PDF or file format

---

## Security & Privacy Considerations

### File Access

- MarkItDown only accesses files you explicitly ask it to convert
- All file processing happens locally on your machine
- No files are uploaded to external servers

### Best Practices

✅ **Do's:**
- Use full file paths to avoid ambiguity
- Ensure you have permission to read files before converting
- Test with non-sensitive files first

❌ **Don'ts:**
- Don't convert files with sensitive content without reviewing the output
- Don't assume OCR (image text extraction) is 100% accurate
- Don't share converted Markdown containing sensitive information without review

---

## Additional Resources

### Microsoft Resources
- **MarkItDown GitHub:** https://github.com/microsoft/markitdown
- **MarkItDown MCP NPX:** https://github.com/ryzhokov/markitdown-mcp-npx

### Getting Help
- **Teams Channel:** [Power Platform Ninjas](https://teams.microsoft.com/l/team/19:7896b998b92945d68fcfbd5cef889e03@thread.tacv2)
- **GitHub Issues:** https://github.com/ryzhokov/markitdown-mcp-npx/issues

---

## Next Steps

After completing this guide:
1. **Convert your first document** – Start with a simple PDF or Word document
2. **Combine with other tools** – Use MarkItDown with ADO or Work IQ MCP
3. **Automate document workflows** – Ask Copilot to batch-convert documents
4. **Share with your team** – Add the config to your team's `.vscode/mcp.json`

---

## Changelog

| Date | Change |
|------|--------|
| 2026-02-12 | Initial guide created for Marketing Engineering PMs |

---

## Questions or Feedback?

Contact: [Your Team Lead or Engineering Contact]
