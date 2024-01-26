#!/usr/bin/python3
"""
    script that takes in a URL, sends a request
    to the URL and displays the value of the
    X-Request-Id variable found in the header of the response.
    You must use the packages urllib and sys
    You are not allow to import packages other than urllib and sys
    The value of this variable is different for each request
    You don’t need to check arguments passed to the script (number or type)
    You must use a with statement
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as rep:
        html_rep = rep.read()
x_id = rep.headers["X-Request-Id"]
print(x_id)
