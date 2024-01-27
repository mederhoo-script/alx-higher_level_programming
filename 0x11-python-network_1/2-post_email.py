#!/usr/bin/python3
"""
    Script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)

    The email must be sent in the email variable
    You must use the packages urllib and sys
    You are not allowed to import packages other than urllib and sys
    You don’t need to check arguments passed to the script (number or type)
    You must use the with statement
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    mail = sys.argv[2]
    url = sys.argv[1]
    data = {}
    data['email'] = mail
    url_data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, url_data)
    with urllib.request.urlopen(req) as rep:
        body = rep.read().decode('utf-8')
        print(body)
