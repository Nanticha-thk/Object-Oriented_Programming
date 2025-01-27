import requests

api_key = 'your_cat_api_key'
cat = 'Abyssinian'
url = f'https://api.thecatapi.com/v1/breeds/search?q={cat}'

headers = {'x-api-key': api_key}

result = requests.get(url, headers=headers).json()

breed = result[0] 
name = breed['name']
description = breed['description']
origin = breed['origin']
temperament = breed['temperament']
life_span = breed['life_span']
intelligence = breed['intelligence']
grooming = breed['grooming']
affection_level = breed['affection_level']

print(f"ข้อมูลสายพันธุ์แมว: {name}")
print(f"คำอธิบาย: {description}")
print(f"แหล่งกำเนิด: {origin}")
print(f"อารมณ์: {temperament}")
print(f"อายุเฉลี่ย: {life_span} ปี")
print(f"ระดับความฉลาด: {intelligence}")
print(f"ระดับความพยายามในการเลี้ยงดู: {grooming}")
print(f"ระดับการรักใคร: {affection_level}")
