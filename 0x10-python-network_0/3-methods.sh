#!/bin/bash
# Allows the http messages to be displayed
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
