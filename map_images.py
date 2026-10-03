import re

with open('d:/ME/ABI/mamma_website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

mapping = {
    'Tea': '/chai.jpg',
    'Black Tea': '/chai.jpg',
    'Lime Tea': '/chai.jpg',
    'Masala Tea': '/chai.jpg',
    'Ginger Tea': '/chai.jpg',
    'Cardamom Tea': '/chai.jpg',
    'Ginger Tea (Black)': '/chai.jpg',
    'Coffee': '/coffee.jpg',
    'Black Coffee': '/coffee.jpg',
    'Chukku Kappi': '/coffee.jpg',
    'Boost': '/coffee.jpg',
    'Horlicks': '/coffee.jpg',
    'Pazhampori': '/pazhampori.png',
    'Masala Bonda': '/masalabonda.png',
    'Parippuvada': '/parippuvada.png',
    'Mulaku Vada': '/mulakuvada.png',
    'Mulaku Bajji': '/samosa.jpg',
    'Pathiri': '/samosa.jpg',
    'Omlet Single': '/samosa.jpg',
    'Omlet Double': '/samosa.jpg',
    'Idiyappam': '/samosa.jpg',
    'Velleppam': '/samosa.jpg',
    'Chappathy': '/samosa.jpg',
    'Uppu Soda': '/lime.jpg',
    'Fresh Lime': '/lime.jpg',
    'Fresh Mint': '/lime.jpg',
    'Soda Lime': '/lime.jpg',
    'Soda Mint': '/lime.jpg'
}

def replacer(match):
    name = match.group(1)
    img = mapping.get(name, '/logo.png')
    return f'<img src="{img}" alt="{name}" />'

new_html = re.sub(r'<img src="[^"]+" alt="([^"]+)" />', replacer, html)

with open('d:/ME/ABI/mamma_website/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
