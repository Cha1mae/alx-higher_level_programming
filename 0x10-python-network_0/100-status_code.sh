#!/bin/bash
# uh tikchbila tiwliwla Curl o URL displays status
curl -s -I -o HEAD -w "%{http_code}" "$1"
