import re

with open('d:/ME/ABI/mamma_website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('d:/ME/ABI/mamma_website/menu_temp.html', 'r', encoding='utf-8') as f:
    menu = f.read()

filters = '''      <div class="menu-filters">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="tea">Tea</button>
        <button class="filter-btn" data-filter="coffee">Coffee</button>
        <button class="filter-btn" data-filter="hot-drinks">Hot Drinks</button>
        <button class="filter-btn" data-filter="snacks">Snacks</button>
        <button class="filter-btn" data-filter="food">Food</button>
        <button class="filter-btn" data-filter="cold-drinks">Cold Drinks</button>
      </div>

      <!-- Menu Grid -->
      <div class="menu-grid" id="menu-grid">
''' + menu + '\n      </div>'

# Regex to replace everything from <div class="menu-filters"> to the closing </div> of menu-grid
new_html = re.sub(r'      <div class="menu-filters">.*?      </div>\s*</section>', filters + '\n    </section>', html, flags=re.DOTALL)

with open('d:/ME/ABI/mamma_website/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
