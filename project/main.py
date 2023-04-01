import eel; 
import requests;

@eel.expose
def get_weather(city):
    api_key = "9341597124d912b5669e6a98711aab2b"
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
        
    else:
        print('error')

eel.init('front', allowed_extensions=['.js', '.html'])
eel.start("index.html")

