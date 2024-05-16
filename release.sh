#!/usr/bin/env bash
new_version=$1
echo $new_version
git checkout --orphan temp_branch
git add .
git commit -m $new_version
git branch -D master
git branch -m master
git push --force origin master