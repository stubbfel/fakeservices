#!/usr/bin/env python3
__author__ = 'dev'
import cgi

from fake_services.service.webservice.fake_http_request_handler import RESPONSE_PATH_PARAMETER_KEY_NAME

response_file_path = cgi.FieldStorage()[RESPONSE_PATH_PARAMETER_KEY_NAME].value
response_file = open(response_file_path, "r")
response_file_content = response_file.read()
response_file.close()

print("\n")
print(response_file_content)


