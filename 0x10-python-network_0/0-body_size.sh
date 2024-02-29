#!/bin/bash
# Printing the length of the content
curl -s -I $1 | grep Content-Length | awk '{print $2}'
