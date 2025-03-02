import requests


API_KEY = '9c4ccd54ca712c2044d1dc15edf637a0'

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