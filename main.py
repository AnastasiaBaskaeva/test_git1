import requests
import webbrowser
url = 'https://anime777.ru/api/rand'
response=requests.get(url)
genre=input("Введите жанр (Enter если не важно)")
year=input("Введите год выпуска (Enter если не важно)")
episodes=input("Введите количество эпизодов (Enter если не важно)")
choise={"genre":genre,
        "year": year,
        "episodes_total": episodes}
response.raise_for_status()
response=requests.get(url, params=choise)
print(response.json())
print('Название:',response.json()['title'])
print("Озвучка:",response.json()['translate'])
print("Кол-во эпизодов",response.json()['material_data']['episodes_total'])
print("Год выпуска:",response.json()['year'])
print("Описание",response.json()['material_data']['description'])
print("Жанры:",response.json()['material_data']['all_genres'])
webbrowser.open(response.json()['material_data']["poster_url"])
