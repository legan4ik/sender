import generator
import requests


class Sender:
    """This class will have an object with method send()
    All needed values are initialized in constructor.
    """
    def __init__(self, count=None, endpoint=None):
        if count and endpoint:
            self.count = count
            self.endpoint = endpoint
        else:
            raise Exception("Please specify number of requests and endpoint")
        # basic validation of url
        if not self.endpoint.startswith('http://') or \
                not self.endpoint.startswith('http://'):
            raise Exception("Incorrect endpoint")
        if type(count) == int:
            self.lst = generator.generate(self.count)
        else:
            raise Exception("Count must be integer")

    def send(self):
        for d in self.lst:
            return requests.post(self.endpoint, data=d)
