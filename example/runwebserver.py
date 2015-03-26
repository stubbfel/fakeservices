#!/usr/bin/env python3
__author__ = 'dev'
from fake_services.service.webservice.fake_web_server_manager import FakeWebServerManager

config = {
    "/1/a/3/foo/bar.php":
        [
            {
                "response_content_path": "cgi-bin/testA.html"
            }
        ]
}

server = FakeWebServerManager(server_port=80, requests_config=config)
server.start_server()
#server.stop_server()

