filepath = r"c:\Users\sunilve\OneDrive - Microsoft\Learning\ME PM Lab\PM MCP Server Install Files\AI Voice Assistant prototype\eCommerce Big Bold\.eCommerce Voice AI Agent prototype - Big Bold.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The em dashes I inserted used wrong Unicode codepoints (U+00E2 U+0080 U+0094)
bad_em = "\u00e2\u0080\u0094"

count = content.count(bad_em)
print("Found %d instances of bad em dash encoding" % count)

# The file's standard em dash encoding (double-encoded UTF-8 via Windows-1252)
# is U+00E2 U+20AC U+201D
existing_em = "\u00e2\u20ac\u201d"
existing_count = content.count(existing_em)
print("Existing standard em dash count: %d" % existing_count)

if count > 0:
    # Replace bad em dashes with the file standard encoding
    content = content.replace(bad_em, existing_em)
    
    verify_bad = content.count(bad_em)
    verify_good = content.count(existing_em)
    print("After fix: bad=%d, standard=%d" % (verify_bad, verify_good))
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("File saved successfully.")
else:
    print("No bad em dashes found, nothing to fix.")
