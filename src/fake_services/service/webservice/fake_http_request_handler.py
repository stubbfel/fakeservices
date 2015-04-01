__author__ = 'dev'

import re
from http.server import SimpleHTTPRequestHandler

HEADERS_HOST_PARAMETER_KEY_NAME = "Host"
REQUEST_LINE_ENCODING = "iso-8859-1"
HOST_PATTERN_KEY_NAME = "host_pattern"
RESPONSE_CONTENT_PATH_KEY_NAME = "response_content_path"


class FakeHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.__set_path_setting()
        SimpleHTTPRequestHandler.do_GET(self)

    def do_HEAD(self):
        self.__set_path_setting()
        SimpleHTTPRequestHandler.do_HEAD(self)

    def do_POST(self):
        self.command = "GET"
        self.do_GET()

    def __set_path_setting(self):
        response_content_path = None
        if self.server.requests_config is not None:
            server_path = self.__get_server_path()
            if server_path in self.server.requests_config:
                request_config = self.server.requests_config[server_path]
                response_content_path = self.__get_response_content_path(request_config)

        if response_content_path is not None:
            self.path = response_content_path
        else:
            self.path = "/404"

    def __get_response_content_path(self, request_config):
        sorted_configs = sorted(request_config, key=len, reverse=True)
        server_host = self.__get_server_host()
        for config in sorted_configs:
            if HOST_PATTERN_KEY_NAME in config:
                result = re.search(config[HOST_PATTERN_KEY_NAME], server_host)
                if result is None:
                    continue

            if RESPONSE_CONTENT_PATH_KEY_NAME in config:
                return config[RESPONSE_CONTENT_PATH_KEY_NAME]
        return None

    def __get_server_path(self):
        request_line = str(self.raw_requestline, REQUEST_LINE_ENCODING).rstrip('\r\n')
        words = request_line.split()
        if len(words) < 2:
            return ""

        return words[1]

    def __get_server_host(self):
        return self.headers[HEADERS_HOST_PARAMETER_KEY_NAME]