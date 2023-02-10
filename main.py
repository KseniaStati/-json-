import json
import requests

#Здесь гет запрос на сервер и запись ответа в файл
headers = {
    'email': 'tommycyberus@gmail.com',
    'password': '1234567890'
}

json_data=requests.get(url='https://petfriends.skillfactory.ru/api/key', headers=headers)
#print(json_data.json)

#print(json.dumps(json_data.text))

h = {
    'auth_key':'cf3d04fce5cd5021edce8fd713dc2d865e2ac0e2d7e0c29261bf196d',
      }
f = requests.get(url='https://petfriends.skillfactory.ru/api/pets?filter=my_pets', headers=h)
f.text.encode('ascii').decode('unicode_escape')

with open('json_data5.json', 'w', encoding='utf8') as t:
    print('JSON Ответ:',f.json())
    print('JSON Ответ:', f.text.encode('ascii').decode('unicode_escape'))
    print(type(f.json()))
    print(type(f.text))
    json.dump(f.json(),t,ensure_ascii=False)




"""

#data = json.loads(json_data.text)
#print(data)
r = requests.get(url='https://petfriends.skillfactory.ru/api/pets?filter=my_pets', headers=h)
r.encoding = 'windows-1251'
print (json.dumps(r.text))
print(r.text.encode('ascii').decode('unicode_escape'))


with open('json_data.json', 'w', encoding='utf8') as response:
    response = requests.get('https://petfriends.skillfactory.ru/api/pets?filter=my_pets', headers=h)
    todos = json.loads(response.text.encode('ascii').decode('unicode_escape'))
    print(todos == response.json())  # True
    # print(type(todos))




# with open('json_data.json', encoding='utf8') as f:
#     tr=json.load(f)
#     print(tr)

"""