import requests
import webbrowser
from colorama import *
# https://anime777.ru/api/rand?genre=%D0%A1%D0%BF%D0%BE%D1%80%D1%82
init()
a = Fore.MAGENTA
b = Fore.YELLOW
c = Fore.CYAN
d=Fore.RESET
print(a + '\n\t\t' "Добро пожаловать!")
print(a)

def run():

        url = 'https://anime777.ru/api/rand'
        response = requests.get(url)
        choise = {"genre": input(b + "Введите жанр (Enter если не важно)" + d),
                  "year": input(b + "Введите год выпуска (Enter если не важно)" + d),
                  "episodes_total" : input(b + "Введите количество эпизодов (Enter если не важно)" + d)}
        response.raise_for_status()
        response = requests.get(url, params=choise)
        print_request(response)
        save_history(response)
        save_to_favourites(response)

def print_request(response):

        print(c + 'Название:' + d, a, response.json()['title'])
        print(c + "Озвучка:" + d, a, response.json()['translate'])
        print(c + "Кол-во эпизодов:" + d, a, response.json()['material_data']['episodes_total'])
        print(c + "Год выпуска:" + d, a, response.json()['year'])
        print(c + "Описание:" + d, a, response.json()['material_data']['description'])
        print(c + "Жанры:" + d, a, response.json()['material_data']['all_genres'])
        webbrowser.open(response.json()['material_data']["poster_url"])

def save_history(response):

        with open("history.txt", "a") as f:
                print("Кол-во эпизодов:", response.json()['material_data']['episodes_total'], file=f)
                print("Год выпуска:",  response.json()['translate'], file=f)
                print('Название:', response.json()['title'], file=f)
                print("Озвучка:", response.json()['year'], file=f)
                print("Описание:", response.json()['material_data']['description'], file=f)
                print("Жанры:", response.json()['material_data']['all_genres'], file=f)
                print("__________________________________________", file=f)
def save_to_favourites(response):
        favourite = input(b + "Добавить в избранное? да/нет")
        if favourite == "да":
                with open("favourite.txt", "a") as h:
                        print('Название:', response.json()['title'], file=h)
                        print("Озвучка:", response.json()['translate'], file=h)
                        print("Кол-во эпизодов:", response.json()['material_data']['episodes_total'], file=h)
                        print("Год выпуска:", response.json()['year'], file=h)
                        print("Описание:", response.json()['material_data']['description'], file=h)
                        print("Жанры:", response.json()['material_data']['all_genres'], file=h)
                        print("__________________________________________", file=h)
run()
while True:
        ask = (b + input("Хотите продолжить? да/нет" + a))
        if ask == "да":
                run()
        else:
                print(a + '\n\t\t', "Хорошего дня!")
                input(b + "Enter чтобы закрыть" + a)
                break