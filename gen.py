import json

data = {
    'tea': [
        ('Tea', '15.0', '/chai.jpg'),
        ('Black Tea', '12.0', '/chai.jpg'),
        ('Lime Tea', '15.0', '/chai.jpg'),
        ('Masala Tea', '20.0', '/chai.jpg'),
        ('Ginger Tea', '20.0', '/chai.jpg'),
        ('Cardamom Tea', '20.0', '/chai.jpg'),
        ('Ginger Tea (Black)', '15.0', '/chai.jpg')
    ],
    'coffee': [
        ('Coffee', '20.0', '/coffee.jpg'),
        ('Black Coffee', '12.0', '/coffee.jpg'),
        ('Chukku Kappi', '15.0', '/coffee.jpg')
    ],
    'hot-drinks': [
        ('Boost', '30.0', '/coffee.jpg'),
        ('Horlicks', '30.0', '/coffee.jpg')
    ],
    'snacks': [
        ('Pazhampori', '15.0', '/samosa.jpg'),
        ('Masala Bonda', '15.0', '/samosa.jpg'),
        ('Parippuvada', '15.0', '/samosa.jpg'),
        ('Mulaku Vada', '15.0', '/samosa.jpg'),
        ('Mulaku Bajji', '15.0', '/samosa.jpg')
    ],
    'food': [
        ('Pathiri', '15.0', '/samosa.jpg'),
        ('Omlet Single', '20.0', '/samosa.jpg'),
        ('Omlet Double', '40.0', '/samosa.jpg'),
        ('Idiyappam', '10.0', '/samosa.jpg'),
        ('Velleppam', '10.0', '/samosa.jpg'),
        ('Chappathy', '5.0', '/samosa.jpg')
    ],
    'cold-drinks': [
        ('Uppu Soda', '20.0', '/lime.jpg'),
        ('Fresh Lime', '20.0', '/lime.jpg'),
        ('Fresh Mint', '20.0', '/lime.jpg'),
        ('Soda Lime', '25.0', '/lime.jpg'),
        ('Soda Mint', '25.0', '/lime.jpg')
    ]
}

html = []
for category, items in data.items():
    for name, price, img in items:
        block = f'''        <div class="menu-item" data-category="{category}">
          <div class="menu-img-wrap">
            <img src="{img}" alt="{name}" />
            <div class="overlay"><button class="btn-icon">+</button></div>
          </div>
          <div class="menu-info">
            <h3>{name}</h3>
            <span class="price">₹{price}</span>
          </div>
        </div>'''
        html.append(block)

with open('d:/ME/ABI/mamma_website/menu_temp.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))
