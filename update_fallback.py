import re

with open('d:/ME/ABI/mamma_website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Revert all menu images back to using the logo.png
new_html = re.sub(r'<img src="https://image\.pollinations\.ai[^"]+" alt="([^"]+)" />', r'<img src="/logo.png" alt="\1" />', html)

with open('d:/ME/ABI/mamma_website/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
