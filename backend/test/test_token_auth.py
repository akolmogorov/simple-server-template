#encoding: utf-8

from datetime import date, timedelta

from simple_server.token_auth import TokenAuth

__author__ = 'deon'

import unittest


class TestStringMethods(unittest.TestCase):
    def test_equality(self):
        first_token_auth = TokenAuth("user@user.org", date.today(), "127.0.0.1", 1234, "pass")
        second_token_auth = TokenAuth("user@user.org", date.today(), "127.0.0.1", 1234, "pass")

        third_token_auth = TokenAuth("different@user.org", date.today() - timedelta(1),
                                     "192.168.0.1", 4321, "otropass")

        self.assertTrue(first_token_auth == second_token_auth)
        self.assertTrue(second_token_auth != third_token_auth)
        self.assertEqual(first_token_auth, second_token_auth)
        self.assertNotEqual(second_token_auth, third_token_auth)

    def test_token_generation(self):
        principal = "test@user.org"
        expiration_date = date.today()
        ip_addr = "127.0.0.1"
        salt = 1234
        secret = "unpassword"

        original_token_auth = TokenAuth(principal, expiration_date, ip_addr, salt, secret)

        token = original_token_auth.generate_token()
        parsed_from_original_token = TokenAuth.from_token(token)

        # Vamos a probar que generate_token() genera una token que puede parsear
        # el método from_token(token), si efectivamente ambos métodos funcionan,
        # origina_token_auth y parsed_from_original_token deberían ser iguales

        self.assertEqual(original_token_auth, parsed_from_original_token,
                         "el objeto generado por from_token(token) debería ser igual "
                         "al objeto original que generó la token")


if __name__ == '__main__':
    unittest.main()
