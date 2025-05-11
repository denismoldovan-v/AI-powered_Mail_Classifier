import json
from bs4 import BeautifulSoup

# Assuming your JSON is stored in a file named 'emails.json'
with open('D:\\Hackathon\\taskmanager\\Resources\\stuff.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

# Convert JSON to a Python list of dictionaries
emails_list = json.loads(json_data)
conts = []
for i in emails_list:
    conts.append(i['body'])

new_l = []
for i in conts:
    soup = BeautifulSoup(i, 'html.parser')
    txt = soup.select("p")
    for k in txt:
        print(k.get_text())



