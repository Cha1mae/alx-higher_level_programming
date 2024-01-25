#!/bin/bash
# so basically displays the URL size of the body of the response
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
