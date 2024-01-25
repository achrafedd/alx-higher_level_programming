#!/bin/bash
# Send request and display body size
curl -s "$1" | wc -c
