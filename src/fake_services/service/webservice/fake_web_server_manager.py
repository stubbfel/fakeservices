__author__ = 'dev'

import os
import stat
import threading
import pkgutil
import shutil

from fake_services.service.webservice.fake_http_request_handler import FakeHTTPRequestHandler
from fake_services.service.webservice.fake_web_server import FakeWebServer


class FakeWebServerManager:

    def __init__(self, server_port, requests_config=None, request_handle_script_path=None):

        cgi_path = request_handle_script_path
        if cgi_path is None:
            cgi_path = pkgutil.get_loader("fake_services.service.webservice.file_content_response").path
            newPath = os.path.basename(cgi_path)
            if not os.path.exists(newPath):
                shutil.copyfile(cgi_path, newPath)

            cgi_path = newPath

        if not os.path.exists(cgi_path):
            raise FileNotFoundError

        if not os.access(cgi_path, os.X_OK):
            st = os.stat(cgi_path)
            os.chmod(cgi_path, st.st_mode | stat.S_IEXEC)

        self.server = FakeWebServer(('', server_port), FakeHTTPRequestHandler, cgi_path, requests_config)

    def start_server(self):
        threading.Thread(target=self.server.serve_forever).start()

    def stop_server(self):
        self.server.shutdown()