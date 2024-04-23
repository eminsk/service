class Weather:
    """ Класс для получения данных о погоде """

    def __init__(self, weather_api_key):
        """ Инициализация класса """
        self.weather_api_key = weather_api_key
        self.lat = 53.0185
        self.lon = 28.0049
        self.params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": self.weather_api_key,
            "units": "metric",
            "lang": "ru"
        }
        self.url = "https://api.openweathermap.org/data/2.5/onecall"

    def get_weather_data(self):
        """ Получение данных о погоде """
        response = __import__('requests').get(self.url, params=self.params)
        if response.status_code == 200:
            ip, city = self.get_ip()
            data = response.json()
            current = data["current"]
            daily = data["daily"][0]
            return {
                "city": {city},
                "temp": current["temp"],
                "feels_like": current["feels_like"],
                "pressure": current["pressure"],
                "humidity": current["humidity"],
                "clouds": current["clouds"],
                "description": current["weather"][0]["description"],
                "icon": current["weather"][0]["icon"],
                "min_temp": daily["temp"]["min"],
                "max_temp": daily["temp"]["max"],
                "daily_feels_like": daily["feels_like"]["day"],
                "daily_pressure": daily["pressure"],
                "daily_humidity": daily["humidity"],
                "daily_clouds": daily["clouds"],
                "daily_description": daily["weather"][0]["description"],
                "daily_icon": daily["weather"][0]["icon"]
            }
        else:
            return {}

    def get_ip(self):
        """ Получение IP-адреса """
        try:
            response = __import__('requests').get(
                'https://ipinfo.io/json', timeout=0.5)
            data = response.json()
            return data['ip'], data['city']
        except (__import__('requests').exceptions.RequestException, ValueError):
            return 'неизвестен', 'неизвестен'
