#!/usr/bin/env python3
__author__ = 'dev'

response_file_path = "cgi-bin/test.html"
response_file = open(response_file_path, "r")
response_file_content = response_file.read()
response_file.close()

print("\n")
print(response_file_content)