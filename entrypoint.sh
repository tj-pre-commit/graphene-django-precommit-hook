#!/usr/bin/env bash

if [[ $(git ls-files -z -o --exclude-standard | wc -l) -eq 1 ]]; then
 echo "Unstaged changes" && exit 1;
else
 python manage.py graphql_schema;
fi