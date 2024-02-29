#!/bin/bash
# diplays size of the body response
curl -s -i -N "$1" | grep -zP 'HTTP\/\d\.\d 200 OK(.|\n)*' | tail -n 1
