#!/bin/bash
# using GET request to the URL, and displays the body ;)
[ "$(curl -L -s -X HEAD -w "%{http_code}" "$1")" == '200' ] && curl -Ls "$1"
