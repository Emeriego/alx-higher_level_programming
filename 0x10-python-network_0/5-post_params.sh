#!/bin/bash
# POST request to the passed URL using curl, shows the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
