__author__ = 'dev'

import os
import unittest
import urllib.request
import urllib.parse

from fake_services.service.webservice.fake_web_server_manager import FakeWebServerManager


CGI_TEST_SCRIPT_PATH = "cgi-bin/test.py"
CGI_WRONG_SCRIPT_PATH = "cgi"
CGI_FILE_SCRIPT_PATH = "cgi-bin/file_content_response.py"
CGI_VAR_BIN_SCRIPT_PATH = "pybin/file_content_response.py"
SERVER_PORT = 8080
TEST_URL = "http://0.0.0.0:" + str(SERVER_PORT)
TEST_URL_EXPAND = TEST_URL + "/1/a/3/foo/bar.php"
DEFAULT_CONFIG = {
    "/": [{"response_content_path": "cgi-bin/testA.html"}],
    "/1/a/3/foo/bar.php":
        [
            {
                "host_pattern": "^0.0.0.0$",
                "response_content_path": "cgi-bin/testA.html"
            },
            {
                "host_pattern": "0.0.0.0:8080",
                "response_content_path": "cgi-bin/testB.html"
            },
            {
                "response_content_path": "cgi-bin/testC.html"
            }
        ]
}


class TestFakeSever(unittest.TestCase):
    def setUp(self):
        try:
            os.chdir("service/webservice")
        except:
            pass

    def tearDown(self):
        try:
            os.chdir("../..")
        except:
            pass

    def test_file_request(self):
        server = FakeWebServerManager(server_port=SERVER_PORT, requests_config=DEFAULT_CONFIG)
        server.start_server()
        content = urllib.request.urlopen(TEST_URL).read().decode('utf-8')
        content2 = urllib.request.urlopen(TEST_URL_EXPAND).read().decode('utf-8')
        server.stop_server()
        self.assertNotEqual("", content)
        self.assertNotEqual(content, content2)
        self.assertFalse(content.startswith("#"))

    def test_file_var_bin_request_post(self):
        server = FakeWebServerManager(server_port=SERVER_PORT, requests_config=DEFAULT_CONFIG)
        server.start_server()
        content = urllib.request.urlopen(TEST_URL_EXPAND).read().decode('utf-8')
        data = urllib.parse.urlencode({'q': 'Status'})
        content2 = urllib.request.urlopen(TEST_URL_EXPAND, data.encode('utf-8')).read().decode('utf-8')

        server.stop_server()
        self.assertNotEqual("", content)
        self.assertFalse(content.startswith("#"))
        self.assertEqual(content, content2)


if __name__ == '__main__':
    unittest.main()
