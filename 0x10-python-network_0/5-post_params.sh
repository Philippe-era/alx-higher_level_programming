#!/bin/bash
# Post request to the email desirable for this task
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
