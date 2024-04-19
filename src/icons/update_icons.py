import requests
from tqdm import tqdm


url_template = 'https://openweathermap.org/img/wn/{icon_id}@2x.png'
icons_id = ("01d", "02d", "03d", "04d", "09d", "10d", "11d", "13d", "50d",
            "01n", "02n", "03n", "04n", "09n", "10n", "11n", "13n", "50n")

for icon_id in tqdm(icons_id):
    url = url_template.format(icon_id=icon_id)
    response = requests.get(url)

    if response.status_code == 200:
        with open('{icon_id}.png'.format(icon_id=icon_id), 'wb') as f:
            f.write(response.content)
    else:
        print(f'id: {icon_id}, response: {response.status_code}')
