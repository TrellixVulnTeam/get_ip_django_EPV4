import requests

api_key2 = 'd60722d76693fe5719d84103c6d08d89'

city_name = 'almaty'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key2}'
req = requests.get(url)
data = req.json()

name = data['name']
lon = data['coord']['lon']
lat = data['coord']['lat']

exclude = "minute,hourly"

url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key2}'

print(url2)

req2 = requests.get(url2)
data2 = req2.json()

days = []
nights = []
descr = []

for i in data2['daily']:
    days.append(round(i['temp']['day'] - 273.15, 2))
    nights.append(round(i['temp']['night'] - 273.15, 2))
    descr.append(i['weather'][0]['main'] + ': ' + i['weather'][0]['description'])

data_dict = {'morning': days, 'nights': nights, 'descr': descr}
data_every = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: '',
    7: '',

}

for i in range(0, 7):
    myStr = str(data_dict["morning"][i]) + " " + str(data_dict["nights"][i]) + " " + str(data_dict["descr"][i])
    data_every[i] = myStr


# for item, value in data_dict.items():
#     for i in range(1, 9):
#         for ii in value:
#             data_every[i] = ii
#             print(ii)

print(data_every)


weather = {'weather': data_every}