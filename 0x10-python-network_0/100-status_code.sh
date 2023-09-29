#!/bin/bash
# Get request in place
curl -s -o /dev/null -w "%{http_code}" "$1"
