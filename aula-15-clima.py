import requests

cidade = "Manaus"

api_key = '321735b99a640c6dd23b5fb15f62fe45'

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

requisicao = requests.get(link)
dict = requisicao.json()

descricao = dict['weather'][0]['description']
temperatura = dict['main']['temp'] - 273.15

print(descricao, f"{temperatura}°C")
