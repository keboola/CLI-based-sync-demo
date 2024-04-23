#!/bin/bash

currentDate=`date +%Y-%m-%d:%T%Z`
pull_log=`cat "$RUNNER_TEMP/log.txt"`
git config --global user.name 'Keboola CLI'
git config --global user.email 'keboola-cli@users.noreply.github.com'
git add -A
git commit -a -m "Manual KBC pull $currentDate" -m "$pull_log" || true
git push