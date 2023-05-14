import re

with open('index.html', 'r') as f:
    html_code = f.read()
    # <div\s+id="(?P<id>[^"]+)">\s для id
    # <a\s+href="(?P<href>[^"]+)">\s для ссылки
    # >\s*(?P<text>[^<]+)\s*</a> для текста

pattern = re.compile(r'<div\s+id="(?P<id>[^"]+)">\s*<a\s+href="(?P<href>[^"]+)">\s*(?P<text>[^<]+)\s*</a>')
results = []
matches = re.findall(pattern, html_code)

for match in matches:
    domain = re.search(r'(?:https?:\/\/)?(?:www\.)?([^:\/\n]+)', match[1]).group(1)
    results.append((match[0], domain, match[2].strip()))

print(results)
