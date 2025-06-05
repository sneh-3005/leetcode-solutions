#!/bin/bash
git add .
msg="Auto commit: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$msg"
git push
