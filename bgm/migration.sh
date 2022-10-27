#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage:  $0  app_label"
  exit 1
fi

app=$1 # the app where we want to perform migration
# shellcheck disable=SC2207
database_migration=($(./manage.py showmigrations "$app" | awk '{print $2}' | tail -2))

# When their is only one initial migration then we update it else we update the current migration
if [ ${#database_migration[@]} == 1 ]; then
  previous_migration=zero
  current_migration=${database_migration[0]}
else
  previous_migration=${database_migration[0]}
  current_migration=${database_migration[1]}
fi

# go to the previous database migration
./manage.py migrate "$app" "$previous_migration"
# remove the current migration since its outdated
rm "$app"/migrations/"${current_migration}".*
# create a new database migration
./manage.py makemigrations "$app"
# migrate the DB to the new migration
./manage.py migrate "$app"
