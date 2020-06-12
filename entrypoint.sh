#!/usr/bin/env bash

has_missing() {
  if [[ $(git ls-files -z -o --exclude-standard | wc -l) -eq 1 ]]; then
    echo "Unstaged changes" && exit 1;
  fi
}

has_missing
python manage.py graphql_schema
has_missing