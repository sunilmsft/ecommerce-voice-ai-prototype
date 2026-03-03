# Push Handshake Builder Prototype to GitHub Pages
# Usage: .\push-prototype.ps1 or just type 'push-prototype' from anywhere

$source = 'C:\Users\sunilve\OneDrive - Microsoft\Learning\ME PM Lab\PM MCP Server Install Files\AI Voice Assistant prototype\PM-Engineering-Better-Together\Handshake-Builder-Prototype-v3.html'
$repo = "$env:USERPROFILE\sunilmsft-pages"

Push-Location $repo
Copy-Item $source . -Force
git add Handshake-Builder-Prototype-v3.html
$msg = "Update prototype - $(Get-Date -Format 'MMM d, yyyy h:mm tt')"
git commit -m $msg
git push
Pop-Location

Write-Host ""
Write-Host "✅ Pushed! Live in ~30 seconds at:" -ForegroundColor Green
Write-Host "   https://sunilmsft.github.io/ecommerce-voice-ai-prototype/Handshake-Builder-Prototype-v3.html" -ForegroundColor Cyan
