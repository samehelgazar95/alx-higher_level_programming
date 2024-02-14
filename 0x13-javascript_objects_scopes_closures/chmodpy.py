#!/usr/bin/python3
import sys
import os

for file in sys.argv[1:]:
    os.chmod(file, 0o777)
