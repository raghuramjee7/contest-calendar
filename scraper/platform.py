import pip._vendor.requests as requests
import logging
from pprint import pprint


class Platform:

    def __init__(self, name, url, params=None):
        self.name = name
        self.url = url
        self.params = params

    def scrap(self):

        return
    
    def extract(self):

        return
    
    def commit(self):

        return