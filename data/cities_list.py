import requests


def get_city_list():
    cities = requests.get('https://gist.githubusercontent.com/gorborukov/0722a93c35dfba96337b/raw/435b297ac6d90d13a68935e1ec7a69a225969e58/russia').json()
    city_list = []
    for city in cities:
        city_list.append(city['city'])
    city_list.remove('Йошкар-Ола')
    return city_list
