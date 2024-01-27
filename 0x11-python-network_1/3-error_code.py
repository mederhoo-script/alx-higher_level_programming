#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
 and displays the body of the response (decoded in utf-8).

    You have to manage urllib.error.HTTPError exceptions
    and print: Error code: followed by the HTTP status code
    You must use the packages urllib and sys
    You are not allowed to import other packages than urllib and sys
    You don’t need to check arguments passed to the script (number or type)
    You must use the with statement
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as rep:
            body = rep.read().decode('UTF-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
