web_data = {
    'name': 'india',
    'URL': '',
    'description': '',
    'star_rating': ''
}

for name in web_data:
    web_data[name] = input(f"{name}: ")

print()
for name, value in web_data.items():
  print(f"{name}: {value} ")
