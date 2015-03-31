#!/usr/bin/env python3
__author__ = 'dev'
from fake_services.service.webservice.fake_web_server_manager import FakeWebServerManager

config = {
    "/test":
        [
            {
                "response_content_path": "request/test.html"
            }
        ],
    "/test1":
        [
            {
                "response_content_path": "request/testA.html"
            }
        ],
    "/test2":
        [
            {
                "response_content_path": "request/testB.html"
            }
        ],
    "/test3":
        [
            {
                "response_content_path": "request/testC.html"
            }
        ],
    "/test4":
        [
            {
                "response_content_path": "request/test.xml"
            }
        ]

}

server = FakeWebServerManager(server_port=8080, requests_config=config)
server.start_server()
#server.stop_server()

