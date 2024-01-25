#!/bin/bash
# with curl takes URL and displays the HTTP acceptable by the server
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -d ' ' -f 2-
