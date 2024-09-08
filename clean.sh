#!/bin/bash
# Move all subdirectory files to the current directory
find . -mindepth 2 -type f -exec mv -t . {} +

# Remove all empty subdirectories
find . -mindepth 1 -type d -empty -exec rmdir {} +

