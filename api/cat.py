import requests

api_key = 'live_d0WelkY66D47ElpScfa473ODAkB4X6iYb4svJM3ZtfcAvWDYz0UU5TQ8m7tQq4Wx'

Cat = input('ใส่ชื่อสายพันธุ์แมว : ')
url = f''
url_json = ''

result = requests.get(url).json()

name = result[0]['name']
description = result[0]['description']
origin = result[0]['origin']
temperament = result[0]['temperament']
life_span = result[0]['life_span']
intelligence = result[0]('intelligence')  
grooming = result[0]('grooming') 
affection_level = result[0]('affection_level') 

print(f"ข้อมูลสายพันธุ์แมว: {name}")
print(f"คำอธิบาย: {description}")
print(f"แหล่งกำเนิด: {origin}")
print(f"อารมณ์: {temperament}")
print(f"อายุเฉลี่ย: {life_span} ปี")
print(f"ระดับความฉลาด: {intelligence}")
print(f"ระดับความพยายามในการเลี้ยงดู: {grooming}")
print(f"ระดับการรักใคร: {affection_level}")     