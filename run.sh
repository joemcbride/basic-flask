#!/usr/bin/env bash
docker build --rm -t flaskapp:local .
docker run -p 5000:5000 flaskapp:local
