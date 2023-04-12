import eel; 
import requests;

@eel.expose
def get_weather(city):
    api_key = "9341597124d912b5669e6a98711aab2b"
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru' #api для точной погоды сейчас
    
    #https://openweathermap.org/guide - тут смотреть api
    
    gpm = f'https://maps.openweathermap.org/maps/2.0/radar/6/13/24?&appid={api_key}&tm=1600781400' #api для карты осадков хз работает или не
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
        
    else:
        print('error')

eel.init('front', allowed_extensions=['.js', '.html'])
eel.start("index.html")

