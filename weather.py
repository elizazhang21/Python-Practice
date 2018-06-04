# scrape weather information
# -*- coding: utf-8 -*-
__author__ = 'ElizabethZhang'

from urllib import request, parse
from xml.parsers.expat import ParserCreate

class weatherSaxHandler(object): #Sax=Simple API for XML
    def __init__(self):
        self.location = {}
        self.forcast = []
    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.location = attrs
            attrs.pop('xmlns:yweather')
        if name == 'yweather:forecast':
            self.forcast.append(attrs)
    def end_element(self, name):
        pass
    def char_data(self,text):
        pass

def parse_weather(xml): 
    parser = ParserCreate()
    handler = weatherSaxHandler()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    today = {
        'text': handler.forcast[0]['text'],
        'low': int(handler.forcast[0]['low']),
        'high': int(handler.forcast[0]['high'])
    }
    tomorrow = {
        'text': handler.forcast[1]['text'],
        'low': int(handler.forcast[1]['low']),
        'high': int(handler.forcast[1]['high'])
    }
    d = {
        'today': today,
        'tomorrow': tomorrow
    }
    weather = handler.location
    weather.update(d)
    return weather

def get_weather(city):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")' % city
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query})
    with request.urlopen(yql_url) as f:
        city_xml = f.read().decode('utf-8')
    city_weather = parse_weather(city_xml)
    return city_weather

def main():
    city = input('Weather Forecast in City: ')
    print(get_weather(city))

main()
