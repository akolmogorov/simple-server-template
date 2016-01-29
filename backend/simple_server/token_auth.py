import json

from dateutil import parser

__author__ = 'deon'


class TokenAuth:
    """ Genera y parsea tokens """

    def __init__(self, principal, expiration_date, ip_addr, salt, secret):
        self.principal = principal
        self.expiration_date = expiration_date
        self.ip_addr = ip_addr
        self.salt = salt
        self.secret = secret

    def generate_token(self):
        return json.dumps(
            {"principal": self.principal, "expiration_date": self.expiration_date.isoformat(), "ip_addr": self.ip_addr,
             "salt": self.salt, "secret": self.secret})

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def from_token(cls, token):
        j = json.loads(token)

        principal = j["principal"]
        expiration_date = parser.parse(j["expiration_date"])
        ip_addr = j["ip_addr"]
        salt = j["salt"]
        secret = j["secret"]

        return cls(principal, expiration_date, ip_addr, salt, secret)
