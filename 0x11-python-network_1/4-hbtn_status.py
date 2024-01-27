#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status

    You must use the package requests
    You are not allow to import packages other than requests
    The body of the response must be display like the following
    example (tabulation before -)

guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$
"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    rep = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(rep.text)))
    print("\t- content: {}".format(rep.text))
