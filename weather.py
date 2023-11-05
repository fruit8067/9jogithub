import requests

Rain = 1
Snow = 2
Sun = 3
Thunderstorm = 4
Wind = 5

class Weather:
    state = 0
    temperature = 0
    def __init__(self):
        self.state = self.get_weather_state
        self.temperature = self.get_weather_temperature
    
    def get_weasther_state(self):
        return self.state
    
    def get_weather_temperature(self):
        return self.temperature