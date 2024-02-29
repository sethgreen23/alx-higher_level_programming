#!/bin/bash
# diplays size of the body response
curl -s -w '%{size_download}\n' -o /dev/null "$1"
