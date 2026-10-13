import unittest
from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen

from app import Handler


class TestDevOpsApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_returns_http_200(self):
        with urlopen(self.url) as response:
            self.assertEqual(response.status, 200)

    def test_returns_expected_message(self):
        with urlopen(self.url) as response:
            body = response.read().decode()
        self.assertEqual(body, "Hello from my DevOps application!\n")


if __name__ == "__main__":
    unittest.main()
