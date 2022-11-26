import requests
import webbrowser
from colorama import *
init()
url = 'https://anime777.ru/api/rand'
response=requests.get(url)
genre=input(Fore.YELLOW + "Введите жанр (Enter если не важно)")
year=input("Введите год выпуска (Enter если не важно)")
episodes=input("Введите количество эпизодов (Enter если не важно)" + Style.RESET_ALL)
choise={"genre":genre,
        "year": year,
        "episodes_total": episodes}
response.raise_for_status()
response=requests.get(url, params=choise)
print(Fore.MAGENTA + 'Название:' + Style.RESET_ALL,response.json()['title'])
print(Fore.MAGENTA +"Озвучка:" + Style.RESET_ALL,response.json()['translate'])
print(Fore.CYAN +"Кол-во эпизодов:" + Style.RESET_ALL,response.json()['material_data']['episodes_total'])
print(Fore.CYAN +"Год выпуска:" + Style.RESET_ALL,response.json()['year'])
print(Fore.MAGENTA +"Описание:" + Style.RESET_ALL,response.json()['material_data']['description'])
print(Fore.CYAN +"Жанры:" + Style.RESET_ALL,response.json()['material_data']['all_genres'])
webbrowser.open(response.json()['material_data']["poster_url"])
