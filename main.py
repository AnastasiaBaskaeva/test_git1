import requests
import webbrowser
<<<<<<< Updated upstream
from colorama import *
init()
def run():
        url = 'https://anime777.ru/api/rand'
        response=requests.get(url)
        choise={"genre":input(Fore.YELLOW + "Введите жанр (Enter если не важно)"),
                "year": input("Введите год выпуска (Enter если не важно)"),
                "episodes_total": input("Введите количество эпизодов (Enter если не важно)" + Style.RESET_ALL)}
        response.raise_for_status()
        response=requests.get(url, params=choise)
        print_request(response)
        save_history(response)
def print_request(response):
        print(Fore.MAGENTA + 'Название:' + Style.RESET_ALL,response.json()['title'])
        print(Fore.MAGENTA +"Озвучка:" + Style.RESET_ALL,response.json()['translate'])
        print(Fore.CYAN +"Кол-во эпизодов:" + Style.RESET_ALL,response.json()['material_data']['episodes_total'])
        print(Fore.CYAN +"Год выпуска:" + Style.RESET_ALL,response.json()['year'])
        print(Fore.MAGENTA +"Описание:" + Style.RESET_ALL,response.json()['material_data']['description'])
        print(Fore.CYAN +"Жанры:" + Style.RESET_ALL,response.json()['material_data']['all_genres'])
        webbrowser.open(response.json()['material_data']["poster_url"])
def save_history(response):
        with open("history.txt", "a") as f:
                print('Название:', response.json()['title'], file=f)
                print("Озвучка:", response.json()['translate'], file=f)
                print("Кол-во эпизодов:", response.json()['material_data']['episodes_total'], file=f)
                print("Год выпуска:", response.json()['year'], file=f)
                print("Описание:", response.json()['material_data']['description'], file=f)
                print("Жанры:", response.json()['material_data']['all_genres'], file=f)
                print("__________________________________________", file=f)
run()
input("Enter чтобы закрыть")
=======
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
print('Название:',response.json()['title'])
print("Озвучка:",response.json()['translate'])
print("Кол-во эпизодов:",response.json()['material_data']['episodes_total'])
print("Год выпуска:",response.json()['year'])
print("Описание:",response.json()['material_data']['description'])
print("Жанры:",response.json()['material_data']['all_genres'])
webbrowser.open(response.json()['material_data']["poster_url"])
>>>>>>> Stashed changes
