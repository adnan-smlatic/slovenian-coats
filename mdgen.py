
import json

with open('index.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

cities = data['Slovenia']['Divisions']['Level_2']['List']

# Initialize Markdown content with the appropriate grid header
md_content = "| | | | |\n|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|\n"

# Iterate through cities and prepare entries for each city
entries = []
for city_name, city_info in cities.items():
    image_path = f"images/{city_info['Properties']['file_name']}"
    description = f"**{city_info['name']}**<br>Grb občine {city_info['name']}<br>Coat of arms of {city_info['name']}<br>Wappen der Gemeinde {city_info['name']}"
    image_markdown = f"<img width=\"300\" alt=\"{city_info['name']}\" src=\"{image_path}\"><br>{description}"
    entries.append(image_markdown)

# Organize the entries into rows of 4 columns
for i in range(0, len(entries), 4):
    row = entries[i:i+4]
    while len(row) < 4:
        row.append("")  # Fill empty cells if any
    md_content += "| " + " | ".join(row) + " |\n"

with open('readme4.md', 'w', encoding='utf-8') as md_file:
    md_file.write(md_content)
