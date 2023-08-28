#!/bin/bash

# 获取当前日期和时间
current_date=$(date +"%Y-%m-%d")

git add -A

git commit -m "$current_date"

git push origin master