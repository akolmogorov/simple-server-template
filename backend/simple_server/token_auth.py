import datetime

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
        # todo esto es un mock
        return "mocktoken"

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def from_token(cls, token):
        # todo esto es un mock

        principal = "mock@mock.org"
        expiration_date = datetime.date.today()
        ip_addr = "127.0.0.1"
        salt = 8234
        secret = "unpassword"

        return cls(principal, expiration_date, ip_addr, salt, secret)
