#!/bin/bash
# A JSON POST request to a URL, shows the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
