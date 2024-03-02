#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
do this ./6-post_email.py <URL> <email>, to
display the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    req = requests.post(url, data=val)
    print(req.text)
