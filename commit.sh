#!/bin/bash

: ' 
   Simple "commit" script for linux
   with incrementing message. Initial
   post, to be updated.
'

# Variables
count=$(git rev-list --all --count)
msg='Auto Commit #'$count

# Adds "all" files, commits with auto message
# and pushes changes to GitHub Repository
git add --all && git commit -m "$msg" && git push
