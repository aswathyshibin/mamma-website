import re

with open('d:/ME/ABI/mamma_website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Current mapping for the newly added images
mapping_updates = {
    'Mulaku Bajji': '/mulakubajji.png',
    'Pathiri': '/pathiri.png',
    'Omlet Single': '/omlet%20single.png',
    'Omlet Double': '/omlet%20double.png',
    'Idiyappam': '/idiyappam.png',
    'Velleppam': '/velleppam.png',
    'Chappathy': '/chappathi.png'
}

def replacer(match):
    name = match.group(1)
    if name in mapping_updates:
        # replace the img src attribute for this specific item
        return f'<img src="{mapping_updates[name]}" alt="{name}" />'
    return match.group(0) # don't change others

new_html = re.sub(r'<img src="[^"]+" alt="([^"]+)" />', replacer, html)

with open('d:/ME/ABI/mamma_website/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
