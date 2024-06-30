import requests
import os


API_KEY = os.getenv('Key')


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_value = 8 * days
    filtered_data = filtered_data[:nr_value]
    return filtered_data


if __name__ == '__main__':
    get_data(place='tokyo', days=1)