#!/bin/bash
# diplays size of the body response
curl -sLX POST -d "email=test@gmail.com&subjct=I will always be here for PLD" "$1"
