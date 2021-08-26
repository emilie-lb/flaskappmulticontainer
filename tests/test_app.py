import unittest
from back.app import app


class Testbasics(unittest.TestCase):

    def test_entry_point(self):
        ''' Function that allows us to retrieve the response code of the query
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

    def test_hello_world(self):
        ''' sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/hello_world")
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
