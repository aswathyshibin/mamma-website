import re
import urllib.parse

with open('d:/ME/ABI/mamma_website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Map of items to their pollinations prompt
prompts = {
    'Tea': 'Indian_tea_in_glass_cafe_photography',
    'Black Tea': 'black_tea_in_glass_Kerala_cafe',
    'Lime Tea': 'lime_tea_glass_kerala_cafe_drink',
    'Masala Tea': 'masala_chai_in_kulhad_cafe',
    'Ginger Tea': 'ginger_tea_kerala_glass',
    'Cardamom Tea': 'cardamom_tea_indian_glass',
    'Ginger Tea (Black)': 'black_ginger_tea_glass',
    'Coffee': 'south_indian_filter_coffee_glass',
    'Black Coffee': 'black_coffee_glass_cafe',
    'Chukku Kappi': 'chukku_kappi_dry_ginger_coffee_kerala',
    'Boost': 'boost_hot_malt_milk_drink_mug',
    'Horlicks': 'horlicks_hot_milk_drink_mug',
    'Pazhampori': 'kerala_pazhampori_banana_fritters_plate',
    'Masala Bonda': 'masala_bonda_kerala_snack',
    'Parippuvada': 'parippuvada_kerala_dal_fritters',
    'Mulaku Vada': 'mulaku_vada_kerala_snack',
    'Mulaku Bajji': 'mulaku_bajji_chili_fritters_kerala',
    'Pathiri': 'kerala_pathiri_rice_bread_plate',
    'Omlet Single': 'single_egg_omelette_indian_cafe',
    'Omlet Double': 'double_egg_omelette_plate',
    'Idiyappam': 'idiyappam_string_hoppers_kerala_food',
    'Velleppam': 'vellappam_kerala_appam_plate',
    'Chappathy': 'indian_chapati_roti_plate',
    'Uppu Soda': 'uppu_soda_salt_soda_drink_glass',
    'Fresh Lime': 'fresh_lime_soda_glass_mint',
    'Fresh Mint': 'fresh_mint_lime_soda_drink',
    'Soda Lime': 'soda_lime_drink_glass',
    'Soda Mint': 'mint_soda_drink_glass'
}

def replacer(match):
    name = match.group(1)
    prompt = prompts.get(name, name + ' food photography')
    url = 'https://image.pollinations.ai/prompt/' + urllib.parse.quote(prompt) + '?width=400&height=300&nologo=true'
    return f'<img src="{url}" alt="{name}" />'

# Find all <img> tags inside .menu-img-wrap and replace their src
# We match <img src="..." alt="Item Name" />
new_html = re.sub(r'<img src="[^"]+" alt="([^"]+)" />', replacer, html)

with open('d:/ME/ABI/mamma_website/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
