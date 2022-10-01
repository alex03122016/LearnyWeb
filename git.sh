#!/usr/bin/env bash

git status
git add .
git commit -m "removed unused files"
git remote add origin https://github.com/alex03122016/LearnyWeb
git push -u origin master
