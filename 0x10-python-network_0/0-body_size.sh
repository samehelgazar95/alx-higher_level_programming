#!/bin/bash
# Printing the length of the content
curl -s -I 0.0.0.0:5000 | grep Content-Length | awk '{print $2}'
