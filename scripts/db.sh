#!/bin/bash

podman run -d \
  --name marketdraw-db \
  --publish 127.0.0.1:5432:5432 \
  -e POSTGRES_PASSWORD="$PG_PWD" \
  --volume marketdraw-data:/var/lib/postgresql \
  docker.io/library/postgres:18