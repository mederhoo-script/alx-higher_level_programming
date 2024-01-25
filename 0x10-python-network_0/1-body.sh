#!/bin/bash
# Send a GET request to the URL and display the body of the response
curl -s -w "%{http_code}" -o response.txt "$1" | grep -q 200 && cat response.txt
