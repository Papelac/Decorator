import os
import datetime
import requests

def logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
 
        with open('old_HW.log', 'a+') as f:
            f.write(f'Вызов функции - {datetime.datetime.now()}, Имя функции - {old_function.__name__}, Аргументы - {args, kwargs}, Результат - {result}\n')

        return result

    return new_function

@logger
def hero_request():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    base_url = requests.get(url)
    return base_url.json()

List_of_heroes = ['Hulk', 'Captain America', 'Thanos']

if __name__ == '__main__':
    base_hero = hero_request()
    smartest_hero = ''
    smartest_hero_point = 0
    for hero in base_hero:
        if hero['name'] in List_of_heroes:
            if hero['powerstats']['intelligence'] > smartest_hero_point:
                smartest_hero = hero['name']
                smartest_hero_point = hero['powerstats']['intelligence']
    print(f'{smartest_hero} is a smartest hero, he has {smartest_hero_point} intelligence point')