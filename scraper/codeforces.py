import pip._vendor.requests as requests
import logging
from pprint import pprint
from platform import Platform 
from contest import Contest

class Codeforces(Platform):

    def __init__(self):
        
        self.name = "codeforces"
        self.url = "https://codeforces.com/api/"
        self.params = {"gym": "false"}

    def scrap(self):

        request = requests.get(f"{self.url}/contest.list", self.params)
        data = request.json()

        return self.extract(data)
    
    def extract(self, data):

        contest = []

        for contest in data["result"]:
            if contest["phase"]=="BEFORE":

                name = contest["name"]
                platform = self.name

                # to be continued


