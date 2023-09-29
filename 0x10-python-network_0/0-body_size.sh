#!/bin/bash
# The script will return the http requested
curl -s "$1" | wc -c
