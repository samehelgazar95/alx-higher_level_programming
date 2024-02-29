#!/bin/bash
# Print the allowed methods
curl -s -I -X OPTIONS $1 | awk '/Allow:/ {gsub("Allow: ", ""); print}'
