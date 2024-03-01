#!/bin/bash
# diplays size of the body response
curl -is "$1" | grep '^Allow: '| awk -F 'Allow: ' '{print $2}'
