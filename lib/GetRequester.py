import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        personel_list = []
        personel = json.loads(self.get_response_body())
        for person in personel:
            personel_list.append(personel)
        
        return personel

# my_personel = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')

# print(my_personel.load_json())