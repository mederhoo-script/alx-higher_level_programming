#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status

    You must use the package urllib
    You are not allowed to import any packages other than urllib
    The body of the response must be displayed like the following
    example (tabulation before -)
     You must use a with statement
"""


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html_content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html_content)))
    print(f"\t- content: {html_content}")
    print(f"\t- utf8 content: {html_content.decode('utf-8')}")
