from .util import headers, objects
from requests import Session

class randStuff:
    def __init__(self):
        self.api = 'https://randstuff.ru/{}/generate/'.format
        self.session = Session()
        self.headers = headers.Headers().headers

    def number(self, start: int, end: int, count: int):
        data = {'start': start, 'end': end, 'count': count}
        req = self.session.post(url = self.api('number'), headers = self.headers, data = data)
        return objects.Number(req.json()).Number

    def password(self, length: int, numbers: int, symbols: int):
        data = {'length': length, 'numbers': numbers, 'symbols': symbols}
        req = self.session.post(url = self.api('password'), headers = self.headers, data = data)
        return objects.Password(req.json()).Password

    def ask(self, question):
        data = {'question': question}
        req = self.session.post(url=self.api('ask'), headers=self.headers, data=data)
        return objects.Ask(req.json()).Ask

    def ticket(self):
        req = self.session.post(url=self.api('ticket'), headers=self.headers)
        return objects.Ticket(req.json()).Ticket

    def fact(self):
        req = self.session.post(url=self.api('fact'), headers=self.headers)
        return objects.Fact(req.json()).Fact

    def saying(self):
        req = self.session.post(url=self.api('saying'), headers=self.headers)
        return objects.Saying(req.json()).Saying