#!/bin/bash
# A request to an URL with curl, and displays the size of the response
curl -s "$1" | wc -c
